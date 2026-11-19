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
"""Extract / reinject body paragraphs of an ODT for paraphrasing.

extract <content.xml> <out.json> [styles...]   -> list of {id, style, lead, text}
inject  <content.xml> <in.json> <out_content.xml>
Italic spans (style with fo:font-style="italic") <-> *...* markup.
"""
import json, re, sys, html

PAT = r'<text:p text:style-name="(%s)"([^>/]*)>((?:(?!<text:p[ >]).)*?)</text:p>'


def italic_styles(x):
    auto = x[x.find('<office:automatic-styles>'):x.find('</office:automatic-styles>')]
    return {m.group(1) for m in re.finditer(
        r'<style:style style:name="([^"]+)" style:family="text"[^>]*>(?:(?!</style:style>).)*fo:font-style="italic"', auto, re.S)}


def to_markup(inner, ital):
    lead = ''
    inner = inner.replace('<text:soft-page-break/>', '')
    m = re.match(r'(<text:s text:c="\d+"/>)', inner)
    if m:
        lead = m.group(1); inner = inner[len(lead):]
    def span(m):
        t = m.group(2)
        return '*' + t + '*' if m.group(1) in ital else t
    inner = re.sub(r'<text:span text:style-name="([^"]+)">(.*?)</text:span>', span, inner, flags=re.S)
    inner = re.sub(r'<text:s text:c="(\d+)"/>', lambda m: ' ' * int(m.group(1)), inner)
    inner = inner.replace('<text:s/>', ' ')
    if '<' in inner:
        raise ValueError('unhandled tag: ' + inner[:200])
    inner = inner.replace('**', '')  # adjacent italic spans
    return lead, html.unescape(inner)


def from_markup(lead, text, ital_style):
    parts = re.split(r'(\*[^*]+\*)', text)
    out = []
    for p in parts:
        if p.startswith('*') and p.endswith('*') and len(p) > 2:
            out.append('<text:span text:style-name="%s">%s</text:span>' % (ital_style, html.escape(p[1:-1], quote=False)))
        else:
            out.append(html.escape(p, quote=False))
    return lead + ''.join(out)


def pack(src_odt, content_xml, out_odt):
    import zipfile
    new_content = open(content_xml, 'rb').read()
    with zipfile.ZipFile(src_odt, 'r') as zin:
        items = [
            (it, new_content if it.filename == 'content.xml' else zin.read(it.filename))
            for it in zin.infolist()
        ]
    with zipfile.ZipFile(out_odt, 'w') as zout:
        for it, data in items:
            if it.filename == 'mimetype' or it.filename.endswith('/'):
                comp = zipfile.ZIP_STORED
            else:
                comp = it.compress_type
            zout.writestr(it, data, compress_type=comp)


def main():
    cmd = sys.argv[1]
    if cmd == 'pack':
        return pack(sys.argv[2], sys.argv[3], sys.argv[4])
    x = open(sys.argv[2], encoding='utf-8').read()
    ital = italic_styles(x)
    start = x.find('<office:text')
    if cmd == 'extract':
        styles = sys.argv[4:] or ['P15', 'P21', 'P24']
        segs = []
        for i, m in enumerate(re.finditer(PAT % '|'.join(styles), x[start:], re.S)):
            if '<draw:' in m.group(3) or '<text:tab' in m.group(3):
                continue
            lead, t = to_markup(m.group(3), ital)
            if len(t.split()) < 6:
                continue
            segs.append({'id': i, 'style': m.group(1), 'lead': lead, 'text': t})
        json.dump(segs, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(len(segs), 'segments,', sum(len(s['text'].split()) for s in segs), 'words')
    elif cmd == 'inject':
        segs = {s['id']: s for s in json.load(open(sys.argv[3], encoding='utf-8'))}
        ist = sorted(ital)[0]
        styles = sorted({s['style'] for s in segs.values()})
        cnt = [0, 0]
        def rep(m):
            i = cnt[0]; cnt[0] += 1
            s = segs.get(i)
            if not s:
                return m.group(0)
            cnt[1] += 1
            return '<text:p text:style-name="%s"%s>%s</text:p>' % (m.group(1), m.group(2), from_markup(s['lead'], s['text'], ist))
        body = re.sub(PAT % '|'.join(styles), rep, x[start:], flags=re.S)
        open(sys.argv[4], 'w', encoding='utf-8').write(x[:start] + body)
        print('replaced', cnt[1], 'of', len(segs))

if __name__ == '__main__':
    main()
