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
"""
ut_audit.py — Self-contained Indonesian & English Academic Prose, Anti-Slop,
PUEBI Italic, Character-Budget, and APA Citation Auditor for Universitas Terbuka (UT).

Works both on local CLI environments and inside web LLM Python sandboxes
(zero third-party dependencies; uses only Python standard library).

Usage:
    python3 ut_audit.py <file.md|file.odt|file.docx|file.txt> [--max-chars 1400]
"""
from __future__ import annotations

import argparse
import re
import statistics
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

# 1. Banned AI Slop & Throat-Clearing Patterns (Indonesian & English)
AI_SLOP_PATTERNS = [
    (r"\bdi era digital\b", "Pembuka klise 'di era digital' — langsung masuk ke subjek teknis/kasus."),
    (r"\bdalam era globalisasi\b", "Pembuka klise 'dalam era globalisasi' — hapus dan mulai dari klaim inti."),
    (r"\brevolusi industri 4\.0\b", "Klise 'Revolusi Industri 4.0' — hindari kecuali menjadi variabel resmi soal."),
    (r"\bseiring (dengan )?perkembangan\b", "Pembuka klise 'seiring (dengan) perkembangan' — sebutkan langsung perubahan spesifiknya."),
    (r"\btidak dapat dipungkiri\b", "Frasa klise 'tidak dapat dipungkiri' — langsung nyatakan fakta atau datanya."),
    (r"\bperlu dicatat bahwa\b", "Throat-clearing 'perlu dicatat bahwa' — langsung tulis kalimat intinya."),
    (r"\bpenting untuk diingat\b", "Throat-clearing 'penting untuk diingat' — hapus pengantar kosong."),
    (r"\bdalam lanskap\b", "Metafora AI 'dalam lanskap' — ganti dengan istilah bidang yang konkret."),
    (r"\bbukan hanya\b[^.?!]{3,80}\bmelainkan juga\b", "Kontras biner mekanis 'bukan hanya X, melainkan juga Y' — nyatakan langsung kedua fungsinya."),
    (r"\btidak sekadar\b[^.?!]{3,80}\btetapi juga\b", "Kontras biner mekanis 'tidak sekadar X, tetapi juga Y' — tulis lugas tanpa retorika biner."),
    (r"\bdengan demikian, dapat disimpulkan bahwa\b", "Penutup repetitif 'Dengan demikian, dapat disimpulkan bahwa' — akhiri paragraf pada implikasi teknis."),
    (r"\bsecara keseluruhan, dapat disimpulkan\b", "Penutup repetitif — hapus kesimpulan satu kalimat yang mengulang isi paragraf."),
    (r"\b(krusial|holistik|transformatif|revolusioner|peran sentral|garda terdepan|menyelami)\b", "Kata sifat promosi/AI slop — ganti dengan ukuran atau mekanisme teknis yang terukur."),
    (r"\bmemanfaatkan secara optimal\b", "Terjemahan AI dari 'leverage optimally' — sebutkan cara pemanfaatannya secara spesifik."),
    (r"\b(delve|delves|delving|leverage|leverages|leveraging|showcase|showcases|underscore|underscores|pivotal|multifaceted|groundbreaking|ever-evolving)\b", "English LLM-tell lexical marker — ganti dengan kata kerja akademik lugas."),
]

# 2. Chatbot Meta-Artifacts & Leftover Placeholders
META_PATTERNS = [
    (r"^(tentu|baik),?\s+(berikut|ini)\s+adalah", "Teks meta chatbot di awal dokumen."),
    (r"\bsemoga membantu\b", "Teks penutup chatbot."),
    (r"\[(isi|insert|masukkan|tambahkan|link|todo)[^\]]*\]", "Placeholder belum diisi."),
]

# 3. Common Foreign Technical Terms that Must Be Italicized in Indonesian Prose (PUEBI)
FOREIGN_TERMS_CHECK = [
    "open standard", "self-hosted", "walled garden", "single point of failure",
    "switching costs", "throughput", "trunking", "ransomware", "phishing",
    "defense in depth", "cloud computing", "client/server", "mainframe",
    "freeware", "shareware", "copyleft", "unauthorized access", "cybercrime",
    "cyber espionage", "carding", "cyberstalking", "data forgery",
    "illegal contents", "probing", "port scanning", "gap research",
    "research gap", "awareness", "surveillance capitalism", "enshittification",
]


def extract_text_from_file(path: Path) -> tuple[str, list[str]]:
    """Return plain/markdown text and a list of format-specific warnings."""
    warnings: list[str] = []
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8", errors="replace"), warnings

    if suffix == ".odt":
        with zipfile.ZipFile(path) as z:
            xml_bytes = z.read("content.xml")
        root = ET.fromstring(xml_bytes)
        ns = {
            "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
            "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
            "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
        }
        italic_styles = set()
        for xml_name in ("content.xml", "styles.xml"):
            if xml_name in z.namelist():
                sroot = ET.fromstring(z.read(xml_name))
                for st in sroot.findall(".//style:style", ns):
                    name = st.attrib.get(f"{{{ns['style']}}}name", "")
                    tp = st.find("style:text-properties", ns)
                    if tp is not None and tp.attrib.get(f"{{{ns['fo']}}}font-style") == "italic":
                        italic_styles.add(name)

        paragraphs: list[str] = []
        for elem in root.iter():
            tag = elem.tag.split("}")[-1]
            if tag in {"p", "h"}:
                p_style = elem.attrib.get(f"{{{ns['text']}}}style-name", "")
                p_is_italic = p_style in italic_styles or "Italic" in p_style
                parts: list[str] = []
                if elem.text:
                    parts.append(f"*{elem.text}*" if p_is_italic else elem.text)
                for child in elem:
                    ctag = child.tag.split("}")[-1]
                    st_name = child.attrib.get(f"{{{ns['text']}}}style-name", "")
                    ctext = "".join(child.itertext())
                    if p_is_italic or (ctag == "span" and (st_name in italic_styles or "Italic" in st_name)):
                        parts.append(f"*{ctext}*")
                    else:
                        parts.append(ctext)
                    if child.tail:
                        parts.append(f"*{child.tail}*" if p_is_italic else child.tail)
                line = "".join(parts).strip()
                if line:
                    paragraphs.append(line)

        toc_headings = [p for p in paragraphs if p.upper() == "DAFTAR ISI"]
        if len(toc_headings) > 1:
            warnings.append(
                f"[LAYOUT/TOC] Judul 'DAFTAR ISI' muncul {len(toc_headings)} kali di dalam ODT (risiko tercetak ganda)."
            )
        return "\n\n".join(paragraphs), warnings

    if suffix == ".docx":
        with zipfile.ZipFile(path) as z:
            xml_bytes = z.read("word/document.xml")
        root = ET.fromstring(xml_bytes)
        paragraphs = []
        for p in root.iter():
            if p.tag.endswith("}p"):
                txt = "".join(p.itertext()).strip()
                if txt:
                    paragraphs.append(txt)
        return "\n\n".join(paragraphs), warnings

    return path.read_text(encoding="utf-8", errors="replace"), warnings


def split_body_and_references(text: str) -> tuple[str, str]:
    pattern = re.compile(
        r"^#{1,3}\s*(daftar pustaka|sumber|referensi|references)\b.*$",
        re.IGNORECASE | re.MULTILINE,
    )
    m = pattern.search(text)
    if not m:
        # Also check plain heading in ODT
        m2 = re.search(r"\n(DAFTAR PUSTAKA|Daftar Pustaka|Sumber|Referensi)\s*\n", text)
        if m2:
            return text[: m2.start()], text[m2.end() :]
        return text, ""
    return text[: m.start()], text[m.end() :]


def check_citations(body: str, refs: str) -> list[str]:
    findings: list[str] = []
    if not refs.strip():
        findings.append("[SITASI] Bagian 'Daftar Pustaka' atau 'Sumber' tidak ditemukan.")
        return findings

    # Extract in-text (Author, YYYY) or Author (YYYY)
    in_text_years: list[tuple[str, str]] = []
    # Pattern 1: inside parentheses e.g. (Laudon & Laudon, 2020; Sukoco, 2021)
    for paren in re.findall(r"\(([^()]{4,180})\)", body):
        for chunk in paren.split(";"):
            m = re.search(r"([A-Z][A-Za-z'’\-]+(?:\s+(?:&|dan|et al\.|dkk\.)\s+[A-Z][A-Za-z'’\-]+)?).*?\b(19\d{2}|20\d{2}[a-z]?)\b", chunk)
            if m:
                surname = m.group(1).split()[0].strip(",.")
                year = m.group(2)
                in_text_years.append((surname, year))

    # Pattern 2: Narrative citation e.g. menurut Sutarman (2007)
    for m in re.finditer(r"\b([A-Z][A-Za-z'’\-]{2,})(?:\s+(?:dkk\.|et al\.|(?:&|dan)\s+[A-Z][A-Za-z'’\-]+))?\s*\((19\d{2}|20\d{2}[a-z]?)\)", body):
        surname = m.group(1).strip(",.")
        year = m.group(2)
        in_text_years.append((surname, year))

    ref_lines = [line.strip() for line in refs.splitlines() if len(line.strip()) > 15]
    ref_text_lower = refs.lower()

    missing_in_bib = set()
    for surname, year in in_text_years:
        if surname.lower() in {"tabel", "gambar", "modul", "bab", "langkah", "nomor", "pasal", "uu"}:
            continue
        if surname.lower() not in ref_text_lower or year.lower() not in ref_text_lower:
            missing_in_bib.add(f"{surname} ({year})")

    for item in sorted(missing_in_bib):
        findings.append(f"[SITASI] Kutipan in-text '{item}' belum memiliki padanan yang cocok di Daftar Pustaka/Sumber.")

    # Check if each bibliography entry is cited in body
    body_lower = body.lower()
    for rline in ref_lines:
        clean = re.sub(r"^[\-\*\d\.\s]+", "", rline)
        m = re.match(r"([A-Za-z'’\-]+)", clean)
        ym = re.search(r"\((19\d{2}|20\d{2}[a-z]?)\)", clean)
        if m and ym:
            first_word = m.group(1).lower()
            year = ym.group(1).lower()
            if first_word not in body_lower and year not in body_lower:
                findings.append(f"[SITASI] Entri Daftar Pustaka '{clean[:55]}...' tidak ditemukan kutipannya di badan teks.")

    return findings


def audit_document(path: Path, max_chars_per_item: int = 0) -> int:
    text, warnings = extract_text_from_file(path)
    body, refs = split_body_and_references(text)
    lines = text.splitlines()

    print(f"=== UT ACADEMIC & ANTI-SLOP AUDIT: {path.name} ===")
    issue_count = 0

    for w in warnings:
        print(w)
        issue_count += 1

    # 1. Check AI Slop & Meta patterns line by line
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            continue
        for pat, msg in AI_SLOP_PATTERNS + META_PATTERNS:
            for m in re.finditer(pat, line, flags=re.IGNORECASE):
                print(f"[SLOP/META Baris {idx}] '{m.group(0)}' -> {msg}")
                issue_count += 1

        # Em-dash density
        em_dashes = line.count("—")
        if em_dashes >= 2:
            print(f"[GAYA Baris {idx}] {em_dashes} em-dash (—) dalam satu paragraf/baris — ganti dengan koma, titik, atau kurung.")
            issue_count += 1

        # Mid-sentence bold in prose (excluding headings, tables, list labels)
        stripped = line.strip()
        if (
            stripped
            and not stripped.startswith(("#", "|", "-", "*"))
            and not re.match(r"^\d+\.\s*\*\*", stripped)
        ):
            bolds = re.findall(r"\*\*([^*]+)\*\*", stripped)
            if len(bolds) >= 2:
                print(f"[FORMAT Baris {idx}] Ditemukan {len(bolds)} frasa huruf tebal (**bold**) di tengah kalimat prosa.")
                issue_count += 1

    # 2. Check Foreign Terms Italicization (PUEBI) in body
    for idx, line in enumerate(body.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "```", "|")):
            continue
        # Remove already italicized spans *...* or _..._ and inline code `...`
        unitalicized = re.sub(r"(\*[^*]+\*|_[^_]+_|`[^`]+`)", " ", stripped)
        for term in FOREIGN_TERMS_CHECK:
            if re.search(rf"\b{re.escape(term)}\b", unitalicized, flags=re.IGNORECASE):
                print(f"[PUEBI/ITALIC Baris {idx}] Istilah asing '{term}' belum dicetak miring (*{term}*).")
                issue_count += 1

    # 3. Check Burstiness (Sentence Length Variation) in long prose paragraphs
    paragraphs = [p.strip() for p in body.split("\n\n") if len(p.strip()) > 250 and not p.strip().startswith(("#", "|", "```", "-", "*"))]
    for p_idx, para in enumerate(paragraphs, 1):
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", para) if len(s.strip().split()) >= 4]
        if len(sents) >= 4:
            lengths = [len(s.split()) for s in sents]
            stdev = statistics.pstdev(lengths)
            if stdev < 3.0:
                print(
                    f"[BURSTINESS Paragraf {p_idx}] Panjang kalimat terlalu seragam (SD={stdev:.1f} kata, panjang={lengths}). Variasikan kalimat pendek (8-12 kata) dan kalimat analitis (20-30 kata)."
                )
                issue_count += 1

    # 4. Optional Character Budget per Numbered Answer (e.g., max 1400 chars)
    if max_chars_per_item > 0:
        numbered_items = re.findall(r"(?:^|\n)(\d+\.\s+.*?)(?=\n\d+\.\s+|\n---|\n##|\Z)", body, flags=re.DOTALL)
        for item in numbered_items:
            char_len = len(item.strip())
            num_label = item.strip().split()[0]
            status = "MELEBIHI BATAS" if char_len > max_chars_per_item else "OK"
            print(f"[KARAKTER Soal {num_label}] {char_len}/{max_chars_per_item} karakter ({status})")
            if char_len > max_chars_per_item:
                issue_count += 1

    # 5. Check Citations
    cit_findings = check_citations(body, refs)
    for cf in cit_findings:
        print(cf)
        issue_count += 1

    if issue_count == 0:
        print("LULUS AUDIT: 0 temuan AI slop, PUEBI italic, maupun ketidaksesuaian sitasi.")
    else:
        print(f"TOTAL TEMUAN PERLU DITINJAU: {issue_count}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit draf tugas/proposal UT (Anti-Slop, PUEBI Italic, Burstiness, Sitasi APA).")
    parser.add_argument("file", type=Path, help="Berkas .md, .odt, .docx, atau .txt")
    parser.add_argument("--max-chars", type=int, default=0, help="Batas karakter per nomor soal (mis. 1400)")
    args = parser.parse_args()
    if not args.file.exists():
        print(f"Error: Berkas tidak ditemukan: {args.file}", file=sys.stderr)
        return 1
    return audit_document(args.file, args.max_chars)


if __name__ == "__main__":
    raise SystemExit(main())
