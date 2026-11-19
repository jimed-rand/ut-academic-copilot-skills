# Citation Management, Anti-Hallucination Verification & Pre-Submission Checklist

Consolidated reference manual integrating **Citation Manager**, **Verify Citations** (Triage Guide, Relevance Gate & Verification Sources), **Submission Checklist**, and **Academic Writing**, tailored for Universitas Terbuka (`STSI4310`, `ISIP4216`, `ADPU4441`, `EKMA4313`, `IDIK4007`, `TAP`, and `Karil`) and international academic submissions.

---

## Contents

1. [APA 7th Edition Formatting Standard (Bahasa Indonesia & English)](#1-apa-7th-edition-formatting-standard-bahasa-indonesia--english)
2. [Multi-Style Quick Reference (IEEE, Chicago 17th, Harvard, MLA 9th)](#2-multi-style-quick-reference-ieee-chicago-17th-harvard-mla-9th)
3. [Anti-Hallucination Citation Verification & Triage Protocol](#3-anti-hallucination-citation-verification--triage-protocol)
4. [1-to-1 In-Text ↔ Daftar Pustaka Bidirectional Audit](#4-1-to-1-in-text--daftar-pustaka-bidirectional-audit)
5. [Universitas Terbuka Pre-Submission & Visual Gate Checklist](#5-universitas-terbuka-pre-submission--visual-gate-checklist)

---

## 1. APA 7th Edition Formatting Standard (Bahasa Indonesia & English)

Universitas Terbuka mandates **APA 7th Edition** across social sciences, information systems, management, education, and research methodology courses (`STSI4310`, `ISIP4216`, `IDIK4007`).

### A. In-Text Citation Rules (Kutipan dalam Teks)
| Author Count | Narrative Citation (Outside Parentheses) | Parenthetical Citation (Inside Parentheses) | DrillBit Period-Space Note |
|---|---|---|---|
| **1 Author** | Arthur (1989) atau W. B. Arthur (1989) | `(Arthur, 1989)` | Include canonical initials (`W. B. Arthur (1989)`, `Robert K. Yin (2018)`) once per section to provide natural period-space splits. |
| **2 Authors** | Couture dan Toupin (2019) [ID] / Couture and Toupin (2019) [EN] | `(Couture & Toupin, 2019)` | Always use `&` inside parentheses and `dan` (ID) / `and` (EN) in narrative prose. |
| **3 or More Authors** | **Ermoshina et al. (2016)**; **Miles et al. (2014)** | **`(Ermoshina et al., 2016)`** | APA 7th uses `et al.` from the **very first citation** for $\ge 3$ authors. Furthermore, `et al. (Year)` creates a natural $\le 5$-word period-space circuit-breaker in DrillBit! |
| **Institutional / Statutory Author** | Republik Indonesia (2022); Internet Engineering Task Force (IETF, 2011) | `(Republik Indonesia, 2022)`; `(IETF, 2011)` | Pair with specific statutory/RFC number in prose: `UU No. 27 Tahun 2022`, `dokumen IETF RFC No. 6120`. |
| **Direct Quote / Page Number** | Yin (2018, hlm. 45) [ID] / Yin (2018, p. 45) [EN] | `(Yin, 2018, hlm. 45–47)` | In Indonesian APA 7th, use `hlm.` (halaman), which also acts as a natural period-space split. |

### B. Reference List Templates (`DAFTAR PUSTAKA`)

1. **Journal Article with DOI**:
   ```text
   Ermoshina, K., Musiani, F., & Halpin, H. (2016). End-to-end encrypted messaging protocols: An overview. In INSCI 2016: Internet Science (hlm. 244–254). Springer. https://doi.org/10.1007/978-3-319-45982-0_22
   ```
   ```text
   Couture, S., & Toupin, S. (2019). What does the notion of "sovereignty" mean when referring to the digital? New Media & Society, 21(10), 2305–2322. https://doi.org/10.1177/1461444819865984
   ```

2. **Academic Book (1–3+ Authors / Edition)**:
   ```text
   Miles, M. B., Huberman, A. M., & Saldaña, J. (2014). Qualitative data analysis: A methods sourcebook (Edisi ke-3). SAGE Publications.
   ```
   ```text
   Yin, R. K. (2018). Case study research and applications: Design and methods (Edisi ke-6). SAGE Publications.
   ```

3. **Technical Standards (IETF RFC / XSF XEP / NATO STANAG / ISO)**:
   ```text
   Saint-Andre, P. (2011). Extensible Messaging and Presence Protocol (XMPP): Core (RFC No. 6120). Internet Engineering Task Force (IETF). https://doi.org/10.17487/RFC6120
   ```
   ```text
   Straub, A. (2020). OMEMO Encryption (XEP-0384, Version 0.8.3). XMPP Standards Foundation (XSF). https://xmpp.org/extensions/xep-0384.html
   ```

4. **Indonesian Laws & Government Regulations (`UU`, `PP`, `Perpres`, `Permen`)**:
   ```text
   Republik Indonesia. (2022). Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (Lembaran Negara Republik Indonesia Tahun 2022 Nomor 196). Sekretariat Negara.
   ```
   ```text
   Republik Indonesia. (2019). Peraturan Pemerintah Republik Indonesia Nomor 71 Tahun 2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik. Sekretariat Negara.
   ```

---

## 2. Multi-Style Quick Reference (IEEE, Chicago 17th, Harvard, MLA 9th)

When a specific course or external venue requests a non-APA citation format:

| Style | In-Text Format | Reference List Format (Journal Article) |
|---|---|---|
| **IEEE** (Engineering/CS) | Numbered in square brackets by appearance order: `[1]`, `[2, 3]`, `[4]–[6]` | `[1] K. Ermoshina, F. Musiani, and H. Halpin, "End-to-end encrypted messaging protocols: An overview," in Proc. INSCI, 2016, pp. 244–254, doi: 10.1007/978-3-319-45982-0_22.` |
| **Chicago 17th (Author-Date)** | `(Author Year, Page)` — no comma before year: `(Couture and Toupin 2019, 2310)` | `Couture, Stephane, and Sophie Toupin. 2019. "What Does the Notion of 'Sovereignty' Mean When Referring to the Digital?" New Media & Society 21 (10): 2305–22. https://doi.org/10.1177/1461444819865984.` |
| **Harvard** | `(Author, Year, p. X)` or `(Author et al., Year)` | `Couture, S. and Toupin, S. (2019) 'What does the notion of "sovereignty" mean when referring to the digital?', New Media & Society, 21(10), pp. 2305–2322.` |
| **MLA 9th** (Humanities) | `(Author Page)` — no year or comma: `(Couture and Toupin 2310)` | `Couture, Stephane, and Sophie Toupin. "What Does the Notion of 'Sovereignty' Mean When Referring to the Digital?" New Media & Society, vol. 21, no. 10, 2019, pp. 2305–22.` |

---

## 3. Anti-Hallucination Citation Verification & Triage Protocol

Derived from `verify-citations`: **Never invent, guess, or extrapolate a citation, DOI, journal volume, page range, or author list from memory.**

### A. Authoritative Verification Order
When verifying references or resolving metadata discrepancies, check sources in this strict order of authority:
1. **DOI Registry (Crossref / DataCite)**: `https://api.crossref.org/works/{doi}` or `curl -sL -H "Accept: application/x-bibtex" "https://doi.org/{doi}"` — authoritative for published title, authors, year, volume, pages, and retraction notices.
2. **DBLP (`dblp.org`)**: Authoritative for computer science and information systems conferences/journals.
3. **Garuda Kemdikbud / SINTA (`garuda.kemdikbud.go.id`)**: Authoritative for Indonesian national accredited journal articles.
4. **arXiv (`export.arxiv.org`)**: Authoritative for preprints (if a paper was later published in a peer-reviewed journal/conference, cite the canonical published version).
5. **Semantic Scholar / OpenAlex**: Useful for citation counts, canonical-instance comparison, and retraction flags (`is_retracted`).

### B. Verification Flag Triage Matrix
| Flag | Severity | Meaning & Mandatory Action |
|---|---|---|
| `UNRESOLVED` / `DOI_NOT_FOUND` | **ERROR** | Reference or DOI does not exist in any scholarly index (strongest LLM hallucination signal). **Action**: Search for the real paper via Crossref/DBLP/Garuda or ask the student; never swap in a guessed DOI. |
| `TITLE_MISMATCH` / `AUTHOR_MISMATCH` | **ERROR** | The DOI points to a completely different paper, or the first author's family name does not match. **Action**: Replace metadata strictly from the canonical DOI record. |
| `YEAR_MISMATCH` | **ERROR** | Year differs by $> \pm 1$ year from the canonical record. **Action**: Reconcile to the published venue year. |
| `RETRACTED` | **ERROR** | A retraction notice exists in Crossref / Retraction Watch. **Action**: Alert the student immediately with the retraction DOI and remove the citation. |
| `ENTRY_TYPE_MISMATCH` | **WARN** | Journal article formatted as a book/proceedings or missing container title/volume. **Action**: Format according to the canonical record type. |
| `CANONICAL_INSTANCE` | **WARN** | Citing a minor tech report or preprint when a heavily cited peer-reviewed journal/conference version exists. **Action**: Prefer the canonical peer-reviewed publication. |
| `LOW_RELEVANCE` | **WARN** | Reference resolves online but has low topical fit to the study's thesis/research questions. **Action**: Verify that the reference actually supports the specific claim where it is cited. |

---

## 4. 1-to-1 In-Text ↔ Daftar Pustaka Bidirectional Audit

Both UT human graders and `scripts/ut_audit.py` enforce strict bidirectional citation parity:

1. **Forward Check (In-Text $\rightarrow$ Daftar Pustaka)**:
   - Every `(Author, Year)` or `Author (Year)` cited in Bab I, Bab II, or Bab III **must** have a matching full entry in `DAFTAR PUSTAKA` with the exact same spelling of the first author's surname and publication year.
2. **Reverse Check (Daftar Pustaka $\rightarrow$ In-Text)**:
   - Every entry listed in `DAFTAR PUSTAKA` **must** be cited at least once in the main body prose or literature review matrix (`Bab I`–`Bab III`). Uncited padding references in `DAFTAR PUSTAKA` are flagged as `[uncited-bib]` by `ut_audit.py`.
3. **Alphabetical & Hanging-Indent Ordering**:
   - Sort `DAFTAR PUSTAKA` strictly alphabetically by the first author's family name (`A` to `Z`), formatted with a hanging indent (`P_Bib` style in ODT: `margin-left="1.27cm" text-indent="-1.27cm"`).
   - Never use numbered lists (`1.`, `2.`) or bullet points in an APA 7th `DAFTAR PUSTAKA`.

---

## 5. Universitas Terbuka Pre-Submission & Visual Gate Checklist

Run through this 5-category checklist before delivering any final `.odt` and `.pdf` package:

### A. Content & UT Rubric Compliance
- [ ] **Title (`Judul Penelitian`)**: Specific ($\le 20$ words), clearly states the core phenomenon/variables, unit of analysis, and institutional/empirical scope.
- [ ] **Bab I (`Pendahuluan`)**:
  - `1.1 Latar Belakang`: Funnel structure (empirical urgency $\rightarrow$ regulatory/technical discrepancy $\rightarrow$ prior literature summary $\rightarrow$ research gap).
  - `1.2 Rumusan Masalah` & `1.3 Tujuan Penelitian`: Exact 1-to-1 numbered correspondence (`1..k`).
  - `1.4 Manfaat Penelitian`: Divided explicitly into *Manfaat Teoretis / Akademis* and *Manfaat Praktis / Kebijakan*.
- [ ] **Bab II (`Tinjauan Pustaka`)**:
  - Contains $\ge 5$ International Journals + $\ge 5$ National Journals (last 10 years) + $\ge 5$ Books/Standards (last 10 years).
  - Includes a structured **Tabel Matriks Penelitian Terdahulu** and an explicit **Kerangka Pemikiran / Hipotesis**.
- [ ] **Bab III (`Metode Penelitian`)**:
  - Explicitly justifies the research paradigm, approach, and design (e.g., Robert K. Yin, 2018; Creswell & Creswell, 2018).
  - Details population/informants (`IK-01` s.d. `IK-05` or sample size $n$), operational variable/concept definitions, data collection grids (*kisi-kisi instrumen*), data analysis steps (`Miles et al., 2014` or statistical tests), trustworthiness/validity (`triangulasi sumber, teknik, waktu`), and research ethics (`informed consent` & `UU No. 27 Tahun 2022`).
- [ ] **Cumulative Proposal Completeness (`Tugas 4`)**:
  - Includes Cover Page (with UT attribution), **single** `DAFTAR ISI` (page numbers synced to rendered PDF), `BAB I`, `BAB II`, `BAB III`, `DAFTAR PUSTAKA`, and `LAMPIRAN: Surat Pernyataan Kejujuran Akademik` (with student signature image embedded).

### B. DrillBit 0% AI & 0% Similarity Compliance (`ut_audit.py`)
- [ ] **Mode A (When fixing a DrillBit AI PDF Report)**: Only the blue-highlighted AI blocks were rewritten; 100% of unflagged (`0% AI`) Human paragraphs were preserved intact.
- [ ] **Mode B (When consolidating Tugas 1–3 into Tugas 4)**: All prose paragraphs were structurally paraphrased so 8-gram overlap against `Tugas 1–3` is `< 15%`.
- [ ] **Unbroken Sentence Run Ceiling**: `max_unbroken_run <= 4` raw `(?<=[.!?])\s+` sentences (`< 130 words`) across the entire document, anchored by natural period-space circuit-breakers (`No.`, `et al.`, `mis.`, `s.d.`, scholar initials).
- [ ] **Clause-Dense Syntax**: Zero artificial 6–13 word LLM signpost sentences; multi-clause 35–65 word sentences linked via `;`, `:`, and `/` technical pairs.
- [ ] **Terse Colon Lists**: All numbered/lettered conceptual definitions and instrument modules use `: <Active Verb/Noun Phrase>` with varied opening verbs.
- [ ] **Zero Em-Dashes & Lexical Ceilings**:
  - Em-dashes (`—`) = `0`
  - `secara <adjektiva>` `< 6.0 / 1,000 words`
  - `merupakan` `< 1.0 / 1,000 words`
  - `me-...-kan` `< 30.0 / 30/1k words`
  - Zero AI-paraphraser slop words (*sanggup*, *obrolan*, *pemakai*, *kawakan*, *paguyuban*).

### C. ODT XML, PDF Rendering & Visual Inspection
- [ ] `python3 scripts/ut_audit.py <File.odt>` passes with **0 findings**.
- [ ] `libreoffice --headless --convert-to pdf <File.odt>` succeeds without warnings or missing image placeholders.
- [ ] Every section and table in `DAFTAR ISI` matches its exact page number in the rendered PDF (`pdftotext -f N -l N`).
- [ ] Visual inspection of `pdftoppm -png -r 150` confirms clean typography, properly italicized foreign loanwords (`*...*`), intact tables, and visible signature PNG on the `Surat Pernyataan`.
