import os
import asyncio
import edge_tts

OUTPUT_DIR = 'audio_berakhlak'
VOICE = 'id-ID-GadisNeural'
RATE = '+0%'

SCRIPTS = {
    0: (
        'Selamat datang di Modul Pembelajaran Interaktif Penerapan Tugas dan Fungsi ASN di Tempat Kerja. '
        'Modul yang dikembangkan oleh Pusbangkom MKMB ini dirancang untuk menanamkan Core Values BerAKHLAK '
        'ke dalam budaya kerja dan tata kelola digital di lingkungan Kementerian Agama. '
        'Silakan klik tombol Mulai Pembelajaran untuk mengawali modul ini.'
    ),
    1: (
        'Sebelum melangkah lebih jauh, mari cermati peta alur pembelajaran berikut. '
        'Terdapat sebelas unit pembelajaran terstruktur yang memadukan teori nilai BerAKHLAK '
        'dengan studi kasus riil tata kelola digital Kementerian Agama. '
        'Selesaikan seluruh aktivitas interaktif untuk membuka evaluasi akhir.'
    ),
    2: (
        'Core Values BerAKHLAK diluncurkan sebagai fondasi moral bersama seluruh ASN di Indonesia '
        'dengan semboyan Bangga Melayani Bangsa. Nilai-nilai luhur ini ditopang oleh lima prinsip utama, '
        'mulai dari pemberian layanan publik yang prima, integritas tanpa kompromi, '
        'hingga inovasi yang adaptif terhadap dinamika zaman. Cermati kelima prinsip tersebut pada layar Anda.'
    ),
    3: (
        'Pada era kekinian, nilai Berorientasi Pelayanan diwujudkan nyata melalui digitalisasi layanan keagamaan, '
        'seperti pendaftaran haji daring, sertifikasi halal digital, dan pencatatan nikah online. '
        'Sementara nilai Akuntabel dijaga melalui transparansi proses, fitur pelacakan berkas secara langsung, '
        'dan keterbukaan menerima umpan balik dari masyarakat.'
    ),
    4: (
        'Lima nilai berikutnya saling menopang tugas harian kita. ASN Kemenag dituntut Kompeten melalui peningkatan literasi teknologi, '
        'Harmonis dalam merajut moderasi beragama di ruang digital, Loyal menjalankan kebijakan nasional, '
        'Adaptif menciptakan solusi madrasah cerdas, serta Kolaboratif menggandeng komunitas dan pemangku kepentingan demi pelayanan terbaik.'
    ),
    5: (
        'Di Kementerian Agama, transformasi digital telah mengakar ke dalam lima ekosistem utama. '
        'Mulai dari satu pintu aplikasi super Pusaka, modernisasi data pendidikan madrasah lewat EMIS, '
        'pengelolaan zakat dan wakaf digital, layanan konsultasi keagamaan berbasis kecerdasan buatan, '
        'hingga perizinan dan sertifikasi halal yang cepat tanpa tatap muka.'
    ),
    6: (
        'Keberhasilan sistem digital diukur dari seberapa banyak masyarakat yang terbantu. '
        'Untuk mempercepat adopsi teknologi, Kemenag merangkul para tokoh agama dan penyuluh di lapangan, '
        'menghadirkan antarmuka aplikasi yang mudah dipahami oleh semua kalangan, '
        'serta mengintegrasikannya dengan kanal komunikasi populer seperti WhatsApp dan pembayaran digital.'
    ),
    7: (
        'Perjalanan transformasi digital tidak lepas dari tantangan besar. '
        'Kita menghadapi lima hambatan utama: kesiapan budaya kerja sebagian aparatur, '
        'keterbatasan infrastruktur internet di daerah pelosok, ancaman keamanan data pribadi, '
        'keterpaduan antar aplikasi yang masih terkotak-kotak, serta keragaman tingkat literasi masyarakat pengguna layanan.'
    ),
    8: (
        'Sebagai solusi menyeluruh, Kementerian Agama memadukan pelatihan kompetensi SDM dan penguatan infrastruktur siber '
        'dengan pendekatan tata kelola keagamaan. Nilai-nilai luhur agama dijadikan pedoman moral pemanfaatan teknologi, '
        'dengan komitmen mutlak bahwa seluruh layanan digital harus inklusif dan dapat diakses dengan setara oleh seluruh umat beragama.'
    ),
    9: (
        'Mari uji kepekaan etika Anda dalam skenario nyata di tempat kerja. '
        'Seorang warga membutuhkan panduan layanan perizinan digital di kantor Anda. '
        'Cermati situasinya dan pilih keputusan yang paling mencerminkan nilai Berorientasi Pelayanan dan Harmonis.'
    ),
    10: (
        'Saatnya membuktikan pemahaman Anda melalui evaluasi akhir. '
        'Terdapat delapan butir soal pilihan ganda yang menguji esensi nilai BerAKHLAK dan penerapannya '
        'di lingkungan kerja Kementerian Agama. Cermati setiap butir soal dengan saksama. Selamat mengerjakan!'
    ),
    11: (
        'Selamat! Anda telah sukses menyelesaikan modul Penerapan Tugas dan Fungsi ASN di Tempat Kerja. '
        'Ingatlah selalu bahwa teknologi hanyalah sarana, sedangkan ruh pelayanan terletak pada integritas dan ketulusan hati kita. '
        'Mari jadikan Core Values BerAKHLAK sebagai napas dalam setiap langkah pengabdian di Kementerian Agama Republik Indonesia.'
    )
}

async def generate_single(uid, text):
    out = os.path.join(OUTPUT_DIR, f'unit_{uid}.mp3')
    print(f'🎙️  [{uid + 1:02d}/12] Memproses Unit {uid:02d} -> {out} ...', end=' ', flush=True)
    try:
        comm = edge_tts.Communicate(text, VOICE, rate=RATE)
        await comm.save(out)
        print('✅ Berhasil!')
    except Exception as e:
        print(f'❌ Gagal: {e}')

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print('=' * 65)
    print('🚀 GENERASI AUDIO MODUL PENERAPAN TUGAS DAN FUNGSI ASN (BERAKHLAK)')
    print(f'🗣️  Voice: {VOICE} | Folder: ./{OUTPUT_DIR}/')
    print('=' * 65)
    for uid, text in SCRIPTS.items():
        await generate_single(uid, text)
    print('=' * 65)
    print('🎉 SEMUA 12 FILE AUDIO TELAH SELESAI DIGENERATE!')
    print('=' * 65)

if __name__ == '__main__':
    asyncio.run(main())
