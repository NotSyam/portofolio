# Modul E-Learning Interaktif: Pengenalan Manajemen Kinerja Pegawai ASN
### Seri Orientasi Pegawai Pemerintah dengan Perjanjian Kerja (PPPK) & ASN Kementerian Agama RI

Modul pembelajaran interaktif berbasis web (*Single Page Application*) mandiri (*self-contained*) ini menyajikan materi teknis dan regulasi manajemen kinerja aparatur berdasarkan **PermenPANRB No. 6 Tahun 2022**, **SE MenpanRB No. 3 Tahun 2023**, dan materi resmi **Pusbangkom MKMB Kementerian Agama RI**.

Modul ini telah **100% diselaraskan secara struktural, arsitektural, dan visual** dengan modul:
1. **Pengenalan Jabatan — Orientasi ASN Kementerian Agama**
2. **Penerapan Tugas dan Fungsi ASN — Orientasi BerAKHLAK Kementerian Agama**

Sehingga ketiga modul siap untuk digabungkan ke dalam satu kesatuan paket **Course Orientasi ASN Kementerian Agama**.

---

## 🚀 Fitur Interaktif Unggulan

1. **Pohon Kinerja & Cascading Hierarchy (Unit 04):**
   - Mekanisme drag-and-drop / klik terurut 5 tingkatan instrumen: `RPJPN/RPJMN` $\rightarrow$ `Renstra Kemenag` $\rightarrow$ `Perjanjian Kinerja (PK) Pimpinan` $\rightarrow$ `SKP JPT` $\rightarrow$ `SKP JA/JF (PPPK)`.

2. **Simulasi Audit e-Kinerja "Spot the Mistake" (Unit 06):**
   - Inspeksi formulir SKP dalam antarmuka e-Kinerja BKN untuk menemukan dan mengoreksi 5 kesalahan fatal (Pejabat Penilai, Periode Penilaian, Rumusan RHK, Indikator & Target Kuantitas, serta Dukungan Sumber Daya).

3. **Sandbox Distribusi Predikat Kinerja Pegawai (Unit 09):**
   - Eksplorasi kurva distribusi predikat kinerja sesuai SE MenpanRB No. 3/2023 berdasarkan capaian kinerja unit kerja (Istimewa, Baik, Butuh Perbaikan, Kurang, Sangat Kurang) lengkap dengan kalkulator simulasi riil jumlah pegawai.

4. **Simulasi Alur Keberatan & Sengketa Kinerja (Unit 12):**
   - Pengujian batas waktu hukum pengajuan keberatan (14 hari ke penilai) dan banding (7 hari ke atasan penilai).

5. **Matriks Konsekuensi & Reward Kinerja PPPK (Unit 13):**
   - Pemetaan skenario predikat tahunan terhadap dampaknya pada perpanjangan kontrak kerja PPPK dan talent pool.

6. **Kuis Evaluasi Akhir 10 Butir Soal (Unit 14):**
   - Kuis evaluasi pemahaman regulasi dengan kunci jawaban dan pembahasan terenkripsi SHA-256 + XOR.
   - Ambang kelulusan 75% (minimal 8 benar), efek selebrasi confetti, nada fanfare, dan tombol eksplisit *Lanjut ke Penutup*.

7. **Lembar Ikrar Komitmen Digital (Unit 15):**
   - Pengisian nama pegawai, unit kerja/satker, checklist komitmen, tanda tangan digital interaktif, dan tombol salin ikrar ke clipboard.

---

## 🎧 Sistem Audio Terintegrasi

- **Sintesis Efek Suara (Web Audio API):**
  4 nada audio instan tanpa ketergantungan berkas eksternal (`click`, `success`, `error`, `fanfare`).
- **Narasi Suara Alami (Edge-TTS):**
  16 berkas narasi tersimpan di folder `audio/` (`unit_0.mp3` s.d. `unit_15.mp3`) yang dinarasikan oleh model suara `id-ID-GadisNeural`.
- **Kontrol Audio Penuh:**
  Tombol toggle narasi pada header, indikator pemutaran live di samping judul unit, serta tombol putar ulang (*replay*).

---

## 🛡️ Keamanan & Integritas Progres

- **Anti-Tamper Signature:** Status progres dan penyelesaian tugas dienkripsi dan divalidasi dengan SHA-256 signature (`STORAGE_KEY = "kemenag_pmk_lock_v1"`).
- **Unit Gate Lock:** Setiap unit mewajibkan pemenuhan tugas interaksi (`isTaskDone`) dan batas waktu telaah materi sebelum tombol lanjut aktif.
- **Answer Masking:** Seluruh kunci jawaban dan penjelasan umpan balik kuis disimpan dalam bentuk hash SHA-256 dan ciphertext hex.

---

## 📂 Struktur Berkas

```text
D:\Download\Pengenalan Manajemen Kinerja\
├── index.html                           # Aplikasi utama modul interaktif
├── Pengenalan Manajemen Kinerja.html    # Salinan identik aplikasi
├── README.md                            # Dokumentasi modul dan panduan penggabungan
├── generate_audio.py                    # Skrip regenerasi narasi Edge-TTS
└── audio/                               # Berkas audio narasi unit 0–15
    ├── unit_0.mp3
    ├── unit_1.mp3
    ...
    └── unit_15.mp3
```

---

## 🔗 Kesiapan Penggabungan Course (*Course Integration Ready*)

Modul ini telah mengadopsi standar DOM, CSS, dan JavaScript yang 100% kongruen dengan:
- `Pengenalan Jabatan.html`
- `Penerapan Tugas dan Fungsi ASN.html`

Semua variabel navigasi, hook audio, sistem kuncian gate, dan styling siap diintegrasikan baik sebagai modul mandiri maupun digabungkan ke dalam satu portal induk (*Master Course Wrapper*) Orientasi ASN Kemenag.
