---
name: "penjawab-tugas-akademik-ut"
description: Skill mandiri (zero-dependency) untuk menyusun, mengaudit, dan memformat jawaban tugas tutorial (Tugas 1-3), diskusi Tuton/LMS, laporan praktikum, analisis kasus, dan panduan video demonstrasi di seluruh fakultas Universitas Terbuka (FST, FEB, FHISIP, FKIP, Pascasarjana) maupun perguruan tinggi lain (mencakup rumpun Sains & Teknologi, Ekonomi & Bisnis, Hukum & Ilmu Sosial-Politik, Keguruan & Pendidikan, serta Kesehatan/Humaniora) dengan gaya akademik manusiawi (humanized), bebas AI slop (deslopified), verifikasi klaim dan sitasi nyata, kepatuhan etika penggunaan AI (Pertor UT No. 436/2025 & Panduan GenAI Diktiristek), serta adaptasi dinamis antara mesin lokal (CLI) dan AI/LLM di web (Claude Web, Gemini Web, dll). Menjalankan kode pintas B1E2P3-KODEMK (khusus diskusi), A1B2C3-KODEMK (khusus tugas esai 1/2/3), dan A2B4C6-KODEMK (khusus tugas praktikum / laporan proyek / studi kasus). Untuk proposal penelitian (mis. STSI4310 atau mata kuliah metodologi penelitian), gunakan skill `metodologi-penelitian-univterbuka`.
---

# Penjawab Tugas Akademik & Laporan Praktikum UT (Self-Contained, Local + Web)

Skill ini memandu penyusunan, revisi, verifikasi literatur, dan pemformatan dokumen untuk seluruh tugas kuliah reguler, diskusi Tuton, serta laporan praktikum teknis Universitas Terbuka (UT) maupun perguruan tinggi lain. Seluruh aturan *deslopification*, *academic humanization*, verifikasi sitasi/klaim, restrukturisasi argumen, kepatuhan etika AI, dan penyusunan naskah video telah **diintegrasikan langsung di dalam skill ini beserta skrip bawaannya (`scripts/` dan `references/`)**, sehingga **tidak memerlukan ketergantungan pada skill eksternal** dan dapat dijalankan baik di **mesin lokal (CLI)** maupun di **AI/LLM berbasis web (Claude Web, Gemini Web, dll)**.

> **Batas Cakupan (Zero Conflict Rule):**
> - Gunakan skill ini untuk **Tugas 1–3 mata kuliah reguler/berpraktik, Diskusi Tuton/LMS, Laporan Praktikum/Proyek/Kasus, dan Skrip Video Demonstrasi** di seluruh fakultas UT (FST, FEB, FHISIP, FKIP, Pascasarjana) maupun perguruan tinggi lain.
> - Bila pengguna mengetik kode pintas `B1E2P3-<KODE_MK>`, `A1B2C3-<KODE_MK>`, atau `A2B4C6-<KODE_MK>`, jalankan perintah tersimpan pada **Bagian 4** terlebih dahulu; aturan Bagian 4 mengatur batas karakter, struktur artefak, dan format keluaran sesuai peruntukan masing-masing kode.
> - Khusus untuk penyusunan **Proposal Penelitian Bab I–IV/V** (mata kuliah Metodologi Penelitian, Karya Ilmiah/Karil, atau Tugas Akhir seperti `STSI4310`, `MSIM4312`, `EKMA4367`, `HKUM4306`, `IDIK4007`, dll.), gunakan skill `metodologi-penelitian-univterbuka`.

---

## 0. Prinsip Utama & Kepatuhan Etika Penggunaan AI (UT & Perguruan Tinggi)

Skill ini wajib mengikuti ketentuan penggunaan Kecerdasan Artifisial Generatif (GenAI) di lingkungan Universitas Terbuka (**Peraturan Rektor UT Nomor 436 Tahun 2025** tentang Kode Etik Sivitas Akademika, Tenaga Kependidikan, dan Pendidik Eksternal) serta pedoman akademik nasional (**Panduan Penggunaan Generative Artificial Intelligence pada Pembelajaran di Perguruan Tinggi**, Ditjen Diktiristek Kemendikbudristek, 2024) dan etika AI UNESCO:

1. **AI sebagai Mitra Belajar (*Copilot*), Bukan Penulis Pengganti**:
   - **Boleh dibantu AI**: merapikan struktur, menyunting tata bahasa Indonesia baku (EYD/PUEBI) dan istilah asing, memformat sitasi APA dari metadata terverifikasi, memverifikasi perhitungan/skrip, menyusun draf awal berbasis poin pikiran atau artefak praktikum milik mahasiswa, serta memeriksa cacat teknis dokumen.
   - **Wajib dari mahasiswa & sumber nyata**: pemahaman konsep inti, keputusan analisis/desain, seluruh artefak praktikum nyata (`.pkt`, skrip, proyek QGIS, log terminal), serta fakta, angka, regulasi, dan referensi terverifikasi. Dilarang menyerahkan keluaran AI mentah tanpa telaah kritis dan penyuntingan mandiri (*AI-giarism*).
2. **Larangan Fabrikasi & Kepatuhan Artefak Nyata**:
   - Dilarang mengarang output perintah CLI, hasil `ping`, tangkapan layar, data statistik, atau sitasi. Jika suatu artefak praktikum belum dijalankan atau datanya belum tersedia, nyatakan secara jujur dan pandu mahasiswa menjalankannya terlebih dahulu.
3. **Transparansi & Deklarasi Penggunaan AI**:
   - Apabila mata kuliah, tutor, atau perguruan tinggi mewajibkan pernyataan penggunaan AI, bantu menyusun deklarasi yang jujur (alat yang dipakai, tujuan pemanfaatan, serta penegasan bahwa substansi, artefak, dan verifikasi dilakukan oleh mahasiswa). AI **tidak boleh** dicantumkan sebagai penulis di dalam Daftar Pustaka.
4. **Privasi & Perlindungan Data Pribadi**:
   - Jangan menyimpan data pribadi nyata (nama asli, NIM, email, alamat, atau data rahasia instansi studi kasus) di dalam berkas skill maupun mengunggahnya ke layanan AI publik tanpa anonimisasi. Gunakan *placeholder* saat menyusun draf dan lengkapi identitas secara lokal sebelum pengumpulan.
5. **Tujuan Anti-Slop & Kepatuhan Aturan Khusus**:
   - Standar anti-slop dan humanisasi diterapkan demi kejelasan, kekhususan argumen, dan mutu akademik—**bukan** untuk mengakali alat deteksi plagiarisme/AI. Jika suatu ujian (mis. UAS/THE/TMK) atau tugas tertentu secara eksplisit melarang penggunaan AI, ikuti aturan yang lebih ketat tersebut.

---

## 1. Adaptasi Dinamis Lingkungan (Mesin Lokal vs. Web LLM)

Deteksi kemampuan lingkungan tempat agen berjalan dan sesuaikan eksekusi secara dinamis berdasarkan permintaan pengguna:

### A. Mode Mesin Lokal
Aktif secara otomatis ketika agen memiliki akses ke terminal/bash atau sistem berkas lokal:
1. **Pembacaan Soal & Berkas Kerja Lokal**:
   - Ekstrak teks PDF soal/modul dengan `pdftotext "<berkas.pdf>" -` atau render halaman PDF yang memuat gambar/topologi dengan `pdftoppm -png -r 150 "<berkas.pdf>" page`.
   - Baca berkas `.docx` atau `.odt` melalui modul Python standar (`zipfile` + `xml.etree.ElementTree` / `lxml`).
   - Periksa berkas topologi Cisco Packet Tracer 9 (`.pkt` / `.pka`) menggunakan skrip bawaan `python3 scripts/pt9.py info <berkas.pkt>` atau `decode <berkas.pkt> -o topology.xml`.
2. **Eksekusi Perhitungan, Skrip, & Audit Lokal**:
   - Jalankan perhitungan kuantitatif (mis. Location Quotient, proyeksi penduduk geometrik/eksponensial, subnetting VLSM) menggunakan `python3` dan simpan skripnya bila diminta (mis. `T3-STPL4211-<NIM>.py`).
   - Jalankan skrip audit mandiri di folder `scripts/` sebelum menyerahkan hasil.
3. **Kompilasi Dokumen & Pemeriksaan Visual Lokal**:
   - Konversi `.odt` atau `.docx` ke `.pdf` dengan `libreoffice --headless --convert-to pdf <berkas>`.
   - Bila memodifikasi `.odt` secara terprogram (via `zipfile` + `content.xml`), gunakan gaya karakter `T_Italic` (`fo:font-style="italic"`) untuk setiap istilah asing dan gunakan font serif (Times New Roman / Liberation Serif).
   - Render PDF hasil akhir dengan `pdftoppm -png -r 150 <berkas.pdf> /tmp/page_check` untuk memastikan tidak ada tabel terpotong atau cacat tata letak.

### B. Mode Web AI/LLM (Claude Web, Gemini Web, dll)
Aktif ketika skill diunggah sebagai `.zip`/`.skill` atau `SKILL.md` di antarmuka web:
1. Gunakan fitur **Web Search / Web Fetch** bawaan platform untuk memverifikasi referensi jurnal, DOI, regulasi, dan data BPS terbaru.
2. Bila pengguna mengunggah berkas soal (`.pdf`, `.docx`, `.csv`), baca langsung dari lampiran percakapan.
3. Bila lingkungan web menyediakan *Python sandbox / Code Execution*, jalankan skrip bawaan (`scripts/ut_audit.py`) di dalam sandbox; bila tidak tersedia, jalankan seluruh daftar periksa secara manual baris demi baris sebelum menampilkan jawaban.

---

## 2. Identitas Mahasiswa & Konvensi Penamaan Berkas

Jangan menyimpan data pribadi nyata secara permanen di dalam skill. Gunakan profil mahasiswa yang diberikan pengguna pada sesi berjalan (atau *placeholder* berikut bila belum diberikan) pada *header* jawaban, halaman sampul, skrip perkenalan video, dan nama berkas:

- **Nama Lengkap**: `[Nama Lengkap Mahasiswa]`
- **NIM**: `[NIM]`
- **Program Studi**: `[Program Studi]`
- **Fakultas**: `[Fakultas]`
- **Perguruan Tinggi**: `Universitas Terbuka` (atau nama perguruan tinggi sesuai input pengguna; konteks studi kasus wilayah disesuaikan dengan input pengguna apabila soal membebaskan pemilihan daerah)

### Format Header Tugas Esai Reguler (Markdown/PDF)

```markdown
# TUGAS [1/2/3] [KODE_MK]

Nama : [Nama Lengkap Mahasiswa]

NIM : [NIM]

---
```

*(Catatan: Jika sub-soal a dan b digabung ke dalam satu paragraf, tambahkan subbagian `## Disclaimer` atau deklarasi penggunaan AI singkat di bawah NIM hanya bila diminta oleh tugas/tutor).*

### Konvensi Penamaan Berkas di direktori kerja tugas (`<direktori-kerja>`)
- **Tugas Reguler / Praktikum**: `T{1|2|3}-{KODE_MK}-{NIM}.{md|pdf|docx|odt|py|pkt|mp4|tar.xz|zip}`

---

## 3. Empat Mode Pengerjaan Dinamis Sesuai Permintaan Pengguna

Pilih mode secara dinamis berdasarkan bentuk soal atau instruksi pengguna:

### Mode A: Jawaban Soal Esai / Diskusi / Tugas Tutorial Reguler
1. **Varian 1 — Integrasi Sub-Soal Satu Paragraf (Batas Karakter Ketat, mis. Maks. 1.400 Karakter)**:
   - Gunakan bila instruksi soal atau pengguna meminta penggabungan sub-soal (*a*, *b*, *c*) ke dalam satu paragraf utuh per nomor soal atau membatasi panjang maksimal (umumnya ≤ 1.400 karakter termasuk spasi dan sitasi in-text).
   - Langsung buka kalimat pertama dengan definisi/klaim inti yang menjawab sub-soal pertama, lalu sambungkan ke sub-soal berikutnya menggunakan transisi logis berbasis mekanisme (bukan kata sambung klise seperti *"Selanjutnya, tidak kalah pentingnya..."*).
   - Pantau jumlah karakter per nomor soal dengan `python3 scripts/ut_audit.py <berkas> --max-chars 1400`.
   - Bila jawaban diminta lewat kode pintas `B1E2P3` atau `A1B2C3`, batas yang berlaku adalah 1.500 karakter dan seluruh ketentuan Bagian 4 menggantikan varian ini.
2. **Varian 2 — Struktur Multi-Bagian & Perhitungan Analitis (Default bila tanpa batas satu paragraf)**:
   - Gunakan subjudul bernomor (`## 1. ...`, `## 2. ...`) yang mencerminkan pokok persoalan.
   - Untuk soal kuantitatif/ekonomi wilayah/algoritma (mis. perhitungan *Location Quotient* [LQ] pada `STPL4211`), sajikan rumus eksplisit, perhitungan per langkah/sektor, tabel ringkasan yang presisi, serta interpretasi teoritis dan implikasi kebijakan nyatanya.

### Mode B: Laporan Tugas Berpraktik / Praktikum / Proyek Lintas Fakultas (Berbasis Artefak Nyata)
Setiap klaim wajib merujuk langsung pada artefak, data, perhitungan, konfigurasi, atau dokumen aktual mahasiswa sesuai rumpun ilmu dan fakultasnya:
1. **Sains, Teknik, & Teknologi Informasi (FST / Fakultas Teknik / Ilmu Komputer)**:
   - *Jaringan Komputer & Infrastruktur*: Uji konfigurasi nyata di **Cisco Packet Tracer** (`.pkt`/`.pka` via `python3 scripts/pt9.py decode <file.pkt>`) atau terminal Linux/Windows (`ip`/`ipconfig`, `ss`/`netstat`, `traceroute`/`tracert`, `dig`/`nslookup`, `ping`). Cantumkan tabel IP, VLAN, CLI, dan hasil uji yang identik 100% dengan berkas/log aktual.
   - *Pemrograman, Basis Data, & Sistem Enterprise*: Lampirkan dan rujuk kode sumber, skema ERD/SQL, atau analisis kerangka kerja (mis. Zachman, TOGAF, EAP, COBIT, ISO/IEC 27001, NIST CSF, UU Hak Cipta, UU ITE, UU PDP) yang terhubung langsung ke studi kasus soal.
   - *Sains Alam, Matematika, & Statistika*: Verifikasi perhitungan numerik, uji statistik, atau simulasi dengan Python/R sebelum menuliskan angka ke dalam laporan.
2. **Perencanaan Wilayah, Kebumian, & Analisis Spasial/Kuantitatif**:
   - *GIS / QGIS*: Rujuk proyek QGIS lokal milik mahasiswa (`.qgz`), layer vektor administrasi, raster DEM, sistem proyeksi UTM setempat, serta hasil pemrosesan (*Clip*, *Slope*, *Aspect*, klasifikasi) sesuai data aktual.
   - *Demografi & Ekonomi Wilayah*: Verifikasi proyeksi penduduk, PDRB, atau *Location Quotient* (LQ) menggunakan skrip Python/spreadsheet sebelum menarasikan angka.
3. **Ekonomi, Manajemen, & Akuntansi (FEB)**:
   - Sajikan rumus eksplisit, kertas kerja/tabel perhitungan (laporan keuangan, rasio likuiditas/profitabilitas, NPV/IRR, akuntansi biaya, ekonometrika), rujukan PSAK/SAK, dan interpretasi manajerial yang ditopang data aktual (BPS, Bank Indonesia, IDX, atau data kasus soal).
4. **Hukum, Ilmu Sosial, Politik, & Komunikasi (FHISIP)**:
   - Untuk analisis kasus hukum, gunakan silogisme hukum (*isu hukum → aturan/peraturan perundang-undangan sesuai hierarki norma → analisis fakta → kesimpulan*) dengan merujuk pasal dan nomor peraturan yang terverifikasi (UU, PP, Perpres, Putusan MA/MK). Untuk kebijakan publik, sosiologi, atau komunikasi, hubungkan teori kanonik ke data empiris dan dokumen kebijakan resmi.
5. **Keguruan & Ilmu Pendidikan (FKIP)**:
   - Untuk tugas praktik mengajar, RPP/Modul Ajar (Kurikulum Merdeka / K-13), Penelitian Tindakan Kelas (PTK), atau evaluasi pembelajaran, sesuaikan dengan capaian pembelajaran (CP/ATP), karakteristik peserta didik pada kasus, rubrik asesmen nyata, dan regulasi Kemendikbudristek/BSKAP yang berlaku.

### Mode C: Naskah Bicara & Panduan Rekaman Video Demonstrasi (Self-Contained `write-talk-script`)
Gunakan ketika tugas praktikum (`STSI4205`, `STSI4309`, dll.) mewajibkan pembuatan video penjelasan/demonstrasi:
1. **Anggaran Kata & Kecepatan Bicara**: Gunakan patokan kecepatan bicara natural **~130 kata per menit (WPM)**. Hitung anggaran kata per segmen menggunakan `python3 scripts/word_budget.py --minutes <durasi>` dan uji draf naskah dengan `python3 scripts/script_timer.py <berkas.md>`.
2. **Gaya Bahasa Lisan (Spoken Register)**: Tulis kalimat yang enak diucapkan mahasiswa saat merekam layar—kalimat pendek, lugas, menggunakan penunjuk layar eksplisit (*"Pada terminal di sebelah kiri, terlihat bahwa..."*, *"Di sini ping dari PC1 ke PC3 gagal karena..."*), beserta penanda waktu kumulatif `[00:00 - 00:45]` dan daftar bagian opsional yang boleh dipotong (`[OPSIONAL DIPOTONG JIKA WAKTU HABIS]`) sebesar 10–15% durasi.

### Mode D: Audit, Deslopifikasi, & Restrukturisasi Draf (Edit vs. Detect Mode)
1. **Mode Edit (Default)**: Lakukan suntingan minimum yang efektif (*minimum effective edit*) untuk menghapus pola AI slop, memperbaiki keselarasan klaim-bukti, menertibkan cetak miring PUEBI, dan merapikan alur argumen sambil mempertahankan suara asli penulis.
2. **Mode Detect / Audit Saja (Bila pengguna meminta cek tanpa tulis ulang)**: Jangan menulis ulang draf. Sebutkan pola AI slop, ketidaktepatan klaim, atau cacat struktur yang ditemukan, kutip barisnya, dan berikan saran perbaikan singkat.

---

## 4. Kode Pintas Perintah Tersimpan (`B1E2P3`, `A1B2C3`, & `A2B4C6`)

Kode pintas memicu perintah tersimpan sehingga pengguna tidak perlu mengulang instruksi panjang. Format pemicu adalah `<KODE>-<KODE_MK>`, dengan bagian setelah tanda hubung diganti kode mata kuliah yang disebut pengguna, misalnya `B1E2P3-EKMA4116`, `A1B2C3-HKUM4201`, atau `A2B4C6-STSI4309`.

| Kode Pintas | Peruntukan | Perbedaan Keluaran Utama |
|---|---|---|
| `B1E2P3-<KODE_MK>` | Khusus **diskusi** (Tuton) | Berupa paragraf dengan batas maksimal **1.500 karakter**, daftar pustaka tanpa tautan (minimal 5 sumber eksternal + 1 BMP), parafrase akademik bebas AI slop. |
| `A1B2C3-<KODE_MK>` | Khusus **tugas esai reguler** (Tugas 1, 2, dan 3 non-praktikum), klon dari `B1E2P3` | Menjalankan perintah tersimpan `B1E2P3` (paragraf maks. **1.500 karakter**, minimal 5 sumber eksternal + 1 BMP tanpa tautan), ditambah aturan keluaran **teks polos non-Markdown** disertai petunjuk penyalinan ke editor teks Markdown. |
| `A2B4C6-<KODE_MK>` | Khusus **tugas praktikum / laporan proyek / studi kasus mendalam** di seluruh fakultas (jaringan, SIG, akuntansi/keuangan, hukum, RPP/PTK, lab sains, dll.) | **Tanpa batas karakter** (tidak dibatasi 1.400/1.500 karakter), disimpan dalam berkas **Markdown lengkap** (`T{1|2|3}-<KODE_MK>-<NIM>.md`, biarkan pengguna mengekspor sendiri ke PDF/DOCX), berbasis **artefak/data aktual sesuai bidang ilmu** (plus `Panduan-Rekaman-Video.md` untuk pegangan mahasiswa bila ada video), serta **wajib** menerapkan anti-AI slop, humanisasi akademik, cetak miring PUEBI, dan sitasi/daftar pustaka nyata (minimal 5 sumber eksternal + 1 BMP/buku ajar utama tanpa tautan). |

### A. Perintah Tersimpan untuk `B1E2P3` & `A1B2C3` (Diskusi & Tugas Esai Reguler)
Buatkan jawaban soal yang dilampirkan untuk mata kuliah dengan kode yang disebut, dengan ketentuan:
1. **Bentuk dan panjang**: berupa paragraf, dengan batas maksimal **1.500 karakter**.
2. **Daftar pustaka tanpa tautan**: sertakan daftar pustaka tanpa tautan apa pun, baik tautan eksternal maupun tautan yang berkaitan dengan mata kuliah itu sendiri.
3. **Komposisi sumber**: daftar pustaka minimal terdiri dari **5 sumber eksternal** dan **1 sumber dari BMP** mata kuliah tersebut.
4. **Parafrase final**: hasil keluaran wajib sudah diparafrasekan secara mandiri, berbahasa akademik yang ketat, dan bebas dari ciri khas tulisan AI (terapkan Bagian 5), sehingga draf siap ditinjau dan disunting kembali oleh mahasiswa sebelum dikumpulkan.

### B. Aturan Tambahan Khusus `A1B2C3` (Tugas Esai 1/2/3)
1. **Jangan membuat jawaban dalam format Markdown**, agar token tidak cepat habis. Sajikan jawaban sebagai teks polos tanpa judul `#`, huruf tebal, tabel, atau daftar berformat.
2. **Sertakan petunjuk penyalinan**: akhiri keluaran dengan petunjuk singkat agar pengguna menyalin jawaban ke editor teks Markdown untuk penyusunan akhir.

### C. Aturan Khusus `A2B4C6` (Tugas Praktikum / Laporan Praktikum Teknis — Pembeda dari `A1B2C3`)
Ketika pengguna memicu `A2B4C6-<KODE_MK>` (atau meminta penyusunan laporan praktikum berdasarkan template laporan praktikum seperti `.docx`/`.odt`), **jangan** menerapkan aturan batas karakter 1.500 karakter maupun format teks polos 1 paragraf milik `A1B2C3`. Jalankan ketentuan berikut:
1. **Keluaran Berkas Markdown Lengkap Tanpa Batas Karakter (Biarkan Pengguna Ekspor Sendiri)**:
   - Susun laporan praktikum secara utuh dan mendalam tanpa batas karakter (bebas dari batas 1.400/1.500 karakter) ke dalam berkas Markdown (`T{1|2|3}-<KODE_MK>-<NIM>.md`) menggunakan pemformatan Markdown lengkap (*heading* per langkah verifikasi, tabel pengalamatan IP/port/parameter, blok kode konfigurasi CLI/log pengujian, serta narasi analisis teknis).
   - Ikuti struktur bagian dan urutan verifikasi dari berkas template laporan praktikum yang dilampirkan pengguna (mis. `Laporan Praktikum 3 STSI4309.docx`).
   - **Jangan** mengonversi otomatis ke `.pdf` atau `.docx` kecuali diminta secara eksplisit; biarkan pengguna yang mengekspor sendiri berkas `.md` tersebut ke PDF.
2. **Wajib Berbasis Artefak & Data Aktual Sesuai Bidang Ilmu (Mode B & Mode C)**:
   - Bangun atau verifikasi artefak nyata sesuai mata kuliah/bidang ilmu (mis. berkas `.pkt` dan log CLI pada jaringan komputer, log perintah terminal pada sistem operasi, proyek `.qgz` atau skrip perhitungan pada SIG/statistika/ekonomi, kertas kerja akuntansi/keuangan, dokumen regulasi/putusan pada hukum, atau RPP/modul ajar/instrumen pada pendidikan). Pastikan seluruh angka, tabel, pasal, atau output identik 100% dengan artefak aktual.
   - Bila tugas mewajibkan rekaman video verifikasi/demonstrasi/praktik mengajar, buatkan juga berkas pendamping `Panduan-Rekaman-Video.md` (berisi urutan langkah, daftar poin/perintah singkat, dan contoh narasi lisan per segmen) khusus untuk pegangan mahasiswa saat merekam (tidak ikut disetor ke LMS).
3. **Kewajiban Baru: Anti-AI Slop, Humanisasi Akademik, Disiplin PUEBI, & Sitasi/Daftar Pustaka Nyata**:
   - Seluruh penjelasan teknis dan analisis hasil pengujian pada laporan praktikum **wajib** menerapkan standar anti-AI slop dan humanisasi akademik (Bagian 5), variasi ritme kalimat (*burstiness*), serta pencetakan miring (*italic*) istilah bahasa asing yang belum diserap ke dalam KBBI sesuai PUEBI.
   - Wajib menyertakan sitasi in-text `(Penulis, Tahun)` pada penjelasan konsep/analisis mekanisme teknis dan mencantumkan bagian `## Daftar Pustaka` (format APA Style 7th Edition **tanpa tautan apa pun**) di akhir laporan praktikum yang memuat minimal **5 sumber eksternal terverifikasi nyata** dan **1 sumber BMP** mata kuliah terkait (Bagian 6).

### D. Prosedur Eksekusi Kode Pintas
1. **Periksa lampiran**: pastikan soal dan/atau template laporan praktikum benar-benar terlampir atau tertulis di percakapan; jangan berasumsi berkas ada hanya karena disebut. Bila soal tidak ditemukan, minta pengguna melampirkannya.
2. **Tentukan mata kuliah dan BMP**: gunakan daftar BMP pada Bagian 6. Bila kode mata kuliah tidak ada di daftar, cari judul dan penulis BMP-nya melalui pencarian; jangan mengarang.
3. **Riset sebelum menulis**: kumpulkan minimal 5 sumber eksternal yang nyata dan terverifikasi (Bagian 6). Ketiadaan tautan di daftar pustaka tidak mengurangi kewajiban memverifikasi bahwa setiap sumber memang ada.
4. **Tulis dan audit**:
   - Untuk `B1E2P3` dan `A1B2C3`: jalankan `python3 scripts/ut_audit.py <berkas> --max-chars 1500` dan perbaiki hingga 0 temuan.
   - Untuk `A2B4C6`: jalankan `python3 scripts/ut_audit.py <berkas.md>` (**tanpa** `--max-chars`) untuk mengaudit AI slop, cetak miring PUEBI, *burstiness*, dan kecocokan sitasi 1-ke-1 hingga 0 temuan.
5. **Kesesuaian sitasi**: setiap kutipan `(Penulis, Tahun)` pada badan jawaban/laporan harus berpasangan satu-satu dengan entri daftar pustaka berformat APA Style 7th Edition tanpa tautan.

---

## 5. Katalog Lengkap Deslopifikasi, Humanisasi, & Kaidah Prosa Akademik
*(Konsolidasi mandiri dari `no-ai-slop`, `humanizer`, `polish-prose`, `humanize-academic-writing`, `academic-writing`, dan `refactor-structure`)*

### A. Artefak Chatbot & Meta-Text (Hapus Seketika)
Jangan pernah menyisakan kalimat pembuka/penutup asisten seperti *"Tentu, berikut adalah..."*, *"Berdasarkan dokumen yang Anda berikan..."*, *"Semoga membantu"*, atau *placeholder* `[isi sitasi]` / `[Link Video]`.

### B. Pembuka Klise & Kosakata Promosi yang Dilarang (Banned Lexical & Phrasal Tells)
| Pola Klise / AI Slop (Indonesia & Inggris) | Mengapa Terdeteksi sebagai AI | Pola Penulisan Ulang (Humanic Academic) |
|---|---|---|
| *"Di era digital yang semakin berkembang pesat..."* / *"Dalam era globalisasi / Revolusi Industri 4.0..."* / *"Seiring dengan perkembangan teknologi..."* | Pembuka pengulur waktu (*throat-clearing*) yang bisa ditempel ke topik apa pun | Hapus. Mulai kalimat pertama langsung pada subjek teknis, mekanisme, atau masalah spesifik soal. |
| *"Tidak dapat dipungkiri bahwa..."* / *"Perlu dicatat bahwa..."* / *"Penting untuk diingat bahwa..."* (*It is worth noting that*) | Penegasan kosong sebelum klaim biasa | Hapus pengantarnya; tulis langsung klaim beserta buktinya. |
| *krusial, esensial, vital, holistik, komprehensif, transformatif, revolusioner, sinergi, peran sentral, garda terdepan, lanskap, menyelami (delve), memanfaatkan secara optimal (leverage)* | Kosakata brosur/promosi (*puffery*) yang menggantikan penjelasan teknis | Ganti dengan kata kerja dan ukuran konkret: *memisahkan domain broadcast*, *menurunkan waktu henti*, *mengintegrasikan empat basis data terpisah*. |
| *"Bukan hanya X, melainkan juga Y"* / *"Tidak sekadar X, tetapi juga Y"* (*Not only X, but also Y*) | Kontras biner mekanis khas LLM bila diulang | Nyatakan langsung kedua fungsi/implikasinya dengan konjungsi lugas (*dan*, *serta*, *sekaligus*). |
| *"Dengan demikian, dapat disimpulkan bahwa..."* / *"Secara keseluruhan..."* di akhir tiap paragraf | Kalimat penutup satu baris yang hanya mengulang kalimat sebelumnya | Hapus kalimat simpulan repetitif; biarkan paragraf berhenti pada bukti, contoh konkret, atau implikasi operasional terakhir. |
| *Em-dash* (`—`) berulang, **huruf tebal** di tengah kalimat prosa, atau *rule of three* (tiga kata sifat berurutan di tiap kalimat) | Tanda baca dan ritme sintaksis seragam khas generator teks | Gunakan koma, titik, atau tanda kurung biasa; jangan menebalkan kata di badan paragraf; variasikan struktur klausa. |

### C. Kaidah Positif Penulisan Manusiawi & Standar Lolos DrillBit (< 30% AI & Similaritas)
1. **Variasi Ritme Kalimat & Pemutus Ritme (*DrillBit Burstiness Rule*)**:
   - Berdasarkan kalibrasi laporan *DrillBit AI Content Detection*, 84,4% paragraf yang ditandai sebagai teks AI adalah paragraf ≥ 3 kalimat yang seluruh kalimatnya berukuran sedang-panjang (≥ 16 kata) tanpa kalimat pendek.
   - Oleh karena itu, **pada setiap paragraf prosa ≥ 3 kalimat (≥ 60 kata), wajib ada minimal satu kalimat pendek yang tegas (6–13 kata)** yang diselingkan dengan kalimat analitis bermuatan teknis (20–35 kata), sehingga `min_sent <= 13` atau koefisien variasi panjang kalimat (`CV = SD / rata-rata`) ≥ 0,36.
2. **Reduksi Sintaksis Terjemahan Inggris SVO (`me-...-kan`), Adverbia `secara`, & Kopula `merupakan`**:
   - **Batas verba aktif transitif `me-...-kan/-i` < 30,0 per 1.000 kata**: hindari pola monoton `[Subjek abstrak] + me-...-kan + [objek]` (*menunjukkan*, *menegaskan*, *membuktikan*, *menghadirkan*, *memungkinkan*, *melahirkan*, *menggarisbawahi*). Ubah sebagian kalimat ke konstruksi pasif (`di-...-kan` / `ter-`), klausa nominal, atau pembuka preposisional (*Di tingkat...*, *Pada ranah...*, *Dari sisi...*).
   - **Batas adverbia `secara <adjektiva>` < 6,0 per 1.000 kata** (*secara langsung* → *langsung*, *secara mandiri* → *mandiri*, *secara eksplisit* → *tegas*) dan **kopula `merupakan` < 1,0 per 1.000 kata** (variasikan dengan *adalah*, *ialah*, *menjadi*).
   - **Variasi Pembuka Daftar Berpoin (*Layout Regularity*)**: jangan mengawali butir daftar berurutan (`1., 2., 3.` atau `a., b., c.`) dengan kata kerja atau kopula yang sama setelah titik dua (`Merupakan...`, `Mengevaluasi...`, `Menyediakan...`).
3. **Parafrase Struktural Mendalam (Target Similaritas & AI DrillBit < 30%, Target Pengaman < 15%)**:
   - Saat memparafrasekan materi BMP, artikel jurnal, atau draf tugas sebelumnya, jangan sekadar mengganti sinonim kata per kata. Balik urutan klausa (anak kalimat ↔ induk kalimat), ubah aktif ↔ pasif, pecah atau gabungkan kalimat, dan pastikan overlap 8-gram terhadap naskah asal `< 15%` agar lolos pemindaian **DrillBit** jauh di bawah ambang **30%**.
4. **Uji Tukar Topik (*Portability Test*)**: Jika sebuah kalimat tetap terdengar cocok saat dipindahkan ke jawaban mata kuliah lain hanya dengan mengganti kata benda utamanya (misal: *"Penerapan kerangka ini meningkatkan efisiensi dan efektivitas organisasi secara signifikan"*), kalimat tersebut adalah *slop*. Ganti dengan mekanisme spesifik dari kasus soal.
5. **Kalibrasi Klaim & Hedging (Aturan `verify-claims`)**:
   - Jangan gunakan kata *signifikan* kecuali merujuk pada uji statistik atau angka selisih yang terukur.
   - Jangan gunakan klaim absolut (*selalu*, *menjamin sepenuhnya*, *satu-satunya*) tanpa syarat batas teknisnya.
   - Setiap angka di dalam teks narasi wajib sama persis dengan angka di dalam tabel atau log keluaran skrip.
6. **Disiplin Istilah Asing (PUEBI/EYD)**:
   - Cetak miring (*italic*) istilah bahasa asing yang belum diserap ke dalam KBBI di bidang apa pun, misalnya: *stakeholder*, *governance*, *supply chain*, *cash flow*, *return on investment*, *judicial review*, *due process*, *scaffolding*, *blended learning*, *randomized controlled trial*, *open standard*, *single point of failure*, *switching costs*, *throughput*, *defense in depth*.
   - **Jangan** memiringkan nama diri, merek, lembaga, singkatan/standar berhuruf kapital (`PDRB`, `UMKM`, `BUMN`, `KUHP`, `KUHPer`, `PSAK`, `RPP`, `CP/ATP`, `WHO`, `UNESCO`, `SPSS`, `SQL`, `VLAN`, `OSPF`, `ISO/IEC 27001`, `QGIS`), atau kata serapan yang sudah baku di KBBI (*server*, *klien*, *jaringan*, *topologi*, *konfigurasi*, *infrastruktur*, *aplikasi*, *basis data*, *komputasi*, *virtualisasi*, *enkripsi*, *autentikasi*, *lisensi*, *manajemen*, *investasi*, *regulasi*, *evaluasi*, *kurikulum*).

---

## 6. Protokol Verifikasi Referensi & Anti-Halusinasi Sitasi
*(Konsolidasi mandiri dari `verify-citations`, `find-papers`, dan `fetch-paper`)*

1. **Hierarki Sumber**:
   - **Wajib Utama**: Buku Materi Pokok (BMP) Universitas Terbuka atau buku ajar utama mata kuliah terkait pada perguruan tinggi pengguna. Identifikasi judul, penulis, edisi, dan tahun terbit BMP/buku ajar resmi dari lampiran pengguna atau katalog resmi pustaka universitas (jangan mengarang metadata). Contoh entri BMP terverifikasi:
     - `STSI4304`: Arifin, Z., & Nugroho, K. (2020). *Dasar infrastruktur teknologi informasi* (Edisi 1). Universitas Terbuka.
     - `STSI4305`: Sukoco, H., & Widiastuti, I. (2021). *Etika profesi* (`MSIM4408`). Universitas Terbuka.
     - `STSI4306`: Arifin, Z. (2022). *Arsitektur dan perancangan sistem enterprise* (`MSIM4311`). Universitas Terbuka.
     - `STSI4205`: Sukaridhoto, S. (2020). *Jaringan komputer* (`MSIM4204`). Universitas Terbuka.
     - `STSI4309`: Wahyono, T. (2022). *Administrasi jaringan* (`MSIM4316`). Universitas Terbuka.
   - **Pendukung Kanonik & Regulasi Lintas Bidang**:
     - *Ekonomi, Manajemen, & Akuntansi (FEB)*: buku teks standar (Mankiw, Kotler & Keller, Kieso et al., Brigham & Houston), standar akuntansi (PSAK/SAK IAI, IFRS), serta data resmi (BPS, Bank Indonesia, OJK, Kemenkeu, IDX).
     - *Hukum, Ilmu Sosial, & Politik (FHISIP)*: peraturan perundang-undangan dan putusan pengadilan (`peraturan.go.id`, JDIH, Mahkamah Agung, MK), buku teks hukum/sosial klasik dan mutakhir, serta dokumen kebijakan resmi.
     - *Keguruan & Pendidikan (FKIP)*: regulasi pendidikan (UU Sisdiknas, Permendikbudristek, panduan BSKAP), buku pedagogi/evaluasi pembelajaran, dan jurnal pendidikan (SINTA, ERIC, DOAJ).
     - *Sains, Teknik, & TI (FST)*: buku teks standar (Laudon & Laudon, Stallings & Brown, Tanenbaum & Wetherall, Kurose & Ross, Pressman, Sjafrizal), standar resmi (`IEEE`, `RFC`, `ISO/IEC`, `COBIT`, `NIST`), serta regulasi terkait (`UU Hak Cipta`, `UU ITE`, `UU PDP`).
     - *Kesehatan & Biologi*: pedoman WHO, Kemenkes, serta artikel terindeks PubMed/Scopus.
2. **Larangan Mutlak Sitasi Fiktif**:
   - Dilarang mengarang nama penulis, tahun terbit, judul buku/jurnal, nomor volume, atau DOI.
   - Pada mesin lokal yang terhubung ke internet, gunakan `python3 scripts/crossref_search.py "<kata kunci>"` atau `python3 scripts/s2_search.py "<kata kunci>"` bila memerlukan artikel jurnal tambahan; pada web LLM, gunakan *Web Search*.
3. **Kesesuaian Satu-Satu In-Text & Daftar Pustaka (`## Sumber` / `## Daftar Pustaka`)**:
   - Setiap kutipan `(Penulis, Tahun)` di dalam jawaban wajib tercantum di bagian `## Sumber` atau `## Daftar Pustaka` dengan format **APA Style 7th Edition**, dan setiap entri di daftar pustaka wajib dikutip minimal satu kali di dalam jawaban.

---

## 7. Gerbang Pemeriksaan Akhir (Self-Check & Bundled Scripts)

Sebelum menyerahkan hasil akhir kepada pengguna, jalankan pemeriksaan berikut:
1. **Audit Otomatis dengan Skrip Bawaan** (jika terminal/Python tersedia):
   ```bash
   # Audit Bahasa Indonesia/Inggris: AI Slop, PUEBI Italic, Burstiness, Batas Karakter, & Sitasi APA 1-ke-1
   python3 scripts/ut_audit.py <berkas.md|.odt|.docx> [--max-chars 1500]
   ```
   *(Catatan: Untuk `A2B4C6` / Laporan Praktikum, jalankan `ut_audit.py` **tanpa** `--max-chars`).*
2. **Perbaikan Temuan**:
   - Jika `ut_audit.py` menemukan kata AI slop, kalimat yang terlalu seragam (*burstiness* rendah), istilah asing yang belum dimiringkan, kelebihan batas karakter (khusus `B1E2P3`/`A1B2C3`), atau sitasi yang belum memiliki pasangan di `## Sumber` / `## Daftar Pustaka`, perbaiki terlebih dahulu hingga **0 temuan**.
3. **Verifikasi Khusus Kode Pintas** (bila dipicu `B1E2P3`, `A1B2C3`, atau `A2B4C6`):
   - **`B1E2P3` & `A1B2C3`**: Jawaban tidak melebihi 1.500 karakter, daftar pustaka memuat minimal 5 sumber eksternal dan 1 BMP tanpa tautan sama sekali, dan untuk `A1B2C3` keluaran berupa teks polos disertai petunjuk penyalinan ke editor teks Markdown, atau buatkan file teks Markdown jika pengguna memintanya.
   - **`A2B4C6`**: Laporan praktikum disajikan dalam berkas `.md` lengkap **tanpa batas karakter** (biarkan pengguna mengekspor sendiri ke PDF), seluruh konfigurasi/tabel/log identik dengan artefak nyata sesuai mata kuliah (`.pkt`, skrip, proyek QGIS, log Linux) ditambah `Panduan-Rekaman-Video.md` bila ada kewajiban video, serta memenuhi kewajiban anti-AI slop, humanisasi akademik, cetak miring PUEBI, dan sitasi 1-ke-1 (minimal 5 sumber eksternal terverifikasi + 1 BMP tanpa tautan).
4. **Verifikasi Akhir Instruksi Soal**:
   - Pastikan seluruh sub-pertanyaan terjawab tuntas, angka tabel cocok dengan perhitungan skrip, dan format keluaran (`.md`, `.pdf`, `.docx`, `.odt`) sesuai dengan yang diminta pengguna.
