# Panduan Pengelolaan & Pengeditan Website Portofolio

Dokumentasi ini dibuat untuk memudahkan pemilik website (**Abdullah Syamsidar**) atau kolaborator dalam memperbarui isi portofolio tanpa khawatir merusak tata letak maupun fungsi interaktif halaman.

---

## 📁 Struktur Berkas

```text
portfolio-syamsidar/
├── index.html                  # Berkas utama portofolio
├── profile.jpg                 # Foto profil resmi
├── README.md                   # Panduan ini
└── modules/                    # Modul E-Learning Interaktif Mandiri
    ├── manajemen-kinerja/      # Modul 16 Unit: Pengenalan Manajemen Kinerja Pegawai ASN (MOOC P3K)
    │   ├── index.html
    │   └── audio/              # File audio narasi TTS (unit_0.mp3 s.d. unit_15.mp3)
    ├── tugas-fungsi-asn/       # Modul 12 Unit: Penerapan Tugas & Fungsi ASN (Orientasi BerAKHLAK)
    │   ├── index.html
    │   └── audio/              # File audio narasi TTS (unit_0.mp3 s.d. unit_11.mp3)
    └── pengenalan-jabatan/     # Modul 11 Unit: Pengenalan Jabatan ASN Kemenag
        ├── index.html
        └── audio/              # File audio narasi TTS (unit_0.mp3 s.d. unit_10.mp3)
```

Website dan seluruh modul di dalamnya bersifat **standalone & offline-ready**. Setiap modul e-learning di dalam folder `modules/` memiliki struktur aplikasi web mandiri lengkap dengan:
- Audio narasi teks-ke-suara (TTS) terpasang di folder `audio/`.
- Efek suara interaktif berbasis Web Audio API (tanpa dependensi file eksternal).
- Gate timer 10 detik membaca dan pos tugas interaktif (*task checkpoints*).
- Kuis evaluasi berbasis enkripsi kriptografi SHA-256 (*anti-tamper & anti-cheat*).
- Lembar ikrar komitmen digital yang dapat ditandatangani dan disalin peserta.

---

## 🛠️ Peta Navigasi Kode di `index.html`

Di dalam file `index.html`, setiap bagian telah ditandai dengan komentar panduan `<!-- [EDITABLE]: ... -->` yang terstruktur:

| No | Bagian Halaman | Estimasi Baris | Yang Dapat Diubah |
|---|---|---|---|
| 1 | **Konfigurasi Tema** | Baris ~45 | Palet warna (`brand`, `accent`) & font |
| 2 | **Header / Navigasi** | Baris ~120 | Logo inisial/ikon, teks nama, dan menu navigasi |
| 3 | **Hero Section** | Baris ~190 | Status badge, judul utama, bio singkat, 4 sorotan |
| 4 | **Tentang Saya (About)** | Baris ~300 | Avatar, profil ringkas, cerita latar belakang, nilai tambah |
| 5 | **Keahlian (Skills)** | Baris ~410 | Kategori kompetensi, persentase penguasaan, badge tools |
| 6 | **Proyek (Projects)** | Baris ~570 | Kartu karya, kategori filter, tautan modul live demo |
| 7 | **Pengalaman (Experience)** | Baris ~780 | Linimasa magang, peran organisasi, uraian pencapaian |
| 8 | **Sertifikasi (Credentials)** | Baris ~880 | Nama sertifikat, nomor registrasi/lisensi, penerbit |
| 9 | **Kontak (Contact)** | Baris ~990 | Alamat surel, nomor WhatsApp (+pesan otomatis), GitHub, domisili |
| 10 | **Modal Studi Kasus** | Baris ~1100 | Rincian masalah, solusi yang dirancang, tombol buka live demo |
| 11 | **JavaScript Controllers** | Baris ~1450 | Fungsi dark mode, filter, popup modal, dan salin email |

---

## 🚀 Menjalankan & Membuka Modul Interaktif

1. **Secara Lokal (Offline):**
   - Buka file `index.html` di browser (Chrome, Edge, Firefox).
   - Masuk ke bagian **Proyek** > klik **"Lihat Studi Kasus & Demo"** pada proyek modul yang diinginkan.
   - Klik tombol **"Buka Modul Interaktif (Live Demo)"**. Modul akan terbuka di tab baru dan audio narasi serta seluruh interaksinya dapat langsung dimainkan tanpa butuh koneksi internet!

2. **Secara Online (GitHub Pages / Hosting Web):**
   - Cukup unggah seluruh isi folder `portfolio-syamsidar/` (termasuk folder `modules/`) ke repositori GitHub.
   - Aktifkan GitHub Pages pada branch utama.
   - Seluruh modul akan otomatis dapat diakses publik dengan URL:
     - `https://username.github.io/modules/manajemen-kinerja/`
     - `https://username.github.io/modules/tugas-fungsi-asn/`
     - `https://username.github.io/modules/pengenalan-jabatan/`

---

## 📝 Panduan Perubahan Konten (How-To)

### 1. Mengubah Data Pribadi & Kontak
Buka `index.html`, lalu cari (Ctrl+F) kata kunci:
- **Email**: Ganti `abdullahsyamsidar@gmail.com`
- **Nomor WhatsApp**: Ganti `6289639301997` pada tautan `https://wa.me/6289639301997?text=...` (Gunakan kode negara `62` tanpa tanda `+` atau spasi).
- **Akun GitHub**: Ganti `NotSyam`.

### 2. Menambah Proyek Baru
Untuk menambahkan proyek baru:
1. Masuk ke bagian `<!-- 05. PROJECTS & CASE STUDIES -->`.
2. Salin salah satu blok `<article class="project-card ...">`.
3. Sesuaikan atribut `data-category` (misal: `prestasi`, `diklat`, `riset`).
4. Atur tombol pemicu modal:
   ```html
   <button type="button" onclick="openModal('modal-proyek-baru')">Lihat Studi Kasus</button>
   ```
5. Masuk ke bagian `<!-- 10. MODAL POP-UP RINCIAN STUDI KASUS -->`.
6. Salin salah satu blok modal dan ubah ID-nya menjadi `id="modal-proyek-baru"`.
