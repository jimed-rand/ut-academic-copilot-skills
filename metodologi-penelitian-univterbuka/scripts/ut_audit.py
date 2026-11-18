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
DrillBit AI-Detection (<30%) & Similarity (<30%), PUEBI Italic, Character-Budget,
and APA Citation Auditor for Universitas Terbuka (UT).

Works both on local CLI environments and inside web LLM Python sandboxes
(zero third-party dependencies; uses only Python standard library).

Usage:
    python3 ut_audit.py <file.md|file.odt|file.docx|file.txt> [--max-chars 1400] [--ref old1.odt old2.odt]
"""
from __future__ import annotations

import argparse
import re
import statistics
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

# 1. Banned AI Slop, Throat-Clearing & DrillBit-Flagged Phrasal Tells (Indonesian & English)
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
    (r"\bbukan semata-mata\b", "Kontras biner AI 'bukan semata-mata' — tulis klaim secara langsung tanpa pola biner."),
    (r"\bdengan demikian, dapat disimpulkan bahwa\b", "Penutup repetitif 'Dengan demikian, dapat disimpulkan bahwa' — akhiri paragraf pada implikasi teknis."),
    (r"\bsecara keseluruhan, dapat disimpulkan\b", "Penutup repetitif — hapus kesimpulan satu kalimat yang mengulang isi paragraf."),
    (r"\b(krusial|holistik|transformatif|revolusioner|peran sentral|garda terdepan|menyelami)\b", "Kata sifat promosi/AI slop — ganti dengan ukuran atau mekanisme teknis yang terukur."),
    (r"\bmemanfaatkan secara optimal\b", "Terjemahan AI dari 'leverage optimally' — sebutkan cara pemanfaatannya secara spesifik."),
    (r"\b(menegaskan bahwa|membuktikan bahwa|menggarisbawahi bahwa)\b", "Verba retoris pemicu DrillBit AI ('menegaskan/membuktikan/menggarisbawahi bahwa') — gunakan verba laporan netral (menunjukkan, mencatat, melaporkan) atau klausa pasif."),
    (r"\b(kendati demikian|namun demikian|berbanding terbalik dengan|sebagai respons evolusioner|mencermati kompleksitas)\b", "Frasa transisi pemicu DrillBit AI — gunakan transisi ringkas ('Namun,', 'Sebaliknya,', atau langsung masuk klaim)."),
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


def split_sents(text: str) -> list[str]:
    """Split text into sentences while protecting Indonesian/academic abbreviations."""
    t = re.sub(
        r"\b(et al|t\.t|No|hlm|Vol|Dr|Prof|mis|dkk|UU|PP|Perpres|SE|vs|ca)\.",
        r"\1<DOT>",
        text,
        flags=re.IGNORECASE,
    )
    t = re.sub(r"\b([A-Za-z])\.", r"\1<DOT>", t)
    t = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)
    return [
        s.replace("<DOT>", ".").strip()
        for s in re.split(r"(?<=[.!?])\s+", t)
        if len(s.split()) >= 2
    ]


def extract_text_from_file(path: Path) -> tuple[str, list[str]]:
    """Return plain/markdown text and a list of format-specific warnings."""
    warnings: list[str] = []
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8", errors="replace"), warnings

    if suffix == ".pdf":
        res = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
        return res.stdout, warnings

    if suffix == ".odt":
        ns = {
            "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
            "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
            "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
        }
        italic_styles: set[str] = set()
        with zipfile.ZipFile(path) as z:
            xml_bytes = z.read("content.xml")
            for xml_name in ("content.xml", "styles.xml"):
                if xml_name in z.namelist():
                    sroot = ET.fromstring(z.read(xml_name))
                    for st in sroot.findall(".//style:style", ns):
                        name = st.attrib.get(f"{{{ns['style']}}}name", "")
                        tp = st.find("style:text-properties", ns)
                        if tp is not None and tp.attrib.get(f"{{{ns['fo']}}}font-style") == "italic":
                            italic_styles.add(name)
        root = ET.fromstring(xml_bytes)

        paragraphs: list[str] = []
        for elem in root.iter():
            tag = elem.tag.split("}")[-1]
            if tag in {"p", "h"}:
                # Skip nested text:p if any
                p_style = elem.attrib.get(f"{{{ns['text']}}}style-name", "")
                p_is_italic = p_style in italic_styles or "Italic" in p_style
                parts: list[str] = []
                if elem.text:
                    parts.append(f"*{elem.text}*" if p_is_italic else elem.text)
                for child in elem:
                    ctag = child.tag.split("}")[-1]
                    if ctag == "p":
                        continue
                    st_name = child.attrib.get(f"{{{ns['text']}}}style-name", "")
                    ctext = "".join(child.itertext())
                    if p_is_italic or (ctag == "span" and (st_name in italic_styles or "Italic" in st_name)):
                        parts.append(f"*{ctext}*")
                    else:
                        parts.append(ctext)
                    if child.tail:
                        parts.append(f"*{child.tail}*" if p_is_italic else child.tail)
                line = "".join(parts).replace("**", "").strip()
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
        matches = list(re.finditer(r"\n(DAFTAR PUSTAKA|Daftar Pustaka|Sumber|Referensi)\s*\n", text))
        if matches:
            m2 = matches[-1]
            return text[: m2.start()], text[m2.end() :]
        return text, ""
    return text[: m.start()], text[m.end() :]


def check_citations(body: str, refs: str) -> list[str]:
    findings: list[str] = []
    if not refs.strip():
        findings.append("[SITASI] Bagian 'Daftar Pustaka' atau 'Sumber' tidak ditemukan.")
        return findings

    # Trim trailing AI Disclaimer from refs if present
    m_disc = re.search(r"\n(PERNYATAAN INTEGRITAS|AI DISCLAIMER)\b", refs)
    refs_only = refs[: m_disc.start()] if m_disc else refs

    in_text_years: list[tuple[str, str]] = []
    for paren in re.findall(r"\(([^()]{4,180})\)", body):
        for chunk in paren.split(";"):
            m = re.search(
                r"([A-Z][A-Za-z'’\-]+(?:\s+(?:&|dan|et al\.|dkk\.)\s+[A-Z][A-Za-z'’\-]+)?).*?\b(19\d{2}|20\d{2}[a-z]?|t\.t\.)\b",
                chunk,
            )
            if m:
                surname = m.group(1).split()[0].strip(",.")
                year = m.group(2)
                in_text_years.append((surname, year))

    for m in re.finditer(
        r"\b([A-Z][A-Za-z'’\-]{2,})(?:\s+(?:dkk\.|et al\.|(?:&|dan)\s+[A-Z][A-Za-z'’\-]+))?\s*\((19\d{2}|20\d{2}[a-z]?|t\.t\.)\)",
        body,
    ):
        surname = m.group(1).strip(",.")
        year = m.group(2)
        in_text_years.append((surname, year))

    ref_lines = [line.strip() for line in refs_only.splitlines() if len(line.strip()) > 25]
    ref_text_lower = refs_only.lower()

    ignore_words = {
        "tabel", "gambar", "modul", "bab", "langkah", "nomor", "pasal",
        "uu", "pp", "perpres", "se", "surat", "undang-undang", "peraturan",
    }
    missing_in_bib = set()
    for surname, year in in_text_years:
        if surname.lower() in ignore_words:
            continue
        if surname.lower() not in ref_text_lower or year.lower() not in ref_text_lower:
            missing_in_bib.add(f"{surname} ({year})")

    for item in sorted(missing_in_bib):
        findings.append(f"[SITASI] Kutipan in-text '{item}' belum memiliki padanan yang cocok di Daftar Pustaka/Sumber.")

    body_lower = body.lower()
    for rline in ref_lines:
        clean = re.sub(r"^[\-\*\d\.\s]+", "", rline)
        m = re.match(r"([A-Za-z'’\-]+)", clean)
        ym = re.search(r"\((19\d{2}|20\d{2}[a-z]?|t\.t\.)\)", clean)
        if m and ym:
            first_word = m.group(1).lower()
            year = ym.group(1).lower()
            if first_word not in body_lower and year not in body_lower:
                findings.append(f"[SITASI] Entri Daftar Pustaka '{clean[:55]}...' tidak ditemukan kutipannya di badan teks.")

    return findings


def check_drillbit_ai_profile(body: str) -> tuple[list[str], float]:
    """Calibrated against DrillBit AI Content Detection Report.
    Returns (findings, estimated_ai_pct).
    """
    findings: list[str] = []
    paras = [
        p.strip()
        for p in body.split("\n\n")
        if len(p.strip().split()) >= 15 and not p.strip().startswith(("#", "|", "```"))
    ]

    all_words = re.findall(r"[a-zà-ÿ]+", body.lower())
    W = max(1, len(all_words))
    secara_rate = sum(1 for w in all_words if w == "secara") * 1000 / W
    merupakan_rate = sum(1 for w in all_words if w == "merupakan") * 1000 / W
    mekan_rate = sum(1 for w in all_words if re.match(r"^me[a-z]{4,}(kan|i)$", w)) * 1000 / W

    if secara_rate > 6.5:
        findings.append(
            f"[DRILLBIT-AI DENSITY] Kepadatan adverbia 'secara' = {secara_rate:.1f}/1k kata (target < 6.0/1k; teks AI DrillBit = 11.4/1k). Pangkas 'secara <adjektiva>' yang tidak perlu."
        )
    if merupakan_rate > 1.1:
        findings.append(
            f"[DRILLBIT-AI DENSITY] Kepadatan kopula 'merupakan' = {merupakan_rate:.1f}/1k kata (target < 1.0/1k; teks AI DrillBit = 1.76/1k). Variasikan dengan 'adalah', 'ialah', 'menjadi', atau klausa langsung."
        )
    if mekan_rate > 32.0:
        findings.append(
            f"[DRILLBIT-AI DENSITY] Kepadatan verba aktif transitif 'me-...-kan/-i' = {mekan_rate:.1f}/1k kata (target < 30.0/1k; teks AI DrillBit = 44.5/1k). Ubah sebagian klausa SVO aktif ke bentuk pasif ('di-...-kan'/'ter-') atau pembuka preposisional."
        )

    # Check parallel list item opening cloning (Layout Regularity)
    prev_opener = ""
    prev_label = ""
    for p in paras:
        m = re.match(r"^(\d+\.|[a-z]\.|•)\s+(?:\*[^*]+\*\s*:\s*|[^:]{3,55}:\s*)([A-Za-z\-]+)", p)
        if m:
            label, opener = m.group(1), m.group(2).lower()
            if opener == prev_opener and len(opener) >= 4:
                findings.append(
                    f"[DRILLBIT-AI LAYOUT] Butir daftar '{prev_label}' dan '{label}' dibuka dengan kata identik setelah titik dua ('{opener}...'). Variasikan struktur pembuka butir daftar."
                )
            prev_opener, prev_label = opener, label
        else:
            prev_opener = ""

    # Score paragraphs & estimate DrillBit flagged block word percentage
    flagged_words = 0
    total_prose_words = sum(len(p.split()) for p in paras)
    for idx, p in enumerate(paras, 1):
        pw = p.split()
        wcnt = len(pw)
        sents = split_sents(p)
        p_alpha = re.findall(r"[a-zà-ÿ]+", p.lower())
        pW = max(1, len(p_alpha))
        p_secara = sum(1 for w in p_alpha if w == "secara") * 1000 / pW
        p_mekan = sum(1 for w in p_alpha if re.match(r"^me[a-z]{4,}(kan|i)$", w)) * 1000 / pW
        p_merupakan = sum(1 for w in p_alpha if w == "merupakan") * 1000 / pW

        low_burst = False
        if len(sents) >= 3 and wcnt >= 60:
            lens = [len(s.split()) for s in sents]
            mn = min(lens)
            cv = statistics.stdev(lens) / max(1.0, statistics.mean(lens))
            if mn > 15 and cv < 0.36:
                low_burst = True
                findings.append(
                    f"[DRILLBIT-AI BURSTINESS Paragraf #{idx}] Kalimat terlalu seragam tanpa kalimat pendek (min={mn} kata, CV={cv:.2f}, lens={lens}) pada: '{p[:75]}...'. Sisipkan minimal 1 kalimat pendek lugas (6-13 kata)."
                )

        # Heuristic block AI score combining burstiness and calqued SVO density
        risk_signals = (
            (1.5 if low_burst else 0.0)
            + (0.8 if p_secara > 9.0 else 0.0)
            + (0.8 if p_mekan > 38.0 else 0.0)
            + (0.5 if p_merupakan > 2.0 else 0.0)
        )
        if risk_signals >= 1.5:
            flagged_words += wcnt

    est_pct = 100.0 * flagged_words / max(1, total_prose_words)
    return findings, est_pct


def check_similarity(body: str, ref_paths: list[Path], n: int = 8) -> tuple[list[str], float]:
    """Calculate n-gram word overlap against reference documents (excluding bibliography)."""
    findings: list[str] = []
    cand_words = re.findall(r"[0-9a-zà-ÿ]+", body.lower())
    if len(cand_words) < n:
        return findings, 0.0

    all_cov = [False] * len(cand_words)
    for rp in ref_paths:
        if not rp.exists():
            continue
        rtext, _ = extract_text_from_file(rp)
        rbody, _ = split_body_and_references(rtext)
        rw = re.findall(r"[0-9a-zà-ÿ]+", rbody.lower())
        rgrams = {tuple(rw[i : i + n]) for i in range(len(rw) - n + 1)}
        cov = [False] * len(cand_words)
        for i in range(len(cand_words) - n + 1):
            if tuple(cand_words[i : i + n]) in rgrams:
                for j in range(i, i + n):
                    cov[j] = True
                    all_cov[j] = True
        pct = 100.0 * sum(cov) / len(cand_words)
        if pct >= 25.0:
            findings.append(
                f"[SIMILARITAS] Overlap {n}-gram terhadap '{rp.name}' = {pct:.1f}% (melebihi ambang aman 25% untuk target DrillBit < 30%)."
            )

    comb_pct = 100.0 * sum(all_cov) / len(cand_words)
    if comb_pct >= 30.0:
        findings.append(
            f"[SIMILARITAS GABUNGAN] Total overlap {n}-gram terhadap dokumen referensi = {comb_pct:.1f}% (WAJIB < 30%)."
        )
    return findings, comb_pct


def audit_document(path: Path, max_chars_per_item: int = 0, ref_paths: list[Path] | None = None) -> int:
    text, warnings = extract_text_from_file(path)
    body, refs = split_body_and_references(text)
    lines = text.splitlines()

    print(f"=== UT ACADEMIC, ANTI-SLOP & DRILLBIT (<30%) AUDIT: {path.name} ===")
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

        em_dashes = line.count("—")
        if em_dashes >= 2:
            print(f"[GAYA Baris {idx}] {em_dashes} em-dash (—) dalam satu paragraf/baris — ganti dengan koma, titik, atau kurung.")
            issue_count += 1

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
        unitalicized = re.sub(r"(\*[^*]+\*|_[^_]+_|`[^`]+`)", " ", stripped)
        for term in FOREIGN_TERMS_CHECK:
            if re.search(rf"\b{re.escape(term)}\b", unitalicized, flags=re.IGNORECASE):
                print(f"[PUEBI/ITALIC Baris {idx}] Istilah asing '{term}' belum dicetak miring (*{term}*).")
                issue_count += 1

    # 3. DrillBit AI Profile & Burstiness Audit
    db_findings, est_ai_pct = check_drillbit_ai_profile(body)
    for df in db_findings:
        print(df)
        issue_count += 1
    status_ai = "LULUS (<30%)" if est_ai_pct < 30.0 else "GAGAL (>=30%)"
    print(f"[ESTIMASI SKOR DRILLBIT AI] {est_ai_pct:.1f}% ({status_ai}; target utama < 15.0%)")
    if est_ai_pct >= 30.0:
        issue_count += 1

    # 4. Optional Similarity Check against reference files (--ref)
    if ref_paths:
        sim_findings, comb_sim = check_similarity(body, ref_paths, n=8)
        for sf in sim_findings:
            print(sf)
            issue_count += 1
        status_sim = "LULUS (<30%)" if comb_sim < 30.0 else "GAGAL (>=30%)"
        print(f"[ESTIMASI SIMILARITAS 8-GRAM] {comb_sim:.1f}% ({status_sim}; target utama < 15.0%)")

    # 5. Optional Character Budget per Numbered Answer
    if max_chars_per_item > 0:
        numbered_items = re.findall(r"(?:^|\n)(\d+\.\s+.*?)(?=\n\d+\.\s+|\n---|\n##|\Z)", body, flags=re.DOTALL)
        for item in numbered_items:
            char_len = len(item.strip())
            num_label = item.strip().split()[0]
            status = "MELEBIHI BATAS" if char_len > max_chars_per_item else "OK"
            print(f"[KARAKTER Soal {num_label}] {char_len}/{max_chars_per_item} karakter ({status})")
            if char_len > max_chars_per_item:
                issue_count += 1

    # 6. Check Citations
    cit_findings = check_citations(body, refs)
    for cf in cit_findings:
        print(cf)
        issue_count += 1

    if issue_count == 0:
        print("LULUS AUDIT: 0 temuan AI slop, DrillBit AI/Similaritas < 30%, PUEBI italic, dan sitasi valid.")
    else:
        print(f"TOTAL TEMUAN PERLU DITINJAU: {issue_count}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit draf tugas/proposal UT (Anti-Slop, DrillBit <30%, PUEBI Italic, Burstiness, Sitasi APA).")
    parser.add_argument("file", type=Path, help="Berkas .md, .odt, .docx, .pdf, atau .txt")
    parser.add_argument("--max-chars", type=int, default=0, help="Batas karakter per nomor soal (mis. 1400)")
    parser.add_argument("--ref", type=Path, nargs="*", default=[], help="Berkas pembanding untuk cek similaritas/self-plagiarism (mis. Tugas1..3)")
    args = parser.parse_args()
    if not args.file.exists():
        print(f"Error: Berkas tidak ditemukan: {args.file}", file=sys.stderr)
        return 1
    return audit_document(args.file, args.max_chars, args.ref)


if __name__ == "__main__":
    raise SystemExit(main())
