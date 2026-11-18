#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""Local similarity self-check (Drillbit-style proxy, zero dependency).

Drillbit/Turnitin flag runs of identical consecutive words against web, journal
and student-paper indexes. This script estimates that locally: the share of
words in the candidate text covered by word n-grams (default n=8) that also
appear in any reference text (old drafts, earlier Tugas, source PDFs/notes).

Usage:
  simcheck.py CANDIDATE --ref REF [REF ...] [--n 8] [--top 15]
  simcheck.py --pairs ORIG.json NEW.json [--n 6] [--max 15]
CANDIDATE/REF: .odt .docx .pdf .txt .md .json (segments list with "text").
"""
import argparse, json, re, subprocess, sys, zipfile, html


def load(path):
    p = path.lower()
    if p.endswith('.json'):
        d = json.load(open(path, encoding='utf-8'))
        return '\n'.join(s['text'] for s in d) if isinstance(d, list) else str(d)
    if p.endswith('.odt') or p.endswith('.docx'):
        z = zipfile.ZipFile(path)
        x = z.read('content.xml' if p.endswith('.odt') else 'word/document.xml').decode('utf-8')
        x = re.sub(r'</(text:p|text:h|w:p)>', '\n', x)
        return html.unescape(re.sub(r'<[^>]+>', ' ', x))
    if p.endswith('.pdf'):
        return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout
    return open(path, encoding='utf-8', errors='ignore').read()


def strip_refs(t):
    # cut bibliography so it does not dominate (Drillbit usually excludes it)
    m = re.search(r'\n\s*DAFTAR PUSTAKA\s*\n(?![^\n]*\t\d)', t)
    if m:
        rest = t[m.end():]
        n = re.search(r'\n\s*(AI DISCLAIMER|PERNYATAAN INTEGRITAS|LAMPIRAN)', rest)
        t = t[:m.start()] + ('\n' + rest[n.start():] if n else '')
    return t


def words(t):
    return re.findall(r'[0-9a-zà-ÿ]+', t.lower())


def grams(w, n):
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def coverage(cand, refset, n):
    cov = [False] * len(cand)
    for i in range(len(cand) - n + 1):
        if tuple(cand[i:i + n]) in refset:
            for j in range(i, i + n):
                cov[j] = True
    return cov


def runs(cand, cov):
    out, i = [], 0
    while i < len(cov):
        if cov[i]:
            j = i
            while j < len(cov) and cov[j]:
                j += 1
            out.append((j - i, ' '.join(cand[i:j])))
            i = j
        else:
            i += 1
    return sorted(out, reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cand', nargs='?')
    ap.add_argument('--ref', nargs='*', default=[])
    ap.add_argument('--pairs', nargs=2)
    ap.add_argument('--n', type=int, default=8)
    ap.add_argument('--top', type=int, default=15)
    ap.add_argument('--max', type=float, default=15.0, help='flag segment if coverage%% above')
    ap.add_argument('--keep-refs', action='store_true')
    a = ap.parse_args()
    if a.pairs:
        o = {s['id']: s['text'] for s in json.load(open(a.pairs[0], encoding='utf-8'))}
        new = json.load(open(a.pairs[1], encoding='utf-8'))
        tot = hit = 0
        for s in new:
            c = words(s['text']); r = grams(words(o.get(s['id'], '')), a.n)
            cov = coverage(c, r, a.n); k = sum(cov)
            tot += len(c); hit += k
            pct = 100 * k / max(1, len(c))
            if pct > a.max:
                print(f"id={s['id']} {pct:.0f}% longest: {runs(c, cov)[0][1][:120]}")
        print(f'OVERALL {a.n}-gram overlap with original: {100*hit/max(1,tot):.1f}% ({len(new)} segments)')
        return
    t = load(a.cand)
    if not a.keep_refs:
        t = strip_refs(t)
    c = words(t)
    print(f'candidate: {len(c)} words (bibliography {"kept" if a.keep_refs else "excluded"})')
    allcov = [False] * len(c)
    for ref in a.ref:
        rt = load(ref)
        cov = coverage(c, grams(words(rt), a.n), a.n)
        allcov = [x or y for x, y in zip(allcov, cov)]
        print(f'  vs {ref}: {100*sum(cov)/max(1,len(c)):.1f}%')
    print(f'COMBINED {a.n}-gram coverage: {100*sum(allcov)/max(1,len(c)):.1f}%')
    for L, s in runs(c, allcov)[:a.top]:
        print(f'  [{L}] {s[:160]}')


if __name__ == '__main__':
    main()
