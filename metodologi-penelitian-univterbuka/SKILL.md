---
name: "metodologi-penelitian-univterbuka"
description: "Skill mandiri (zero-dependency) untuk menyusun, merevisi, dan memeriksa proposal penelitian, karya ilmiah, atau tugas akhir mata kuliah Metodologi Penelitian di seluruh fakultas dan program studi Universitas Terbuka (FST, FEB, FHISIP, FKIP, Pascasarjana — seperti STSI4310, MSIM4312, EKMA4367, HKUM4306, SOSI4311, IDIK4007, dll.) maupun perguruan tinggi lain. Mengikuti sistematika resmi panduan mata kuliah/institusi (dengan acuan dasar STSI4310P / BMP MSIM4312 Tugas 1-4 bila tidak ada format lain), data dan referensi nyata yang terverifikasi, tulisan manusiawi bebas AI slop, kepatuhan etika penggunaan AI (Pertor UT No. 436/2025 & Panduan GenAI Diktiristek), serta adaptasi dinamis antara mesin lokal (CLI) dan AI/LLM di web. Gunakan setiap kali diminta membuat, merevisi, atau mengevaluasi Bab I-IV/V proposal penelitian, judul penelitian, rumusan masalah, kajian pustaka, landasan teori, pertanyaan penelitian/hipotesis, metode penelitian, daftar pustaka (APA Style atau gaya sitasi institusi), atau memeriksa keaslian referensi, kebenaran data, dan gaya tulisan."
---

# Penyusunan Proposal Penelitian (Lintas Fakultas UT & Perguruan Tinggi — Self-Contained)

## Sumber Acuan & Sifat Mandiri (Zero External Dependency)
Skill ini dirancang untuk penyusunan proposal penelitian di **semua fakultas dan program studi Universitas Terbuka** (FST, FEB, FHISIP, FKIP, dan Sekolah Pascasarjana) maupun **perguruan tinggi lain** (lintas rumpun ilmu: Sains & Teknologi, Ekonomi & Bisnis, Hukum & Ilmu Sosial-Politik, Pendidikan/Keguruan, serta Kesehatan/Humaniora).

Secara bawaan, skill ini menyediakan kerangka lengkap Tugas 1–4 berdasarkan *"Panduan Praktik Penyusunan Proposal Penelitian"* (`STSI4310P` / BMP `MSIM4312` Modul 1–9), namun **bersifat adaptif**: apabila mata kuliah, fakultas, atau universitas pengguna memiliki panduan, jumlah bab (mis. Bab I–III atau Bab I–V), struktur subbab, atau gaya sitasi khusus (APA 7th, IEEE, Chicago, Harvard, Vancouver), **ikuti panduan resmi mata kuliah/institusi pengguna terlebih dahulu**. Seluruh kaidah *deslopification*, *academic humanization*, kalibrasi klaim, metodologi & analisis data, restrukturisasi bab, dan verifikasi sitasi ilmiah telah **diintegrasikan langsung di dalam skill ini beserta skrip bawaannya (`scripts/` dan `references/`)**, sehingga **tidak memerlukan ketergantungan pada skill eksternal** dan dapat digunakan baik di **mesin lokal (CLI)** maupun di **AI/LLM berbasis web (Claude Web / Gemini Web)**.

### Pustaka Referensi Bawaan (`references/`)
Baca berkas acuan berikut sesuai kebutuhan tugas agar hasil konsisten dan terukur:
- `references/drillbit-zero-ai-playbook.md` — **Playbook Forensik 0% DrillBit AI & 0% Similaritas** (Mode A perbaikan blok biru terarah vs. Mode B parafrase kumulatif penuh, 5 pilar sintaksis, skrip ekstraksi PDF laporan DrillBit, serta contoh sebelum/sesudah).
- `references/academic-paraphrasing-and-proofreading.md` — 5 teknik parafrase struktural mendalam, 10 prinsip humanisasi akademik, katalog *Signs of AI Writing*, matriks proofreading PUEBI/EYD & bahasa Inggris, serta kamus kata baku KBBI dan istilah asing cetak miring.
- `references/methodology-and-data-analysis.md` — Paradigma & desain riset (kuantitatif, kualitatif, *mixed methods*), teknik sampling, matriks sintesis & 5 tipe *research gap*, pemilihan uji statistik & *effect size*, model interaktif Miles-Huberman-Saldaña (2014), keabsahan Lincoln & Guba, etika riset (UU PDP No. 27 Tahun 2022), serta panduan abstrak IMRAD.
- `references/citation-and-submission-checklist.md` — Templat sitasi APA 7th (Indonesia & Inggris), IEEE, Chicago, Harvard, MLA, protokol anti-halusinasi & triase DOI, audit 1-ke-1 In-Text ↔ Daftar Pustaka, serta daftar periksa visual pra-kumpul UT.
- `references/llm-tells.md`, `references/hedging-and-claims.md`, `references/overclaiming-rules.md`, `references/verification-sources.md`, `references/diagnosis-patterns.md` — Katalog detail tanda LLM, kalibrasi hedging/klaim, dan otoritas indeks verifikasi.

## Adaptasi Dinamis Lingkungan & Identitas Mahasiswa

### 1. Identitas Mahasiswa & Konvensi Berkas (Isi Sesuai Profil Pengguna)
Jangan menyimpan atau menyertakan data pribadi nyata secara permanen di dalam skill. Minta pengguna mengisi atau mengonfirmasi profil berikut bila belum tersedia di percakapan:
- **Nama**: `[Nama Lengkap Mahasiswa]`
- **NIM**: `[NIM]`
- **Program Studi**: `[Program Studi]`
- **Fakultas**: `[Fakultas]`
- **Perguruan Tinggi**: `[Universitas Terbuka / Nama Perguruan Tinggi]`
- **Mata Kuliah**: `[Kode & Nama Mata Kuliah, mis. STSI4310 – Metodologi Penelitian]`
- **Konvensi Berkas di direktori kerja tugas (`<direktori-kerja>`)**:
  - `Tugas{1|2|3|4}_{KODE_MK}_{Topik_Singkat}_{NIM}.{odt|docx|pdf}` (atau sesuai format penamaan yang diminta oleh mata kuliah/institusi).

### 2. Mode Mesin Lokal (CLI) vs. Mode Web AI/LLM
- **Bila dijalankan di Mesin Lokal (`<direktori-kerja>`)**:
  - **Manipulasi Dokumen Kumulatif (`.odt` / `.docx`)**: Baca dan perbarui berkas `.odt` tugas sebelumnya menggunakan modul standar Python (`zipfile` + `xml.etree.ElementTree` pada `content.xml` dan `styles.xml`) atau skrip bantu `scripts/odt_para.py` (`extract`, `inject`, `pack`). Untuk Tugas 2–3, pertahankan bagian yang sudah dinilai baik ("Dipertahankan"); khusus untuk **Tugas 4 (atau ketika pengguna meminta parafrase anti-DrillBit)**, lakukan parafrase struktural menyeluruh pada seluruh bab kumulatif agar skor **DrillBit AI Content Detection < 30%** dan **DrillBit Similarity < 30%** (target utama **< 15%**). Pastikan setiap istilah asing dibungkus dengan `<text:span text:style-name="T_Italic">` (atau style italic aktif seperti `T2`/`T3`) dan menggunakan font serif (Times New Roman / Liberation Serif).
  - **Kompilasi & Pemeriksaan Visual PDF**: Konversi `.odt` ke `.pdf` dengan `libreoffice --headless --convert-to pdf <berkas.odt>`, lalu jalankan `pdftoppm -png -r 150 <berkas.pdf> /tmp/page` atau `pdftotext` untuk memeriksa halaman Daftar Isi (pastikan judul `DAFTAR ISI` tidak tercetak ganda di batas halaman), tabel tidak terpotong buruk, dan nomor halaman sinkron 100%.
  - **Audit Otomatis, Estimasi DrillBit (< 30%), & Pencarian Literatur Lokal**: Jalankan `python3 scripts/ut_audit.py <berkas.odt|.md> --ref <Tugas1.odt> <Tugas2.odt> <Tugas3.odt>` untuk memindai pola AI slop Bahasa Indonesia/Inggris, mengestimasi skor **DrillBit AI Content Detection** (wajib `< 30%`, target `< 15%`), menghitung overlap similaritas 8-gram terhadap tugas terdahulu (wajib `< 30%`, target `< 15%`), memeriksa *burstiness* kalimat, disiplin cetak miring PUEBI, duplikasi Daftar Isi, dan kesesuaian 1-ke-1 kutipan in-text vs Daftar Pustaka. Gunakan juga `scripts/simcheck.py` dan `scripts/paraphrase_validate.py` saat memparafrasekan segmen ODT secara massal, serta `scripts/crossref_search.py`, `scripts/s2_search.py`, dan `scripts/resolve_papers.py` untuk memverifikasi metadata DOI/jurnal.
- **Bila dijalankan di Web AI/LLM (Claude Web / Gemini Web)**:
  - Gunakan fitur **Web Search / Web Fetch** bawaan untuk memverifikasi setiap artikel jurnal, DOI, regulasi, dan data statistik sebelum menulis.
  - Bila *Code Execution / Python sandbox* tersedia di web, jalankan `scripts/ut_audit.py` pada draf; bila tidak tersedia, jalankan pemeriksaan manual menggunakan daftar periksa di bagian "Standar Anti-Slop" dan "Gerbang Pemeriksaan Akhir".

## Prinsip Utama: Penelitian Nyata, AI Seperlunya
Penilai Tugas 2 menuliskan catatan umum bahwa AI/LLM digunakan seperlunya dan bahwa penelitian semestinya memakai data dan referensi yang nyata. Catatan ini adalah syarat tertinggi skill ini dan mengalahkan target panjang, kelengkapan, atau kerapian apa pun.

| Boleh dibantu AI/LLM | Wajib berasal dari penelusuran nyata atau keputusan mahasiswa (dapat dibantu Web Search function jika mahasiswa memerlukan bantuan LLM) |
|---|---|
| Merapikan struktur, menyunting tata bahasa dan EYD, memeriksa konsistensi antarbagian, memformat sitasi APA dari metadata yang sudah terverifikasi, menyusun matriks dari artikel yang benar-benar sudah dibaca, memeriksa cacat teknis dokumen | Setiap angka, tahun, nama peraturan, nama lembaga, judul artikel, nama penulis, DOI/URL, dan temuan penelitian terdahulu; pilihan topik, lokasi, objek, dan metode; klaim kesenjangan penelitian; kesimpulan sementara |

Aturan turunan:
- Pengetahuan Claude, Gemini, dan AI/LLM agentic lain dipakai untuk menyusun kata kunci pencarian dan kerangka konsep, bukan sebagai sumber fakta. Fakta berasal dari halaman atau dokumen asli yang dibuka pada sesi berjalan.
- Bila sesuatu tidak dapat diverifikasi, tulis lebih lemah atau hapus. Jangan mengisi dengan perkiraan, jangan menebak DOI, tahun, atau halaman.
- Mahasiswa harus mampu menjelaskan dan menunjukkan sumber setiap data dan referensi bila ditanya dosen. Susun naskah agar hal itu mungkin.
- Tujuan standar anti-slop adalah mutu, kejelasan, dan keaslian tulisan ilmiah, bukan untuk mengelabui pemeriksa atau menyamarkan kepengarangan.
- **Kepatuhan Etika Penggunaan AI (UT & Perguruan Tinggi)**:
  - Ikuti **Peraturan Rektor Universitas Terbuka Nomor 436 Tahun 2025** tentang Kode Etik Sivitas Akademika, Tenaga Kependidikan, dan Pendidik Eksternal (yang mengatur pemanfaatan Kecerdasan Artifisial Generatif secara etis, bertanggung jawab, dan menjaga perlindungan data pribadi), serta **Panduan Penggunaan Generative Artificial Intelligence (GenAI) pada Pembelajaran di Perguruan Tinggi** (Ditjen Diktiristek Kemendikbudristek, 2024) dan ketentuan spesifik fakultas/program studi/tutor.
  - **AI sebagai Mitra (*Copilot*), Bukan Pengganti**: AI membantu menstrukturkan, menyunting bahasa, dan memverifikasi konsistensi; mahasiswa tetap menjadi penulis utama yang menentukan arah riset, menganalisis secara kritis, dan bertanggung jawab penuh atas isi naskah. Dilarang menyerahkan draf AI mentah tanpa telaah dan verifikasi mandiri (*AI-giarism*).
  - **Transparansi & Deklarasi**: Bila mata kuliah, dosen, atau institusi mewajibkan pernyataan penggunaan AI, bantu menyusun deklarasi secara jujur (alat yang digunakan, tujuan pemanfaatan, serta penegasan bahwa substansi dan verifikasi dilakukan mahasiswa). AI **tidak boleh** dicantumkan sebagai penulis pada Daftar Pustaka.
  - **Privasi & Keamanan Data**: Jangan memasukkan data pribadi sensitif, identitas responden, atau data rahasia instansi penelitian ke dalam layanan AI publik tanpa anonimisasi terlebih dahulu.
  - **Kepatuhan Ujian/Tugas Khusus**: Jika ketentuan tugas, ujian, atau tutor melarang penggunaan AI pada komponen tertentu, ikuti aturan yang lebih ketat.

## Kapan Digunakan
Gunakan skill ini ketika pengguna:
- Meminta bantuan menyusun Tugas 1–4 atau proposal penelitian lengkap (Bab I–III/IV/V) mata kuliah Metodologi Penelitian / Tugas Akhir / Karya Ilmiah di UT maupun perguruan tinggi lain.
- Meminta review atau revisi terhadap bab proposal penelitian yang sudah ada.
- Bertanya tentang sistematika, format cover, metode penelitian (kualitatif, kuantitatif, campuran, yuridis-normatif/empiris, R&D/PTK), atau rubrik penilaian proposal penelitian.
- Meminta komentar dosen/pembimbing diterapkan, referensi atau data diperiksa keasliannya, atau gaya tulisan dibersihkan dari pola generik AI/LLM.
- *Catatan batas cakupan*: Untuk tugas mata kuliah reguler, diskusi Tuton, esai, atau laporan praktikum/kasus di luar penyusunan proposal penelitian, gunakan skill `penjawab-tugas-akademik-ut`.

## Alur Kerja
1. **Tentukan cakupan tugas** — tanyakan atau simpulkan dari konteks apakah pengguna sedang mengerjakan Tugas 1, 2, 3, atau 4, karena setiap tugas memiliki elemen wajib berbeda (lihat tabel "Cakupan per Tugas" di bawah). Elemen di luar cakupan tugas ditandai "KOSONGKAN" dan tidak perlu diisi.
2. **Baca dokumen tugas sebelumnya** bila pengguna menyertakannya (atau dari `<direktori-kerja>/Tugas*_STSI4310_*.odt` bila di mesin lokal). Pertahankan bagian yang dinilai baik atau bertanda "Dipertahankan", ubah hanya bagian yang diminta atau yang perlu diperbaiki menurut "Umpan Balik Penilai: Riwayat dan Tindak Lanjut", dan jangan menulis ulang bagian yang tidak berubah.
3. **Kumpulkan input inti dari pengguna**: topik/bidang penelitian, jenis penelitian (kuantitatif/kualitatif/campuran), dan objek/subjek penelitian (mis. instansi, populasi). Jika belum ada, ajukan pertanyaan singkat sebelum menyusun draf penuh.
4. **Riset dan verifikasi dahulu** sesuai "Protokol Riset dan Verifikasi Sumber" sebelum menulis satu pun klaim faktual.
5. **Susun sesuai Sistematika Proposal** (lihat tabel di bawah), bab per bab, dengan bahasa akademik formal ragam Indonesia baku (EYD/PUEBI) dan "Standar Anti-Slop & Humanisasi Akademik".
6. **Sertakan Daftar Pustaka APA Style** yang hanya memuat sumber terverifikasi dan konsisten 1-ke-1 dengan sitasi dalam teks.
7. **Format keluaran**: satu dokumen utuh mengikuti struktur cover → daftar isi → Bab I-IV (sesuai cakupan tugas) → daftar pustaka. Cover mengikuti template resmi di bagian "Template Cover". Dokumen bersifat kumulatif: setiap pengumpulan memuat seluruh bab yang masuk cakupan tugas tersebut.
8. **Jalankan "Gerbang Pemeriksaan Akhir"** (termasuk `scripts/ut_audit.py` bila Python tersedia) sebelum menyerahkan hasil, lalu laporkan di chat (bukan di dalam dokumen) bagian yang berpotensi mengurangi skor dan hal yang harus diverifikasi sendiri oleh mahasiswa.

## Cakupan per Tugas

| Elemen | Tugas 1 | Tugas 2 | Tugas 3 | Tugas 4 (Proposal Final) |
|---|---|---|---|---|
| Cover + Daftar Isi | Isi | Isi | Isi | Isi |
| Bab I: Latar Belakang, Rumusan Masalah, Tujuan & Manfaat | Isi | Isi | Isi | Isi |
| Bab II: Kajian Pustaka & Landasan Teori, Pertanyaan Penelitian/Hipotesis | Kosongkan | Isi | Isi | Isi |
| Bab III: Metode Penelitian, Teknik Pengumpulan Data & Instrumen | Kosongkan | Kosongkan | Isi | Isi |
| Bab IV: Teknik Analisis Data, Kesimpulan Sementara & Batasan Penelitian | Kosongkan | Kosongkan | Kosongkan | Isi |
| Daftar Pustaka | Isi | Isi | Isi | Isi |

Catatan: Tugas 4 diunggah ulang setelah cek similaritas (plagiarisme) dan disertai Lembar Bebas Plagiasi (`MKKI - Lembar Bebas Plagiasi Metode Penelitian (<NIM>)`).

## Sistematika Proposal Penelitian (Isi Setiap Elemen)

**Judul Penelitian** — Menunjukkan variabel penelitian secara jelas dan ringkas (acuan Modul 1: jenis dan sifat penelitian).

**Bab I — Pendahuluan**
- *Latar Belakang Masalah*: jelaskan fenomena yang melatarbelakangi penelitian dan sertakan *gap research* (kesenjangan penelitian) yang menunjukkan orisinalitas. (Modul 1 & 2)
- *Rumusan Masalah*: disusun dalam kalimat tanya yang fokus dan dipecah menjadi poin bernomor (umumnya tiga poin) dengan urutan logis dari deskriptif, analitis, hingga eksplanatif (lihat bagian "Pola Rumusan Masalah Berpoin"); gunakan diagram tulang ikan (*fishbone*) bila relevan. (Modul 2)
- *Tujuan dan Manfaat Penelitian*: Tujuan = apa yang ingin dicapai; Manfaat = teoritis dan praktis. (Modul 2)

**Bab II — Kajian Pustaka & Landasan Teori**
- *Kajian Pustaka dan Landasan Teori*: telaah literatur dan teori pendukung yang relevan dan mutakhir. (Modul 3)
- *Pertanyaan Penelitian / Hipotesis*: pertanyaan penelitian untuk kualitatif, atau hipotesis (H0/H1) untuk kuantitatif, disertai definisi operasional variabel. (Modul 4)

**Bab III — Metode Penelitian**
- *Metode Penelitian*: pilih pendekatan sesuai rumpun ilmu dan masalah (kuantitatif, kualitatif, campuran/*mixed methods*, penelitian tindakan kelas [PTK], *Research and Development* [R&D], atau yuridis-normatif/yuridis-empiris pada ilmu hukum) dan uraikan desain penelitian (populasi, sampel/informan, teknik sampling, atau bahan hukum). (Acuan dasar Modul 5)
- *Teknik Pengumpulan Data dan Instrumen Penelitian*: instrumen (kuesioner, pedoman wawancara, lembar observasi, studi dokumentasi/kepustakaan, atau pengujian eksperimental) beserta uji validitas dan reliabilitas (kuantitatif) atau uji keabsahan data/triangulasi (kualitatif). (Acuan dasar Modul 6 & 7)

**Bab IV — Analisis Data dan Kesimpulan Sementara** *(atau disesuaikan bila panduan mata kuliah/institusi berhenti di Bab III)*
- *Teknik Analisis Data*: analisis deskriptif dan inferensial/uji hipotesis bila kuantitatif; reduksi, penyajian, penarikan kesimpulan, dan analisis tematik/wacana/sosioteknis/yuridis sesuai pendekatan kualitatif/hukum/sosial. (Acuan dasar Modul 8)
- *Kesimpulan Sementara dan Batasan Penelitian*: kontribusi yang diharapkan serta keterbatasan penelitian sebagai bahan saran. (Acuan dasar Modul 9)
- *Daftar Pustaka*: gunakan APA Style 7th Edition secara default (atau gaya sitasi lain seperti IEEE, Chicago, Harvard, atau Vancouver bila diwajibkan oleh fakultas/institusi); konsisten 1-ke-1 dengan kutipan dalam teks; anjurkan pengelola sitasi (Mendeley/Zotero). (Acuan dasar Modul 9)

## Pola Rumusan Masalah Berpoin
Umpan balik penilai pada Tugas 1 (Rumusan Masalah memperoleh kategori cukup) menunjukkan bahwa rumusan harus disusun sebagai poin bernomor yang masing-masing mewakili satu dimensi penelitian yang berbeda dan berurutan, bukan sekumpulan pertanyaan yang bercampur atau terlalu luas.

| Poin | Dimensi | Fokus yang ditanyakan | Kata kerja operasional pada Tujuan |
|---|---|---|---|
| 1 | Deskriptif | Eksistensi, kondisi terkini, dan pola pemanfaatan objek penelitian | Mengidentifikasi |
| 2 | Analitis | Karakteristik atau aspek teknis objek penelitian terhadap konsep inti yang menjadi variabel pada judul | Menganalisis |
| 3 | Eksplanatif dan implikatif | Faktor penyebab atau penghambat kondisi yang dipermasalahkan beserta implikasinya pada kebijakan, organisasi, atau praktik | Membedah |

Kerangka kalimat tanya yang dapat diadaptasi:
1. Bagaimana eksistensi dan pola pemanfaatan terkini [objek penelitian] di [konteks atau lokasi penelitian]?
2. Bagaimana karakteristik [aspek teknis atau ciri objek] pada [objek penelitian] berkaitan dengan [konsep inti atau variabel]?
3. Faktor apa yang menyebabkan [kondisi masalah, misalnya rendahnya *awareness*] dan apa implikasinya bagi [kebijakan, organisasi, atau praktik]?

Contoh penerapan lintas bidang:
- *Ekonomi/Manajemen*: poin 2 menganalisis pengaruh kualitas layanan dan kepercayaan terhadap loyalitas nasabah; poin 3 membedah faktor penghambat adopsi layanan digital di UMKM beserta implikasinya pada strategi pemasaran.
- *Hukum/Kebijakan*: poin 2 menganalisis kesesuaian regulasi daerah dengan undang-undang terkait perlindungan data pribadi; poin 3 membedah kendala penegakan hukum beserta implikasinya bagi tata kelola lembaga.
- *Pendidikan*: poin 2 menganalisis efektivitas model pembelajaran berbasis proyek terhadap literasi numerasi siswa; poin 3 membedah kendala kesiapan guru beserta implikasinya pada pelatihan sekolah.
- *Sistem Informasi/Teknologi*: poin 2 menelaah karakteristik arsitektur teknis terhadap konsep tata kelola atau kedaulatan digital; poin 3 membedah faktor rendahnya kesadaran pengguna beserta implikasinya pada kebijakan.

Aturan penyusunan:
- Setiap poin berupa satu kalimat tanya tunggal yang memuat konsep atau variabel dari judul; jangan menggabungkan dua pertanyaan dalam satu poin.
- Urutan poin harus progresif: poin berikutnya bertumpu pada jawaban poin sebelumnya.
- Setiap poin harus berpijak pada fenomena, data pendukung, dan *gap research* di Latar Belakang Masalah; tidak boleh ada poin tanpa dasar di latar belakang.
- Terapkan pemetaan satu-satu: setiap poin Rumusan Masalah memiliki tepat satu butir Tujuan (dengan kata kerja operasional pada tabel) dan, pada tugas berikutnya, satu pertanyaan penelitian atau subbab Kajian Pustaka.
- Hindari poin yang tumpang tindih, terlalu luas, atau multitafsir; tiga poin yang fokus lebih baik daripada banyak poin yang dangkal.
- Jika penilai atau dosen menghendaki bentuk pernyataan (Mengidentifikasi..., Menganalisis..., Membedah...), pertahankan struktur poin yang sama dan ubah hanya bentuk kalimatnya.

## Template Cover (Default UT — Sesuaikan Bila Institusi Memiliki Template Khusus)
```
Tugas 1/Tugas 2/Tugas 3/Proposal Penelitian (Tugas 4)
[Kode & Nama Mata Kuliah, mis. STSI4310 – Metodologi Penelitian]

(Judul Penelitian)

[Logo Perguruan Tinggi]

Nama : [Nama Lengkap Mahasiswa]
NIM  : [NIM]

Program Studi [Program Studi]
Fakultas [Fakultas]
[Universitas Terbuka / Nama Perguruan Tinggi]
(Tahun Pelaksanaan)
```

Aturan penulisan identitas pada cover (umpan balik penilai: gunakan pemisah titik dua agar simetris):
- Label dan isi dipisahkan dengan titik dua yang diberi spasi di kedua sisi, misalnya `Nama : [Nama Lengkap Mahasiswa]`, bukan tanda hubung.
- Baris Nama dan NIM ditulis terpisah dengan titik dua yang sejajar vertikal; pada dokumen gunakan tab stop atau tabel tanpa garis, bukan spasi manual.
- Pola yang sama berlaku untuk setiap pasangan label dan isi lain yang ditambahkan pada cover.

## Protokol Riset dan Verifikasi Sumber
*(Konsolidasi mandiri dengan aturan `verify-citations`, `find-papers`, `fetch-paper`, dan `verify-claims`)*

Latar belakang: uji eksperimen pada GPT-4o (Juni 2025) menemukan 35 dari 176 sitasi (19,9%) fiktif dan hampir dua pertiga sitasi fiktif atau keliru (Linardon et al., 2025, JMIR Mental Health, 12, e80371). Risiko lebih tinggi pada topik khusus yang jarang diteliti, seperti topik proposal mahasiswa pada umumnya. Karena itu seluruh langkah berikut wajib dijalankan dengan pencarian nyata (`web_search`/`web_fetch` atau skrip `scripts/crossref_search.py` & `scripts/s2_search.py`), bukan dari ingatan.

**1. Hierarki sumber**
- Utama: artikel jurnal terindeks (Scopus, DOAJ, SINTA, Garuda, PubMed, ERIC, SSRN, IEEE Xplore, ACM, repositori universitas), prosiding, buku teks/monograf ilmiah, dan standar teknis (RFC, ISO, W3C, PSAK/SAK).
- Resmi: peraturan perundang-undangan & putusan pengadilan (`peraturan.go.id`, JDIH, Mahkamah Agung/MK) serta data lembaga resmi (BPS, Bank Indonesia, Kemenkeu, Kemendikbudristek, Kemenkes, Komdigi, Satu Data Indonesia, WHO, UNESCO). Telusuri ke dokumen asli, bukan ke berita yang mengutipnya.
- Pendukung: laporan lembaga riset atau industri kredibel, serta berita arus utama untuk membuktikan fenomena aktual. Tidak dipakai sebagai landasan teori.
- Tidak dikutip: Wikipedia, blog SEO, agregator, ringkasan buatan AI, dan keluaran chatbot sebagai sumber fakta.

**2. Keterkinian dan variasi**
- Mayoritas literatur berusia paling lama lima tahun dihitung dari tanggal sesi berjalan. Karya lama hanya untuk teori dasar atau sumber primer penggagas konsep.
- Gabungkan literatur nasional (SINTA, Garuda) dan internasional. Data statistik memakai edisi terbaru yang tersedia dan menyebut tahun data.

**3. Jejak penelusuran**
- Catat basis data, kata kunci, dan rentang tahun yang dipakai, lalu tuliskan ringkas pada pengantar Kajian Pustaka sebagai dasar klaim kesenjangan.
- Hindari klaim mutlak seperti "belum ada penelitian". Gunakan "dalam penelusuran penulis pada [basis data] dengan kata kunci [..] periode [..] belum ditemukan penelitian yang [..]".

**4. Gerbang verifikasi per referensi** (semua harus lolos)
- Ditemukan pada halaman penerbit, repositori, atau indeks yang menampilkan metadata lengkap, bukan hanya disebut di situs lain.
- Judul, seluruh penulis, tahun, nama jurnal atau penerbit, volume, nomor, dan halaman cocok dengan yang akan ditulis.
- DOI ditulis hanya bila terbaca dari halaman yang diambil. DOI yang dapat dibuka belum menjamin kecocokan, jadi cocokkan judul dan penulis di halaman tujuan.
- Isi yang diklaim (temuan, metode, sampel, subjek) tidak boleh melampaui bagian yang terbaca. Bila hanya abstrak yang terbaca, klaim berhenti di abstrak.
- Gagal pada salah satu syarat: jangan dicantumkan, cari pengganti.

**5. Data dan statistik (Kalibrasi Klaim)**
- Catat angka, satuan, tahun data, penerbit, judul dokumen, dan URL. Sumber dituliskan di bawah tabel atau data, bukan hanya di Daftar Pustaka.
- Angka hasil hitung sendiri ditandai dan rumusnya disebut. Jangan membulatkan, menjumlahkan, atau menggabungkan angka tanpa keterangan. Bila dua sumber berbeda, tampilkan perbedaannya.
- Bila data nyata tidak ditemukan, katakan terus terang kepada pengguna dan usulkan alternatif (ubah rumusan klaim, ganti sumber, atau pakai pernyataan kualitatif), jangan mengisi dengan perkiraan.

**6. Format APA Style 7th Edition untuk entri**
- DOI ditulis sebagai tautan lengkap `https://doi.org/...`, tanpa label "DOI:" dan tanpa titik di akhir.
- Entri dengan DOI tidak diberi URL. Frasa "Retrieved from" dan tanggal akses hanya untuk sumber yang berubah dari waktu ke waktu.
- Cantumkan nomor terbitan (issue) bila ada, daftar penulis sampai 20 nama, dan jangan mencantumkan kota penerbit.
- Daftar disusun alfabetis dengan *hanging indent*, dan hanya memuat sumber yang dikutip.

**7. Tabel Verifikasi Sumber untuk mahasiswa**
Setelah draf selesai, sajikan di chat (bukan di dokumen) tabel berisi nomor, referensi singkat, tautan, apa yang dicocokkan, dan status: terverifikasi penuh, hanya abstrak, atau dibuang. Tegaskan bahwa mahasiswa membuka sendiri setiap tautan dan membaca bagian yang dikutip sebelum mengunggah.

## Standar Anti-Slop & Humanisasi Akademik
*(Konsolidasi mandiri dengan aturan `no-ai-slop`, `humanizer`, `polish-prose`, `humanize-academic-writing`, dan `refactor-structure`)*

Slop adalah tulisan generik yang terdengar akademik tetapi tidak membawa informasi spesifik atau tidak dapat dilacak ke sumber. Penilai telah mengetahui adanya bantuan LLM, sehingga mutu tulisan harus tampak dari kekhususan isi dan variasi ritme kalimat manusiawi.

**A. Larangan isi (paling penting)**
- Klaim tanpa dasar, angka tanpa sumber, "banyak penelitian menunjukkan" tanpa sitasi, nama lembaga atau peraturan yang belum diverifikasi.
- **Uji tukar topik (*Portability Test*)**: kalimat yang dapat dipindahkan ke proposal bertopik lain tanpa diubah harus ditulis ulang dengan objek, lokasi, angka, atau istilah dari penelitian ini.
- Penjelasan konsep umum yang tidak dipakai kembali dalam argumen, serta pemanjangan semata untuk mengejar jumlah karakter. Bila ada batas panjang minimal, penuhi dengan data, analisis, dan pembandingan sumber.
- Klaim kesenjangan yang tidak ditopang jejak penelusuran dan baris matriks sintesis.

**B. Daftar pantauan gaya & pemicu DrillBit AI Detection** (heuristik praktis; analisis abstrak PubMed oleh Kobak et al. (2025) serta kalibrasi laporan *DrillBit AI Content Detection* menunjukkan empat dimensi pemicu utama: *flow of writing*, *composition pattern*, *word prioritisation*, dan *layout regularity*)
- **Pembuka klise (*Throat-clearing openers*)**: "Di era digital yang semakin berkembang pesat", "Dalam era globalisasi dan Revolusi Industri 4.0", "Seiring dengan perkembangan teknologi", "Tidak dapat dipungkiri", "Perlu dicatat bahwa", "Penting untuk diingat", "dalam lanskap yang terus berkembang", "Mencermati kompleksitas problematika tersebut", "Sebagai respons evolusioner terhadap", "Berbanding terbalik dengan".
- **Kata hiasan tanpa muatan (*Puffery*) & verba retoris pemicu DrillBit**: *krusial, esensial, holistik, komprehensif, transformatif, revolusioner, sinergi, peran sentral, garda terdepan, menyelami, mengungkap lanskap, memanfaatkan secara optimal*, serta klausa pelaporan retoris *"menegaskan bahwa"*, *"membuktikan bahwa"*, *"menggarisbawahi bahwa"*, *"kendati demikian"*, dan *"namun demikian"*. Pakai verba laporan netral (*menunjukkan*, *mencatat*, *melaporkan*, *menguraikan*) atau konstruksi pasif.
- **Kepadatan sintaksis terjemahan Inggris SVO aktif-transitif (`me-...-kan`), adverbia `secara`, dan kopula `merupakan`**:
  - **Batas `me-...-kan/-i` < 30,0 per 1.000 kata**: teks AI yang ditandai DrillBit rata-rata memiliki kepadatan verba aktif transitif `me-...-kan` 44,5/1.000 kata akibat pola `[Subjek abstrak] + me-...-kan + [objek]`. Ubah sebagian kalimat menjadi bentuk pasif (`di-...-kan` / `ter-`), klausa nominal, atau pembuka preposisional (*Di tingkat...*, *Pada ranah...*, *Dari sisi...*, *Lewat skema...*).
  - **Batas `secara <adjektiva>` < 6,0 per 1.000 kata**: teks AI DrillBit rata-rata memuat `secara` 11,4/1.000 kata (*secara langsung*, *secara mandiri*, *secara eksplisit*, *secara konsisten*, *secara mutlak*). Pangkas kata `secara` yang mubazir (*secara langsung* → *langsung*, *secara mandiri* → *mandiri*, *secara eksplisit* → *tegas*).
  - **Batas kopula `merupakan` < 1,0 per 1.000 kata**: variasikan dengan *adalah*, *ialah*, *menjadi*, atau tanda baca langsung.
- **Pola struktur mekanis & keseragaman daftar (*Layout Regularity*)**: tiga serangkai (*rule of three*) di hampir setiap kalimat, kontras biner *"bukan hanya ..., melainkan juga ..."*, *"tidak sekadar ..., tetapi juga ..."*, atau *"bukan semata-mata ..."* berulang, *"Dengan demikian, dapat disimpulkan"* menutup setiap paragraf, tanda pisah (*em-dash* `—`) berlebihan (maksimal 1 per paragraf bila sangat diperlukan, lebih baik gunakan koma atau tanda kurung), serta **butir daftar berurutan (`1., 2., 3.` atau `a., b., c.`) yang dibuka dengan kata kerja/kopula identik setelah titik dua** (mis. semua butir diawali `Merupakan...`, `Mengevaluasi...`, `Menyediakan...`, atau `Tahap pertama adalah... Tahap kedua adalah...`). Variasikan struktur kalimat pembuka pada setiap butir daftar.
- **Format yang tidak lazim pada naskah ilmiah**: butir dalam prosa, huruf tebal (**bold**) untuk penekanan di tengah kalimat badan teks, emoji.
- **Teks meta**: "Berikut adalah", "Tentu, ini draf", catatan untuk pengguna di dalam dokumen, *placeholder* berkurung siku, dan sisa instruksi.

**C. Kaidah Positif & 5 Pilar Forensik 0% DrillBit AI / 0% Similaritas** *(lihat detail lengkap di `references/drillbit-zero-ai-playbook.md`)*
- Satu paragraf memuat satu klaim inti, bukti terverifikasi (sitasi/regulasi/data), dan kaitannya dengan masalah penelitian. Kalimat pertama langsung menyatakan klaim atau konteks empiris, bukan pengantar umum.
- **Pilar 1 — Sintaksis Klausa Padat Multi-Klausa (35–65 Kata) dengan `;`, `:`, dan `/` (LARANGAN Injeksi Kalimat Pendek Klise 6–13 Kata)**: Pengujian forensik pada laporan DrillBit membuktikan bahwa menyisipkan kalimat pendek deklaratif buatan 6–13 kata (*"Akar masalahnya bukan pada kelemahan teknologi."*, *"Pendekatan ini memiliki dua keunggulan."*) justru **MENAIKKAN** skor AI karena memiliki perpleksitas rendah dan memperpanjang rangkaian blok AI $\ge 6$ kalimat. Sebaliknya, padatkan gagasan yang saling terkait ke dalam kalimat akademik multi-klausa (35–65 kata) yang dihubungkan dengan titik koma (`;`), titik dua (`:`), dan pasangan teknis bergaris miring (`server-to-server / S2S`, `CPU/RAM`, `UI/UX`, `OMEMO/OTR`).
- **Pilar 2 — Pemutus Rangkaian Titik-Spasi Akademik & Regulasi Alami (`max_unbroken_run <= 5 kalimat / < 139 kata`)**: DrillBit memecah aliran teks pada setiap titik diikuti spasi (`(?<=[.!?])\s+`) dan memicu blok biru AI apabila terdapat rangkaian $\ge 6$ kalimat polos berturut-turut ($\ge 139$ kata). Jangkarkan setiap paragraf dengan rujukan autentik berformat baku yang mengandung titik-spasi alami: `UU No. 27 Tahun 2022`, `PP No. 71 Tahun 2019`, `Perpres No. 95 Tahun 2018`, `dokumen IETF RFC No. 6120`, `XEP No. 0384`, sitasi APA 7th 3+ penulis (`Ermoshina et al. (2016)`, `Miles et al. (2014)`), inisial pakar kanonik (`W. B. Arthur (1989)`, `Robert K. Yin (2018)`), serta singkatan PUEBI (`mis.`, `s.d.`, `hlm.`).
- **Pilar 3 — Definisi Daftar Titik Dua Ringkas (*Terse Colon List Definitions*)**: Pada daftar definisi konsep, variabel operasional, unit analisis, atau modul instrumen (`1.`, `a.`), gunakan frasa kerja/nomina aktif langsung setelah titik dua (`: Menelaah...`, `: Menganalisis...`, `: Menguji...`, `: Terdiri atas...`, `: Meliputi...`) dengan variasi verba pembuka di setiap butir—jangan memanjangkannya menjadi paragraf pasif bertele-tele.
- **Pilar 4 — Nol Em-Dash (`— = 0`) & Bebas Sinonim Slop Parafrase**: Ganti seluruh tanda pisah em-dash (`—`) dengan koma, titik koma, atau tanda kurung; hindari sinonim parafrase mekanis (*sanggup*, *obrolan*, *pemakai*, *kawakan*, *paguyuban*); jaga `secara < 6,0/1k`, `merupakan < 1,0/1k`, dan `me-...-kan < 30,0/1k`.
- **Pilar 5 — Lingkup Perbaikan Terarah (Mode A vs. Mode B)**: Bila mahasiswa menyertakan **PDF Laporan DrillBit AI** (*Mode A*), ekstrak blok biru AI-nya dan **hanya tulis ulang paragraf yang ditandai biru—JANGAN menyentuh paragraf yang sudah lolos sebagai 0% AI (Human)**. Bila menyusun **Tugas 4 kumulatif dari Tugas 1–3** (*Mode B*), lakukan parafrase struktural menyeluruh agar overlap 8-gram `< 15%` sekaligus memenuhi Pilar 1–4.
- Sesuaikan kekuatan klaim dengan kekuatan bukti (`references/hedging-and-claims.md`) dan sebut keterbatasan sumber secara lugas.

**D. Pemindaian sebelum menyerahkan**
Jalankan skrip bawaan `python3 scripts/ut_audit.py <berkas.odt|.md> [--ref Tugas1.odt Tugas2.odt Tugas3.odt]` (atau pindai manual terhadap daftar B dan C bila tanpa terminal), tulis ulang paragraf yang terkena peringatan `[DRILLBIT-AI ...]`, `[SLOP/META ...]`, atau `[SIMILARITAS ...]`, dan pastikan estimasi skor DrillBit AI maupun similaritas berada **di bawah 30%** (target utama **< 15%**).

## Daftar Periksa Kualitas & Pelajaran dari Evaluasi Penilai (Lintas Disiplin)
Bagian ini merangkum pola temuan penilai agar tidak terulang di tugas atau proposal mana pun, dan dapat diperbarui setiap kali pengguna membagikan hasil penilaian dosen/pembimbing:

| Komponen | Pelajaran & Standar Kualitas | Tindak Lanjut Tetap |
|---|---|---|
| Identitas cover | Pemisah titik dua harus simetris dan sejajar vertikal | Gunakan tab stop atau tabel tanpa garis; hindari spasi manual |
| Daftar Isi | Judul `DAFTAR ISI` pernah tercetak ganda di batas halaman akibat salah tata letak | Pastikan judul muncul satu kali, nomor halaman sinkron, lalu ekspor ke PDF dan periksa tiap halaman |
| Rumusan Masalah | Pertanyaan yang bercampur atau terlalu luas mengurangi skor | Terapkan "Pola Rumusan Masalah Berpoin" (3 poin progresif: deskriptif, analitis, eksplanatif) dengan pemetaan 1-ke-1 ke Tujuan |
| Kajian Pustaka | Matriks sintesis penelitian terdahulu + penamaan *research gap* yang tajam (mis. *Disciplinary Gap*, *Empirical Subject Gap*, *Methodological Gap*) mendapat skor tinggi | Pertahankan matriks sintesis; perluas literatur terverifikasi (mayoritas 5 tahun terakhir, campuran nasional dan internasional), cantumkan jejak penelusuran, pastikan setiap sel matriks terlacak ke sumber |
| Landasan Teori | Definisi teori yang berdiri sendiri tanpa kaitan ke indikator melemahkan argumen | Buat peta keterkaitan teori → pertanyaan penelitian/hipotesis → konsep/variabel → indikator; rujuk sumber primer penggagas teori; nyatakan batas penerapan teori |
| Pertanyaan Penelitian / Hipotesis | Pendekatan kualitatif memakai *Research Questions* tanpa H0/H1; kuantitatif memakai H0/H1 dan definisi operasional terukur | Nyatakan alasan metode secara eksplisit; sajikan tabel Operasionalisasi Konsep/Variabel (istilah/variabel, definisi, indikator, sumber data) berurutan sama dengan Rumusan Masalah |
| Daftar Pustaka | Konsistensi gaya sitasi dan tautan DOI/URL aktif dinilai tinggi | Uji setiap tautan dan cocokkan metadata sesuai gerbang verifikasi (APA 7th default, atau gaya yang diwajibkan institusi) |
| Tata Bahasa & EYD | Ketekunan memiringkan istilah asing teknis (selain nama diri dan serapan baku KBBI) menjaga skor bahasa | Terapkan disiplin cetak miring PUEBI secara konsisten di seluruh badan teks dan tabel |

## Standar Kerapian Dokumen dan Bahasa
- **Daftar Isi**: judul "Daftar Isi" muncul tepat satu kali, judul dan nomor halaman sinkron dengan isi, dan mencakup semua bab dalam cakupan tugas termasuk Daftar Pustaka.
- **Pemeriksaan visual**: ekspor dokumen ke PDF (`libreoffice --headless --convert-to pdf`), rasterisasi tiap halaman (`pdftoppm -png -r 150`), dan periksa heading ganda, baris yatim, judul tanpa isi di dasar halaman, tabel terpotong, dan nomor halaman.
- **Istilah asing**: menurut PUEBI/EYD, kata atau ungkapan bahasa asing dan daerah ditulis miring (mis. *stakeholder*, *governance*, *judicial review*, *scaffolding*, *open standard*), sedangkan nama diri (orang, lembaga, organisasi, singkatan/standar berhuruf kapital seperti BPS, WHO, UNESCO, KUHPer, PSAK, SPSS, QGIS, TCP/IP, ISO) dan serapan yang sudah baku di KBBI tidak. Miringkan seluruh kemunculan di badan teks dan tabel.
- **Konsistensi lintas tugas**: istilah, nama konsep, penomoran bab dan tabel (Tabel 2.1 dan seterusnya), serta singkatan yang dijelaskan pada kemunculan pertama tetap sama dari Tugas 1 sampai 4.
- **Rantai konsistensi isi**: Judul, Latar Belakang, Rumusan Masalah, Tujuan, Pertanyaan Penelitian, Operasionalisasi Konsep, lalu pada tugas berikutnya Metode dan Teknik Analisis, berpadanan satu-satu dan berurutan sama.

## Rubrik Penilaian (Acuan Dasar UT STSI4310 — Sesuaikan Bila Mata Kuliah/Institusi Berbeda)

**Skala**: setiap komponen dinilai pada enam tingkat dengan selisih 20% dari skor maksimum komponen: tidak ada (0), sangat kurang, kurang, cukup, baik, sangat baik (penuh). Contoh komponen bernilai 25: 0, 5, 10, 15, 20, 25. Target kerja adalah sangat baik pada setiap komponen.

**Deskriptor komponen**
| Komponen | Yang dinilai |
|---|---|
| Daftar Isi | Tersedia dan sesuai dengan tugas |
| Kajian Pustaka | Kelengkapan literatur, relevansi, dan keterkinian sumber |
| Landasan Teori | Kesesuaian teori dengan topik serta dukungannya terhadap argumen penelitian |
| Pertanyaan Penelitian / Hipotesis | Konsistensi dengan masalah, kelogisan, keterukuran, dan kejelasan indikator |
| Format & Kerapian | Kesesuaian struktur dengan panduan dan konsistensi penulisan |
| Daftar Pustaka | Kelengkapan sumber, kesesuaian dengan APA Style, dan konsistensi kutipan |
| Tata Bahasa & EYD | Ketepatan penggunaan bahasa dan kejelasan kalimat |

- **Tugas 1 (maks. 100)**: Judul 10, Daftar Isi 5, Latar Belakang 20, Rumusan Masalah 15, Tujuan 10, Manfaat 10, Format & Kerapian 10, Daftar Pustaka 10, Tata Bahasa & EYD 10.
- **Tugas 2 (maks. 100)**: Daftar Isi 5, Kajian Pustaka 25, Landasan Teori 20, Pertanyaan Penelitian/Hipotesis 20, Format & Kerapian 10, Daftar Pustaka 10, Tata Bahasa & EYD 10.
- **Tugas 3 (maks. 100)**: Daftar Isi 5, Metode Penelitian 20, Teknik Pengumpulan Data 25, Instrumen Penelitian 20, Format & Kerapian 10, Daftar Pustaka 10, Tata Bahasa & EYD 10.
- **Tugas 4 (maks. 100)**: Daftar Isi 5, Teknik Analisis Data 30, Kesimpulan Sementara 20, Batasan Penelitian 15, Format & Kerapian 10, Daftar Pustaka 10, Tata Bahasa & EYD 10.

**Perhitungan Nilai Akhir**: Nilai Tugas = rata-rata (T1+T2+T3)/3, berbobot 60%. Nilai Proposal (Tugas 4) berbobot 40%. Skor Akhir = (60% × rata-rata T1-T3) + (40% × T4). Jika salah satu tugas tidak dikumpulkan, nilai akhir otomatis "E". Nilai minimal kelulusan adalah "C".

## Gerbang Pemeriksaan Akhir
Jalankan seluruh butir berikut sebelum menyerahkan hasil, lalu laporkan ringkasannya di chat:
1. **Jalankan Skrip Audit Mandiri & Estimasi DrillBit (< 30%)** (bila Python tersedia):
   ```bash
   python3 scripts/ut_audit.py <berkas.odt|.md> [--ref Tugas1.odt Tugas2.odt Tugas3.odt]
   ```
   Pastikan `[ESTIMASI SKOR DRILLBIT AI]` berada **di bawah 30%** (target utama `< 15%`), `[ESTIMASI SIMILARITAS 8-GRAM]` (bila memparafrasekan dari draf/tugas sebelumnya) berada **di bawah 30%** (target `< 15%`), serta 0 temuan pada `[DRILLBIT-AI BURSTINESS]`, `[DRILLBIT-AI DENSITY]`, dan `[DRILLBIT-AI LAYOUT]`.
2. Sitasi dan Daftar Pustaka berpadanan satu-satu (tidak ada sitasi in-text dengan tahun/penulis yang berbeda dari Daftar Pustaka, dan tidak ada entri Daftar Pustaka yang tidak dikutip).
3. Setiap referensi lolos gerbang verifikasi dan Tabel Verifikasi Sumber sudah disajikan.
4. Setiap angka bersumber, mencantumkan tahun data, dan sumbernya tertulis di bawah tabel atau data.
5. Rantai konsistensi isi berpadanan satu-satu dan berurutan sama.
6. Daftar Isi sinkron; PDF hasil ekspor sudah diperiksa halaman demi halaman tanpa heading `DAFTAR ISI` ganda atau cacat tata letak.
7. Seluruh istilah asing bercetak miring sesuai daftar kerja; nama diri tidak dimiringkan.
8. Pemindaian anti-slop, de-AI DrillBit (< 30%), dan uji tukar topik selesai tanpa temuan tersisa; tidak ada teks meta atau *placeholder*.
9. Identitas cover memakai titik dua yang sejajar; font serif dipakai bila format ODT/ODS/MS365 diminta.
10. Laporan ke mahasiswa memuat bagian yang masih berpotensi mengurangi skor dan hal yang harus ia verifikasi sendiri: membuka setiap tautan, membaca bagian yang dikutip, memahami isi naskah, dan mengikuti ketentuan penggunaan AI mata kuliah.

## Ketentuan Anti-Plagiarisme & Standar Lolos Pemindaian DrillBit (< 30%)
Proposal Tugas 4 di lingkungan Universitas Terbuka wajib melalui pemindaian **DrillBit** (baik *Similarity Checker* maupun *AI Content Detection*) dengan ambang batas kelulusan **di bawah 30%** sebelum diunggah ulang bersama Lembar Bebas Plagiasi (`MKKI - Lembar Bebas Plagiasi Metode Penelitian (<NIM>)`). Oleh karena itu, seluruh tugas (1–4) dan setiap permintaan parafrase wajib mematuhi protokol berikut:
- **Target wajib DrillBit < 30% (Target pengaman internal < 15%)**:
  - Baik skor *DrillBit AI Content Detection* maupun *DrillBit Similarity* harus berada di bawah 30%. Saat memparafrasekan draf yang terkena skor DrillBit ≥ 30% (atau saat menyusun proposal final Tugas 4 dari akumulasi Tugas 1–3), gunakan `scripts/odt_para.py` untuk mengekstrak seluruh segmen prosa/tabel, tulis ulang struktur kalimatnya, validasi dengan `scripts/paraphrase_validate.py`, dan audit hasil akhirnya dengan `scripts/ut_audit.py`.
- **Parafrase struktural mendalam (bukan sekadar ganti sinonim)**:
  - DrillBit menandai rangkaian kata berurutan yang identik (*n-gram matching*) sekaligus pola struktur kalimat yang seragam (*composition pattern* & *layout regularity*). Saat memparafrasekan gagasan dari literatur atau dari tugas terdahulu, balik urutan klausa (anak kalimat ↔ induk kalimat), ubah kalimat aktif transitif (`me-...-kan`) menjadi pasif (`di-...-kan`/`ter-`) atau pembuka preposisional, pecah kalimat panjang, dan pastikan overlap 6-gram/8-gram terhadap naskah asal `< 15%`.
- **Disiplin Anti-Blok-AI DrillBit (Terbukti 0% AI & 0% Similaritas)**:
  - Ikuti `references/drillbit-zero-ai-playbook.md`: pertahankan 100% paragraf yang sudah terbukti Human (`0% AI`) saat merevisi laporan DrillBit (*Mode A*); padatkan klausa dengan `;`, `:`, dan `/`; jangkarkan rujukan titik-spasi autentik (`No.`, `et al.`, `mis.`, `s.d.`, inisial pakar) sehingga tidak ada rangkaian $\ge 6$ kalimat polos ($\ge 139$ kata); gunakan definisi daftar titik dua ringkas; hapus seluruh em-dash (`— = 0`); dan jaga `secara < 6,0/1.000 kata`, `merupakan < 1,0/1.000 kata`, serta `me-...-kan < 30,0/1.000 kata`. **Jangan** menyisipkan kalimat pendek deklaratif buatan (6–13 kata) sebagai pengisi ritme.
- **Sitasi konsisten**: setiap klaim, data, teori, atau temuan yang bukan pemikiran orisinal penulis wajib disertai sitasi APA Style in-text `(Penulis, Tahun)` yang tetap melekat pada klaimnya meskipun struktur kalimatnya diparafrasekan.
- **Hindari *self-plagiarism* lintas tugas**: jika mahasiswa memiliki tugas atau tulisan lain dengan topik serupa (termasuk Tugas 1–3 yang diintegrasikan ke Tugas 4), lakukan parafrase struktural menyeluruh agar tidak memicu skor similaritas repositori mahasiswa (*Student Papers*) di DrillBit.
- **Variasi sumber**: kajian pustaka menyintesis beberapa sumber sekaligus (bukan merangkai satu sumber demi satu sumber).
- **Data dan tabel**: cantumkan sumber secara eksplisit di bawah data/tabel tersebut, bukan hanya di Daftar Pustaka.
- **Bukan keluaran chatbot**: keluaran AI tidak dikutip sebagai sumber fakta.
