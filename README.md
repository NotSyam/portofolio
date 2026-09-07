# Panduan Pengelolaan & Pengeditan Website Portofolio

Dokumentasi ini dibuat untuk memudahkan pemilik website (**Abdullah Syamsidar**) atau kolaborator dalam memperbarui isi portofolio tanpa khawatir merusak tata letak maupun fungsi interaktif halaman.

---

## 📁 Struktur Berkas

```text
portfolio-syamsidar/
├── index.html       # Berkas utama (HTML + Tailwind CSS + Lucide Icons + Javascript)
└── README.md        # Panduan ini
```

Website ini bersifat **standalone single-page**. Artinya, seluruh gaya tampilan (CSS), ikon, dan logika interaktif (JavaScript) bekerja secara mandiri tanpa memerlukan proses *build* atau instalasi Node.js/npm. Anda cukup mengklik dua kali file `index.html` untuk melihatnya di browser!

---

## 🛠️ Peta Navigasi Kode di `index.html`

Di dalam file `index.html`, setiap bagian telah ditandai dengan komentar panduan `<!-- [EDITABLE]: ... -->` yang terstruktur:

| No | Bagian Halaman | Estimasi Baris | Yang Dapat Diubah |
|---|---|---|---|
| 1 | **Konfigurasi Tema** | Baris ~45 | Palet warna (`brand`, `accent`) & font |
| 2 | **Header / Navigasi** | Baris ~120 | Logo inisial, teks nama, dan menu navigasi |
| 3 | **Hero Section** | Baris ~190 | Status badge, judul utama, bio singkat, 4 sorotan |
| 4 | **Tentang Saya (About)** | Baris ~300 | Avatar, profil ringkas, cerita latar belakang, nilai tambah |
| 5 | **Keahlian (Skills)** | Baris ~410 | Kategori kompetensi, persentase penguasaan, badge tools |
| 6 | **Proyek (Projects)** | Baris ~540 | Kartu karya, kategori filter, tautan studi kasus |
| 7 | **Pengalaman (Experience)** | Baris ~710 | Linimasa magang, peran organisasi, uraian pencapaian |
| 8 | **Sertifikasi (Credentials)** | Baris ~810 | Nama sertifikat, nomor registrasi/lisensi, penerbit |
| 9 | **Kontak (Contact)** | Baris ~920 | Alamat surel, nomor WhatsApp (+pesan otomatis), GitHub, domisili |
| 10 | **Modal Studi Kasus** | Baris ~1030 | Rincian masalah, solusi yang dirancang, dampak/prestasi |
| 11 | **JavaScript Controllers** | Baris ~1220 | Fungsi dark mode, filter, popup modal, dan salin email |

---

## 📝 Panduan Perubahan Konten (How-To)

### 1. Mengubah Data Pribadi & Kontak
Buka `index.html`, lalu cari (Ctrl+F) kata kunci:
- **Email**: Ganti `abdullahsyamsidar@gmail.com`
- **Nomor WhatsApp**: Ganti `6289639301997` pada tautan `https://wa.me/6289639301997?text=...` (Pastikan gunakan kode negara `62` tanpa tanda `+` atau spasi).
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

### 3. Mengganti Ikon
Website ini menggunakan kumpulan ikon resmi dari **Lucide Icons** (<https://lucide.dev/icons>):
- Cari nama ikon di situs Lucide (misal: `award`, `layers`, `mail`, `external-link`).
- Ganti atribut `data-lucide="nama-ikon"`, contoh: `<i data-lucide="book-open"></i>`.

---

## 🌐 Cara Publikasi Gratis ke Internet

Portofolio ini sangat cocok di-hosting secara gratis menggunakan **GitHub Pages**:
1. Buat repositori baru di GitHub (misal: `portofolio` atau `username.github.io`).
2. Unggah file `index.html`.
3. Masuk ke tab **Settings** repositori > **Pages**.
4. Pada opsi *Build and deployment*, pilih branch **main** / root folder `/`.
5. Klik **Save**. Dalam 1-2 menit, portofolio Anda sudah tayang secara publik di internet!
