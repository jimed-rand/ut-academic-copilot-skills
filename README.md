# UT & Academic Copilot Skills

> [!CAUTION]
> ## DISCLAIMER BESAR: HANYA UNTUK **COPILOT** TUGAS, BUKAN **"NGEJOKI PENUH PAKE AI"**
>
> Kumpulan *agent skill* ini dibuat semata-mata sebagai **mitra belajar (*copilot*)** untuk membantu mahasiswa merapikan struktur tulisan, menyunting tata bahasa Indonesia baku (EYD/PUEBI), memformat sitasi APA/institusi, memverifikasi referensi nyata, dan memeriksa konsistensi argumen.
>
> **Skill ini BUKAN alat "ngejoki penuh pakai AI" atau mesin pembuat tugas instan.**
> - **Sisanya wajib dikerjakan oleh mahasiswa sendiri**: menentukan topik/ide, membaca sumber asli, menjalankan praktikum/simulasi/perhitungan sendiri, menganalisis data, menulis substansi utama, serta memahami seluruh isi naskah sebelum dikumpulkan.
> - **Dilarang keras** menyerahkan keluaran AI mentah (*AI-giarism*), memalsukan data/angka, memalsukan hasil praktikum/log terminal, atau mengarang sitasi.
> - Penggunaan wajib mematuhi **Peraturan Rektor Universitas Terbuka Nomor 436 Tahun 2025** (Kode Etik Sivitas Akademika terkait *KA Generatif*), **Panduan Penggunaan GenAI pada Pembelajaran di Perguruan Tinggi** (Ditjen Diktiristek Kemendikbudristek, 2024), serta aturan spesifik mata kuliah/dosen/ujian di institusi masing-masing.
> - Jika suatu ujian (UAS/THE/TMK) atau tugas melarang penggunaan AI, **jangan gunakan skill ini**.

> [!NOTE]
> Skill ini hanya membantu bagi pengguna **LibreOffice** dengan format **OpenDocument** dan pengguna Linux, dan bagi anda yang menggunakan skills ini harap menggunakan LibreOffice untuk pengerjaan dokumen nya di dalam lingkungan Linux (jika anda menggunakan Windows, dapat memanfaatkan WSL2 atau membuat mesin virtual dengan VMWare Workstation atau Hyper-V serta memasang distribusi Linux favorit anda). Skills ini tidak mendukung dokumen dengan format **Office Open XML (OOXML)** yang digunakan Microsoft 365.
---

## Daftar Skill

| Skill | Cakupan |
|---|---|
| [`metodologi-penelitian-univterbuka`](./metodologi-penelitian-univterbuka/SKILL.md) | Penyusunan, revisi, parafrase struktural, dan audit proposal penelitian (Bab I–III/IV/V) lintas fakultas Universitas Terbuka (FST, FEB, FHISIP, FKIP, Pascasarjana) maupun perguruan tinggi lain, dengan verifikasi referensi nyata, audit anti-slop, serta kalibrasi lolos pemindaian **DrillBit (< 30% AI Writing & < 30% Similaritas)**. |
| [`penjawab-tugas-akademik-ut`](./penjawab-tugas-akademik-ut/SKILL.md) | Penyusunan, audit, parafrase akademik, dan pemformatan tugas tutorial, diskusi Tuton/LMS, laporan praktikum/proyek/kasus lintas fakultas, serta naskah panduan video demonstrasi yang memenuhi ambang **DrillBit (< 30% AI Writing & Similaritas)**. |

---

## Standar Lolos Pemindaian DrillBit (Terbukti 0% AI Writing & 0% Similaritas)

Di lingkungan Universitas Terbuka (dan berbagai perguruan tinggi yang menggunakan **DrillBit Plagiarism & AI Content Detection**), naskah proposal penelitian (khususnya **Tugas 4** yang wajib dilampiri *Lembar Bebas Plagiasi*) maupun karya ilmiah harus melewati pemindaian dengan batas maksimum **di bawah 30%** — baik pada skor **AI Text Detected (%)** maupun **Similarity (%)**. Kedua skill di repositori ini menerapkan **metodologi forensik yang telah tervalidasi mencapai 0% AI Score dan 0% Similarity** pada pemindaian DrillBit nyata (`references/drillbit-zero-ai-playbook.md`):

1. **5 Pilar Forensik 0% *DrillBit AI Content Detection***:
   - **Sintaksis Klausa Padat Multi-Klausa (`;` / `:` / `/`) — Tanpa Injeksi Kalimat Pendek Klise**: Pengujian forensik pada laporan PDF DrillBit membuktikan bahwa menyisipkan kalimat pendek deklaratif buatan (6–13 kata) justru **menaikkan** skor AI. Sebagai gantinya, gagasan akademik dipadatkan dalam kalimat multi-klausa (35–65 kata) dengan titik koma (`;`), titik dua (`:`), dan pasangan istilah teknis (`server-to-server / S2S`, `CPU/RAM`, `OMEMO/OTR`).
   - **Pemutus Rangkaian Titik-Spasi Akademik & Regulasi Alami**: DrillBit memecah aliran teks pada setiap titik diikuti spasi (`(?<=[.!?])\s+`) dan baru memicu blok biru AI ketika terdapat $\ge 6$ kalimat polos berturut-turut ($\ge 139$ kata). Setiap paragraf dijangkarkan dengan rujukan autentik berformat baku (`UU No. 27 Tahun 2022`, `PP No. 71 Tahun 2019`, `RFC No. 6120`, `XEP No. 0384`, sitasi APA 7th `Author et al. (Tahun)`, inisial pakar kanonik, serta `mis.` / `s.d.` / `hlm.`) agar rangkaian kalimat polos tetap $\le 5$ kalimat (`< 139 kata`).
   - **Definisi Daftar Titik Dua Ringkas (*Terse Colon List Definitions*)**: Butir daftar definisi konsep, variabel operasional, dan instrumen menggunakan frasa kerja/nomina aktif langsung setelah titik dua (`: Menelaah...`, `: Mengukur...`, `: Meliputi...`) dengan verba pembuka yang bervariasi antarbutir.
   - **Nol Em-Dash (`— = 0`), Bebas Sinonim Slop, & Batas Kepadatan Leksikal**: Seluruh em-dash (`—`) diganti koma/kurung, sinonim parafrase mekanis dihindari, serta kepadatan `secara <adjektiva>` dijaga **< 6,0/1k kata**, `merupakan` **< 1,0/1k kata**, dan `me-...-kan/-i` **< 30,0/1k kata**.
   - **Mode A (Perbaikan Blok Biru Terarah) vs. Mode B (Parafrase Kumulatif Penuh)**: Saat merevisi draf yang sudah memiliki laporan PDF DrillBit (*Mode A*), agen hanya menulis ulang paragraf yang ditandai biru AI dan **mempertahankan 100% paragraf yang sudah lolos sebagai 0% AI (Human)**.
2. **Parafrase Struktural & Anti-*Self-Plagiarism* Lintas Tugas (0% Similaritas)**:
   - DrillBit memindai kecocokan rangkaian kata berurutan (*n-gram matching*) terhadap jurnal, internet, dan repositori tugas mahasiswa (*Student Papers*, termasuk Tugas 1–3 yang dikumpulkan sebelumnya).
   - Saat menyusun proposal kumulatif (Tugas 4) atau memparafrasekan rujukan (*Mode B*), skill ini menerapkan **5 teknik parafrase struktural** (`references/academic-paraphrasing-and-proofreading.md`) sambil mempertahankan 100% akurasi angka, tahun, nomor regulasi/standar (RFC, ISO, UU, PP), dan sitasi `(Penulis, Tahun)`.
   - Skrip `ut_audit.py --ref`, `simcheck.py`, `odt_para.py` (aman untuk *in-place packing* & menjaga integritas `Pictures/*` + `META-INF/manifest.xml`), dan `paraphrase_validate.py` menyediakan pemeriksaan lokal otomatis sebelum dokumen diunggah ke LMS/DrillBit.

---

## Apa Saja yang Ada di Dalamnya?

Setiap folder skill bersifat mandiri (*self-contained*, *zero-dependency* Python standard library) dan terdiri dari tiga komponen utama:

1. **`SKILL.md`** — Instruksi utama, alur kerja (*workflow*), aturan etika AI, standar penulisan akademik humanis, serta adaptasi otomatis antara mode CLI lokal dan mode Web AI/LLM.
2. **`scripts/`** — Skrip utilitas Python (*zero-dependency*) untuk membantu audit dan verifikasi:
   - **Audit Tulisan, Anti-Slop, & Kepatuhan DrillBit (< 30% AI & Similaritas)**: `ut_audit.py` (audit PUEBI italic, sitasi APA 1-ke-1, *burstiness* kalimat, kepadatan sintaksis SVO/`secara`/`merupakan`, estimasi skor *DrillBit AI Content Detection*, dan cek similaritas `--ref`), `simcheck.py`, `paraphrase_validate.py`, `odt_para.py`, `prose_lint.py`, `ai_detector.py`, `text_analyzer.py`, `terminology_check.py`, `claim_audit.py`, `outline_extract.py`.
   - **Verifikasi Literatur & Sitasi Nyata**: `crossref_search.py`, `s2_search.py`, `arxiv_search.py`, `dblp_search.py`, `resolve_papers.py`, `resolve_oa.py`, `check_bibtex.py`, `polite_http.py`.
   - **Utilitas Tambahan** *(khusus `penjawab-tugas-akademik-ut`)*: `script_timer.py` & `word_budget.py` (pengatur durasi naskah video demonstrasi), serta `pt9.py` (pembaca/penulis berkas `.pkt`/`.pka` Cisco Packet Tracer 9).
3. **`references/`** — Pustaka panduan akademik mandiri (*self-contained copies*) yang dibaca agen saat menyusun dan mengaudit naskah di kedua skill:
   - `drillbit-zero-ai-playbook.md` — Playbook forensik **0% DrillBit AI & 0% Similaritas** (Mode A blok-terarah vs. Mode B parafrase kumulatif, 5 pilar sintaksis, parser PDF DrillBit).
   - `academic-paraphrasing-and-proofreading.md` — 5 teknik parafrase struktural, 10 prinsip humanisasi akademik, katalog *Signs of AI Writing*, proofreading PUEBI/EYD & bahasa Inggris, serta kamus kata baku KBBI & istilah asing cetak miring.
   - `methodology-and-data-analysis.md` — Paradigma & desain penelitian, sampling, sintesis literatur & 5 tipe *research gap*, uji statistik & *effect size*, analisis kualitatif (Miles-Huberman-Saldaña, Braun & Clarke, Lincoln & Guba), etika riset (UU PDP), & abstrak IMRAD.
   - `citation-and-submission-checklist.md` — Templat sitasi APA 7th, IEEE, Chicago, Harvard, MLA, protokol verifikasi DOI anti-halusinasi, audit sitasi 1-ke-1, & daftar periksa pra-kumpul UT.
   - `llm-tells.md`, `hedging-and-claims.md`, `overclaiming-rules.md`, `verification-sources.md`, `diagnosis-patterns.md`, `script-craft.md`, `timing-and-cuts.md`.

---

## Cara Menggunakan

### 1. Via `skills.sh` / Skills CLI (Direkomendasikan)
Pasang langsung dari GitHub ke agen lokal Anda (Claude Code, Gemini CLI, Codex, Antigravity, dll.):

```bash
npx skills add jimed-rand/ut-academic-copilot-skills
```

Atau pilih skill tertentu saja:

```bash
npx skills add jimed-rand/ut-academic-copilot-skills --skill metodologi-penelitian-univterbuka
npx skills add jimed-rand/ut-academic-copilot-skills --skill penjawab-tugas-akademik-ut
```

### 2. Pemasangan Manual di Mesin Lokal (CLI Agent)
Salin atau *symlink* folder skill ke direktori skill agen Anda (mis. `~/.agents/skills/`):

```bash
cp -r metodologi-penelitian-univterbuka penjawab-tugas-akademik-ut ~/.agents/skills/
```

Skrip audit bawaan (hanya menggunakan Python 3 standard library) dapat dijalankan langsung dari dalam folder masing-masing skill:

```bash
# Audit AI slop, estimasi DrillBit AI (< 30%), PUEBI italic, burstiness, & sitasi APA 1-ke-1
python3 scripts/ut_audit.py <berkas.md|.odt|.docx>

# Audit lengkap disertai cek similaritas 8-gram (< 30%) terhadap draf/tugas terdahulu
python3 scripts/ut_audit.py <Tugas4.odt> --ref <Tugas1.odt> <Tugas2.odt> <Tugas3.odt>
```

### 3. Web AI/LLM (Claude Web, Gemini Web, dll.)
Kompres masing-masing folder skill menjadi `.zip` (atau `.skill`) lalu unggah ke antarmuka web AI yang mendukung *Skills* / *Custom Instructions*.

---

## Prinsip Penggunaan yang Bertanggung Jawab

1. **Verifikasi Mandiri**: Setiap tautan DOI/URL, peraturan perundang-undangan, angka statistik, dan keluaran praktikum wajib dibuka dan diverifikasi sendiri oleh mahasiswa sebelum dikumpulkan.
2. **Transparansi**: Bila mata kuliah, tutor, atau institusi mewajibkan pernyataan penggunaan AI, sertakan deklarasi penggunaan AI secara jujur. AI tidak boleh dicantumkan sebagai penulis di Daftar Pustaka.
3. **Privasi Data**: Jangan memasukkan data pribadi sensitif, identitas responden, atau data rahasia instansi ke dalam layanan AI publik tanpa anonimisasi.

---

## Lisensi

- Seluruh skrip Python di dalam direktori `scripts/` dilisensikan di bawah **GNU General Public License v2.0 or later (`GPL-2.0-or-later`)** — lihat berkas [`LICENSE`](./LICENSE).
- Pengecualian: [`penjawab-tugas-akademik-ut/scripts/pt9.py`](./penjawab-tugas-akademik-ut/scripts/pt9.py) tetap mengikuti lisensi aslinya yaitu **`GPL-3.0-or-later`** (`Copyright (C) 2026 aacanadaa`).
