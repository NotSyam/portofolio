# Pengenalan Jabatan ASN Kementerian Agama

Modul pembelajaran interaktif mandiri (*e-learning*) untuk orientasi pegawai baru, CPNS, dan PPPK di lingkungan **Kementerian Agama Republik Indonesia**.

Dirancang mengacu pada materi resmi Pusbangkom MKMB (Pusat Pengembangan Kompetensi Manajemen Kepemimpinan dan Moderasi Beragama).

---

## 🌟 Fitur Utama

- **11 Unit Modul Terstruktur:** Mulai dari Orientasi, Skala Satuan Kerja & Pegawai, Komparasi PNS vs PPPK, Definisi Jabatan (FTTWH), Klasifikasi Manajerial/Non-Manajerial, Profil 55 JF, Batas Usia Pensiun, Pola Perpindahan Karir, hingga Post-Test Kuis Akhir.
- **Audio Narasi Otomatis (TTS AI):** Terintegrasi suara narator natural bahasa Indonesia untuk setiap unit materi (udio/unit_0.mp3 s.d. udio/unit_10.mp3) lengkap dengan kontrol audio di sticky header dan tombol putar ulang.
- **Lapisan Keamanan & Anti-Cheat (Cryptographic Security Vault):**
  - Kunci jawaban terenkripsi satu arah menggunakan algoritma **SHA-256 with Salt**.
  - Bebas kebocoran DOM (*Zero DOM Leaks*). Tidak ada atribut kunci jawaban pada HTML.
  - Pembahasan kuis terenkripsi (*ciphertext*) dan hanya dapat didekripsi ketika jawaban benar dipilih.
  - Isolasi memori (*IIFE Closure*) sehingga variabel internal tidak dapat diakses melalui Console Developer Tools.
  - Proteksi manipulasi data *localStorage* berbasis *digital signature* (HMAC).
  - Pembatasan klik kanan dan pintasan keyboard inspeksi (*F12 / DevTools*).
- **Desain Modern & Responsif:** Menggunakan Tailwind CSS dengan palet tema warna *Algae Green* khas Kemenag yang ramah diakses lewat desktop maupun smartphone.
- **Gate Locking Mechanism:** Memastikan peserta membaca modul dan menyelesaikan tugas interaktif unit sebelum tombol navigasi lanjut terbuka.

---

## 📁 Struktur Direktori

`	ext
├── index.html                  # File utama modul (Kompatibel dengan GitHub Pages)
├── Tes Pengenalan Jabatan.html # File modul utama
├── generate_audio.py           # Script generator audio narasi otomatis (Edge-TTS)
├── audio/                      # Folder aset audio narasi (unit_0.mp3 - unit_10.mp3)
├── .gitignore
└── README.md
`

---

## 🚀 Cara Menjalankan

1. **Secara Langsung:**
   Cukup *double-click* file index.html pada browser modern (Google Chrome, Microsoft Edge, Mozilla Firefox, dll).
2. **Via GitHub Pages:**
   Aktifkan fitur **GitHub Pages** pada pengaturan repositori (*Settings > Pages > Branch: main / root*) untuk mengakses modul langsung secara online.

---

## 🎙️ Men-generate Ulang Audio Narasi

Jika ingin mengubah naskah atau suara narator:
1. Pastikan Python 3.8+ terpasang.
2. Install library: pip install edge-tts
3. Jalankan script:
   `ash
   python generate_audio.py
   `
