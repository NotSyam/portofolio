import asyncio
import os
import edge_tts

# ==============================================================================
# KONFIGURASI SUARA
# Pilihan suara Bahasa Indonesia resmi Microsoft:
# 1. "id-ID-GadisNeural" (Suara Wanita: ramah, jelas, instruksional) -> DEFAULT
# 2. "id-ID-ArdiNeural"  (Suara Pria: formal, tegas, berwibawa)
# ==============================================================================
VOICE = "id-ID-GadisNeural"

# Kecepatan bicara (opsional: "+0%", "+5%", "-5%")
RATE = "+0%"

# Folder tujuan penyimpanan file MP3
OUTPUT_DIR = "audio"

# ==============================================================================
# NASKAH SUARA LENGKAP UNIT 00 - UNIT 10
# ==============================================================================
SCRIPTS = {
    0: (
        "Selamat datang di Modul Orientasi Pegawai ASN Kementerian Agama Republik Indonesia. "
        "Modul pembelajaran mandiri ini dirancang oleh Pusbangkom MKMB untuk mengenalkan struktur, kedudukan, "
        "serta arah pengembangan karir Anda sebagai abdi negara. Silakan klik tombol Mulai Pembelajaran untuk memulai orientasi."
    ),
    1: (
        "Sebelum melangkah lebih jauh, mari cermati peta alur pembelajaran berikut. "
        "Terdapat sebelas unit materi yang harus Anda selesaikan secara berurutan. "
        "Setiap unit memiliki aktivitas interaktif dan syarat membaca minimal sepuluh detik agar pintu evaluasi akhir dapat terbuka."
    ),
    2: (
        "Kementerian Agama menaungi lebih dari sepuluh ribu satuan kerja di seluruh pelosok nusantara. "
        "Saat ini, kekuatan SDM kita diperkuat oleh tiga ratus delapan puluh tujuh ribu lebih aparatur sipil negara, "
        "yang terdiri dari enam puluh empat persen PNS dan tiga puluh enam persen PPPK. "
        "Silakan jawab kuis singkat di bawah untuk melanjutkan."
    ),
    3: (
        "PNS dan PPPK merupakan dua jalur pengabdian ASN dengan status hukum yang jelas. "
        "PNS diangkat secara tetap, sedangkan PPPK diangkat berdasarkan perjanjian kerja berkala. "
        "Keduanya memiliki NIP nasional dan hak pengembangan kompetensi yang setara. "
        "Silakan klik tab komparasi untuk mencermati perbedaannya."
    ),
    4: (
        "Jabatan ASN bukan sekadar kedudukan di atas kertas. "
        "Jabatan mencakup lima pilar mandat akuntabilitas, yaitu: Fungsi, Tugas, Tanggung Jawab, Wewenang, dan Hak, "
        "atau disingkat F-T-T-W-H. Silakan ketuk kelima kata kunci pada layar untuk memahami maknanya."
    ),
    5: (
        "Secara garis besar, rumpun jabatan ASN terbagi menjadi dua kelompok. "
        "Kelompok Manajerial memiliki peran memimpin unit dan mengarahkan bawahan, mulai dari JPT, Administrator, hingga Pengawas. "
        "Sedangkan kelompok Non-Manajerial berfokus pada kompetensi keahlian fungsional dan teknis pelayanan."
    ),
    6: (
        "Ciri khas Kementerian Agama terletak pada dominasi Jabatan Fungsional yang mencapai delapan puluh enam persen, "
        "mulai dari Guru, Dosen, hingga Penyuluh Agama. Terdapat lima puluh lima varian jabatan fungsional di instansi kita. "
        "Coba cari dan tandai nama jabatan Anda pada daftar pencarian."
    ),
    7: (
        "Batas usia pensiun aparatur ditentukan oleh kelompok jabatannya. "
        "Pejabat Pimpinan Tinggi purna tugas pada usia enam puluh tahun, sedangkan Administrator, Pengawas, "
        "dan Pelaksana pada usia lima puluh delapan tahun. Silakan balik keempat kartu informasi untuk mencermati aturannya."
    ),
    8: (
        "Mobilitas karir ASN bersifat dinamis melalui tiga arah perpindahan: "
        "Horizontal untuk posisi yang setara, Vertikal untuk promosi dalam satu kelompok, "
        "serta Diagonal untuk promosi lintas kelompok jabatan. Selesaikan ketiga skenario perpindahan di layar untuk membuka unit berikutnya."
    ),
    9: (
        "Saatnya menguji pemahaman Anda melalui kuis akhir. "
        "Terdapat delapan butir soal pilihan ganda dengan ambang batas kelulusan minimal tujuh puluh lima persen atau enam jawaban benar. "
        "Cermati setiap pertanyaan dengan saksama. Selamat mengerjakan!"
    ),
    10: (
        "Selamat! Anda telah sukses menuntaskan seluruh rangkaian orientasi Pengenalan Jabatan ASN Kementerian Agama. "
        "Pegang teguh nilai-nilai BerAKHLAK dan jadilah aparatur yang berintegritas serta melayani dengan ikhlas. "
        "Jangan lupa kunjungi portal resmi PTA Kemenag untuk informasi karir lebih lanjut."
    ),
}

async def generate_single_audio(unit_id: int, text: str):
    """Men-generate 1 file audio menggunakan edge-tts"""
    output_path = os.path.join(OUTPUT_DIR, f"unit_{unit_id}.mp3")
    print(f"🎙️  [{unit_id + 1:02d}/11] Memproses Unit {unit_id:02d} -> {output_path} ...", end=" ", flush=True)

    try:
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(output_path)
        print("✅ Berhasil!")
    except Exception as e:
        print(f"❌ Gagal: {e}")

async def main():
    # Buat folder output jika belum ada
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 60)
    print("🚀 MEMULAI GENERASI AUDIO NARASI OTOMATIS (EDGE-TTS)")
    print(f"🗣️  Voice: {VOICE} | Kecepatan: {RATE}")
    print(f"📁 Folder Output: ./{OUTPUT_DIR}/")
    print("=" * 60)

    # Looping 11 unit secara berurutan
    for unit_id, text in SCRIPTS.items():
        await generate_single_audio(unit_id, text)

    print("=" * 60)
    print("🎉 SEMUA AUDIO TELAH SELESAI DIGENERATE!")
    print(f"Silakan periksa folder '{OUTPUT_DIR}' Anda.")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())