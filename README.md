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

---

## Daftar Skill

| Skill | Cakupan |
|---|---|
| [`metodologi-penelitian-univterbuka`](./metodologi-penelitian-univterbuka/SKILL.md) | Penyusunan, revisi, parafrase struktural, dan audit proposal penelitian (Bab I–III/IV/V) lintas fakultas Universitas Terbuka (FST, FEB, FHISIP, FKIP, Pascasarjana) maupun perguruan tinggi lain, dengan verifikasi referensi nyata, audit anti-slop, serta kalibrasi lolos pemindaian **DrillBit (< 30% AI Writing & < 30% Similaritas)**. |
| [`penjawab-tugas-akademik-ut`](./penjawab-tugas-akademik-ut/SKILL.md) | Penyusunan, audit, parafrase akademik, dan pemformatan tugas tutorial, diskusi Tuton/LMS, laporan praktikum/proyek/kasus lintas fakultas, serta naskah panduan video demonstrasi yang memenuhi ambang **DrillBit (< 30% AI Writing & Similaritas)**. |

---

## Standar Lolos Pemindaian DrillBit (< 30% AI Writing & < 30% Similaritas)

Di lingkungan Universitas Terbuka (dan berbagai perguruan tinggi yang menggunakan **DrillBit Plagiarism & AI Content Detection**), naskah proposal penelitian (khususnya **Tugas 4** yang wajib dilampiri *Lembar Bebas Plagiasi*) maupun karya ilmiah harus melewati pemindaian dengan batas maksimum **di bawah 30%** — baik pada skor **AI Text Detected (%)** maupun **Similarity (%)**. Kedua skill di repositori ini dirancang dengan target pengaman internal **< 15%** melalui mekanisme berikut:

1. **Kalibrasi Empat Dimensi *DrillBit AI Content Detection***:
   - **Pemutus Ritme Kalimat (*Intra-Paragraph Burstiness*)**: Mayoritas blok yang ditandai biru oleh DrillBit adalah paragraf panjang ($\ge 3$ kalimat) yang seluruh kalimatnya berukuran sedang-panjang (18–45 kata) tanpa kalimat pendek. Skill ini mewajibkan sisipan minimal satu kalimat pendek lugas (**6–13 kata**) di sela-sela kalimat analitis panjang (25–38 kata) pada setiap paragraf $\ge 60$ kata sehingga `min_sent <= 13` atau koefisien variasi panjang kalimat (`CV`) $\ge 0,36$.
   - **Reduksi Sintaksis Terjemahan Inggris SVO (`me-...-kan`)**: Menekan kepadatan verba aktif transitif `me-...-kan/-i` di bawah **30,0 per 1.000 kata** (blok yang terdeteksi AI oleh DrillBit rata-rata mencapai ~44,5/1.000 kata) dengan mengalihkan sebagian klausa ke bentuk pasif (`di-...-kan`/`ter-`), klausa nominal, atau pembuka preposisional (*Di tingkat...*, *Pada ranah...*, *Dari sisi...*).
   - **Pembatasan Adverbia `secara` & Kopula `merupakan`**: Menjaga kepadatan adverbia `secara <adjektiva>` **< 6,0 per 1.000 kata** dan kopula `merupakan` **< 1,0 per 1.000 kata**, serta menghapus verba pelaporan retoris khas LLM (*"menegaskan bahwa"*, *"membuktikan bahwa"*, *"menggarisbawahi bahwa"*, *"kendati demikian"*, *"namun demikian"*).
   - **Pemecahan Keseragaman Daftar Berpoin (*Layout Regularity*)**: Mencegah butir daftar berurutan (`1., 2., 3.` atau `a., b., c.`) dibuka dengan kata kerja atau kopula yang identik setelah tanda titik dua (mis. mengulang `Merupakan...` atau `Mengevaluasi...` di setiap butir).
2. **Parafrase Struktural & Anti-*Self-Plagiarism* Lintas Tugas (< 30% Similaritas)**:
   - DrillBit memindai kecocokan rangkaian kata berurutan (*n-gram matching*) terhadap jurnal, internet, dan repositori tugas mahasiswa (*Student Papers*, termasuk Tugas 1–3 yang dikumpulkan sebelumnya).
   - Saat menyusun proposal kumulatif (Tugas 4) atau memparafrasekan rujukan, skill ini menerapkan **parafrase struktural** (membalik urutan anak kalimat ↔ induk kalimat, mengubah aktif ↔ pasif, serta memecah/menggabungkan klausa) sambil mempertahankan 100% akurasi angka, tahun, nomor regulasi/standar (RFC, ISO, UU, PP), dan sitasi `(Penulis, Tahun)`.
   - Skrip `ut_audit.py --ref`, `simcheck.py`, `odt_para.py`, dan `paraphrase_validate.py` menyediakan pemeriksaan lokal otomatis sebelum dokumen diunggah ke LMS/DrillBit.

---

## Apa Saja yang Ada di Dalamnya?

Setiap folder skill bersifat mandiri (*self-contained*, *zero-dependency* Python standard library) dan terdiri dari tiga komponen utama:

1. **`SKILL.md`** — Instruksi utama, alur kerja (*workflow*), aturan etika AI, standar penulisan akademik humanis, serta adaptasi otomatis antara mode CLI lokal dan mode Web AI/LLM.
2. **`scripts/`** — Skrip utilitas Python (*zero-dependency*) untuk membantu audit dan verifikasi:
   - **Audit Tulisan, Anti-Slop, & Kepatuhan DrillBit (< 30% AI & Similaritas)**: `ut_audit.py` (audit PUEBI italic, sitasi APA 1-ke-1, *burstiness* kalimat, kepadatan sintaksis SVO/`secara`/`merupakan`, estimasi skor *DrillBit AI Content Detection*, dan cek similaritas `--ref`), `simcheck.py`, `paraphrase_validate.py`, `odt_para.py`, `prose_lint.py`, `ai_detector.py`, `text_analyzer.py`, `terminology_check.py`, `claim_audit.py`, `outline_extract.py`.
   - **Verifikasi Literatur & Sitasi Nyata**: `crossref_search.py`, `s2_search.py`, `arxiv_search.py`, `dblp_search.py`, `resolve_papers.py`, `resolve_oa.py`, `check_bibtex.py`, `polite_http.py`.
   - **Utilitas Tambahan** *(khusus `penjawab-tugas-akademik-ut`)*: `script_timer.py` & `word_budget.py` (pengatur durasi naskah video demonstrasi), serta `pt9.py` (pembaca/penulis berkas `.pkt`/`.pka` Cisco Packet Tracer 9).
3. **`references/`** — Dokumen acuan yang dibaca agen saat mengaudit naskah:
   - `llm-tells.md`, `hedging-and-claims.md`, `overclaiming-rules.md`, `verification-sources.md`, `diagnosis-patterns.md` (dan `script-craft.md`, `timing-and-cuts.md` pada `penjawab-tugas-akademik-ut`).

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
