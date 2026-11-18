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
"""Validate paraphrased segments against original for BOTH:
1. DrillBit Similarity (< 30% target -> < 8% 6-gram overlap against original)
2. DrillBit AI Content Detection (< 30% target -> burstiness CV, short sentence injection,
   low me-...-kan / secara / merupakan density, no parallel list verb cloning).
3. Factual & formatting integrity (IDs, list labels, numbers, citations, balanced *italics*).
"""
import json, re, sys, statistics

o = json.load(open(sys.argv[1], encoding='utf-8'))
n = json.load(open(sys.argv[2], encoding='utf-8'))
if [s['id'] for s in o] != [s['id'] for s in n]:
    print('ID MISMATCH'); sys.exit(1)

def nums(t):
    return set(re.findall(r'\d+(?:[.,]\d+)*[ab]?', t))

def cites(t):
    out = set()
    for par in re.findall(r'\(([^()]*\d{4}[ab]?|[^()]*t\.t\.)\)', t):
        for nm in re.findall(r'([A-Z][A-Za-z\-\.]+(?: [A-Z][A-Za-z\-]+)*)', par):
            w0 = nm.split()[0]
            if w0 not in ('UU', 'PP', 'Perpres', 'SE', 'RFC', 'XEP', 'STANAG', 'Nomor', 'Tahun', 'Pasal'):
                out.add(w0)
    for nm in re.findall(r'([A-Z][A-Za-z\-]+)(?: et al\.| dan [A-Z][A-Za-z\-]+)? \(\d{4}', t):
        if nm not in ('Nomor', 'Tahun', 'Pasal'):
            out.add(nm)
    return out

def words(t):
    return re.findall(r'[0-9a-zà-ÿ]+', t.lower())

def split_sents(text):
    t = re.sub(r'\b(et al|t\.t|No|hlm|Vol|Dr|Prof|mis|dkk|UU|PP|Perpres|SE|vs|ca)\.', r'\1<DOT>', text, flags=re.I)
    t = re.sub(r'\b([A-Za-z])\.', r'\1<DOT>', t)
    t = re.sub(r'(\d)\.(\d)', r'\1<DOT>\2', t)
    sents = [s.replace('<DOT>', '.').strip() for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) >= 2]
    return sents

BANNED_AI = [
    r'\bmenegaskan bahwa\b', r'\bmembuktikan bahwa\b', r'\bmenggarisbawahi bahwa\b',
    r'\bkendati demikian\b', r'\bnamun demikian\b', r'\bberbanding terbalik dengan\b',
    r'\bsebagai respons evolusioner\b', r'\bmencermati kompleksitas\b',
    r'\bbukan semata-mata\b', r'\btidak dapat dipungkiri\b', r'\bperlu dicatat\b',
    r'\bkrusial\b', r'\bholistik\b', r'\btransformatif\b', r'\brevolusioner\b',
    r'\bgarda terdepan\b', r'\bmenyelami\b'
]

err = 0
tot = hit = 0
all_new_words = 0
secara_cnt = merupakan_cnt = mekan_cnt = 0

for a, b in zip(o, n):
    A, B = a['text'], b['text']
    probs = []
    m = re.match(r'^(\d+\.|[a-z]\.|•)\s', A)
    if m and not B.startswith(m.group(1)):
        probs.append('lost label ' + m.group(1))
    miss = nums(A) - nums(B)
    if miss: probs.append('numbers missing ' + str(sorted(miss)))
    mc = {c for c in cites(A) if c not in B}
    if mc: probs.append('citation names missing ' + str(sorted(mc)))
    if B.count('*') % 2: probs.append('unbalanced *')
    r = len(B.split()) / max(1, len(A.split()))
    if r < 0.72 or r > 1.32: probs.append(f'length ratio {r:.2f}')

    wa, wb = words(A), words(B)
    g = {tuple(wa[i:i+6]) for i in range(len(wa)-5)}
    cov = [False]*len(wb)
    for i in range(len(wb)-5):
        if tuple(wb[i:i+6]) in g:
            for j in range(i, i+6): cov[j] = True
    k = sum(cov); tot += len(wb); hit += k
    pct = 100*k/max(1, len(wb))
    if pct > 20 and len(wb) > 15:
        probs.append(f'6-gram overlap {pct:.0f}%')

    # DrillBit AI burstiness check on prose paragraphs (P15) with >= 3 sentences
    if b['style'] == 'P15' and len(wb) >= 60:
        sents = split_sents(B)
        if len(sents) >= 3:
            lens = [len(s.split()) for s in sents]
            mn = min(lens)
            cv = statistics.stdev(lens) / max(1, statistics.mean(lens))
            if mn > 15 and cv < 0.36:
                probs.append(f'low burstiness (min_sent={mn}w, CV={cv:.2f}, lens={lens})')

    for pat in BANNED_AI:
        if re.search(pat, B.lower()):
            probs.append(f'banned AI tell: {pat}')

    w_alpha = re.findall(r'[a-zà-ÿ]+', B.lower())
    all_new_words += len(w_alpha)
    secara_cnt += sum(1 for w in w_alpha if w == 'secara')
    merupakan_cnt += sum(1 for w in w_alpha if w == 'merupakan')
    mekan_cnt += sum(1 for w in w_alpha if re.match(r'^me[a-z]{4,}(kan|i)$', w))

    if probs:
        err += 1
        print(f"id={a['id']}: " + '; '.join(probs))

print(f'segments with issues: {err}/{len(o)}; overall 6-gram overlap {100*hit/max(1,tot):.1f}%')
print(f'DrillBit AI style rates (/1k words): secara={secara_cnt*1000/max(1,all_new_words):.1f} (target <6.0), merupakan={merupakan_cnt*1000/max(1,all_new_words):.1f} (target <1.0), me-kan={mekan_cnt*1000/max(1,all_new_words):.1f} (target <30.0)')
