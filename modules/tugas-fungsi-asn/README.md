# Penerapan Tugas dan Fungsi ASN di Tempat Kerja: Implementasi BerAKHLAK

Modul pembelajaran interaktif mandiri (*e-learning*) orientasi **Core Values BerAKHLAK** dan penerapannya pada tata kelola di lingkungan **Kementerian Agama Republik Indonesia**.

Dirancang mengacu pada materi resmi Pusbangkom MKMB (Pusat Pengembangan Kompetensi Manajemen Kepemimpinan dan Moderasi Beragama).

---

## 🌟 Fitur Utama

- **12 Unit Modul Terstruktur & Interaktif:**
  - Unit 00: Cover & Orientasi Pembelajaran
  - Unit 01: Peta Alur Belajar (4 Fase Strategis)
  - Unit 02: Core Values BerAKHLAK (7 Flip Card 3D) & 5 Prinsip Dasar ASN
  - Unit 03: Dimensi Pelayanan Prima & Akuntabilitas Teruji (Micro-Quiz Kasus Integritas)
  - Unit 04: 5 Dimensi Inti Lanjutan (Tabbed Navigator: Kompeten, Harmonis, Loyal, Adaptif, Kolaboratif)
  - Unit 05: 5 Ekosistem Digitalisasi Layanan Kemenag (Pusaka, EMIS 4.0, SIMBA, AI Konsultasi, Sihalal PTSP)
  - Unit 06: Mendorong Adopsi Digital Umat (Interactive Range Simulator Slider 10% - 100%)
  - Unit 07: 5 Hambatan Utama Transformasi Digital (5 Diagnostic 3D Flip Scanner Cards)
  - Unit 08: Solusi Komprehensif & Tata Kelola Keagamaan Inklusif (4 Pilar Solusi Matrix)
  - Unit 09: Simulasi Kasus Nyata Dilema Etika di Meja Pelayanan (Branching Decision Scenario)
  - Unit 10: Evaluasi Akhir Post-Test (8 Soal Pilihan Ganda Terenkripsi SHA-256 & XOR Ciphertext)
  - Unit 11: Rangkuman Pembelajaran & Lembar Ikrar Komitmen Digital BerAKHLAK
- **Audio Narasi Otomatis (TTS AI):**
  - Terintegrasi suara narator resmi bahasa Indonesia (`id-ID-GadisNeural`) untuk seluruh unit materi (`audio/unit_0.mp3` s.d. `audio/unit_11.mp3`).
  - Dilengkapi kontrol audio di sticky header, pill animasi status di stage card, dan tombol putar ulang.
- **Lapisan Keamanan & Anti-Cheat (Cryptographic Security Vault):**
  - Kunci jawaban diverifikasi satu arah via **SHA-256 with Salt**.
  - Bebas kebocoran DOM (*Zero DOM Leaks*). Tidak ada atribut kunci jawaban pada HTML.
  - Pembahasan didekripsi secara *on-the-fly* (*Hex XOR Ciphertext*) hanya jika jawaban tepat.
  - Isolasi memori (*IIFE Closure*) sehingga variabel internal tidak dapat dimanipulasi via Developer Console.
  - Proteksi integritas progres *localStorage* berbasis tanda tangan digital (HMAC signature).
  - Pembatasan klik kanan dan tombol inspeksi DevTools (*F12, Ctrl+Shift+I/J/C, Ctrl+U*).
- **Double-Locking Gate Mechanism:**
  - Memastikan peserta menyelesaikan aktivitas interaktif wajib dan membaca minimal 10 detik sebelum tombol lanjut terbuka.
  - Status visual 3 warna (*Merah: belum selesai tugas* -> *Biru: timer membaca* -> *Hijau berdenyut: siap lanjut*).
- **Efek Suara Taktil (Web Audio API Synthesizer):**
  - Suara klik lembut, nada melodi sukses, nada peringatan kesalahan, dan nada fanfare kelulusan.
- **Desain Modern & Responsif:**
  - Menggunakan Tailwind CSS palet warna *Algae Green* khas Kemenag yang ramah diakses lewat desktop maupun smartphone.

---

## 📁 Struktur Direktori

```text
├── index.html                           # File utama modul (Kompatibel dengan GitHub Pages)
├── Penerapan Tugas dan Fungsi ASN.html  # File modul mandiri
├── generate_audio.py                    # Script generator audio narasi otomatis (Edge-TTS)
├── audio/                               # Folder aset audio narasi (unit_0.mp3 - unit_11.mp3)
├── audio_berakhlak/                     # Alias folder audio
├── .gitignore
└── README.md
```

---

## 🚀 Cara Menjalankan

1. **Secara Langsung (Offline):**
   Cukup *double-click* file `index.html` atau `Penerapan Tugas dan Fungsi ASN.html` pada browser modern (Google Chrome, Microsoft Edge, Mozilla Firefox, dll).
2. **Via Web Server / GitHub Pages:**
   Letakkan berkas ini pada *root* repositori web hosting atau aktifkan fitur GitHub Pages pada cabang repositori terkait.

---

## 🎙️ Men-generate Ulang Audio Narasi

Jika ingin memperbarui naskah atau mengubah suara narator:
1. Pastikan Python 3.8+ terpasang.
2. Install dependensi: `pip install edge-tts`
3. Jalankan script:
   ```bash
   python generate_audio.py
   ```
