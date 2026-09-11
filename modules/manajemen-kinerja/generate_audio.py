#!/usr/bin/env python3
"""
Edge-TTS Audio Narration Generator for Pengenalan Manajemen Kinerja PPPK
Generates 16 MP3 audio files using id-ID-GadisNeural
"""

import asyncio
import os
import sys
import json
import argparse

VOICE_DEFAULT = "id-ID-GadisNeural"

NARRATIONS = {
    "0": "Selamat datang di Modul Pengenalan Manajemen Kinerja Pegawai ASN dan PPPK. Modul ini dirancang khusus untuk memandu Anda memahami siklus pengelolaan kinerja berbasis ekspektasi pimpinan dan regulasi terkini. Mari kita mulai perjalanan belajar bersama.",
    "1": "Berikut adalah peta pembelajaran manajemen kinerja kita yang terbagi ke dalam empat pilar pokok bahasan: perencanaan, pelaksanaan dan pemantauan, penilaian kinerja, serta tindak lanjut evaluasi. Pelajari setiap tahapan dengan tuntas.",
    "2": "Pengelolaan kinerja aparatur berlandaskan pada lima prinsip umum. Kinerja bukan lagi sekadar penilaian masa lalu, melainkan instrumen pengembangan diri dan pemenuhan ekspektasi pimpinan secara berkelanjutan.",
    "3": "Perencanaan kinerja diawali dengan dialog kinerja intensif antara pimpinan dan pegawai. Hasil kesepakatan dialog ini kemudian dituangkan dalam penyusunan dan penetapan Sasaran Kinerja Pegawai atau SKP.",
    "4": "Mari kita pelajari penyelarasan kinerja organisasi ke individu melalui pohon kinerja atau cascading. Sasaran strategis jangka panjang nasional diturunkan ke Renstra, Perjanjian Kinerja, hingga SKP jabatan fungsional Anda.",
    "5": "Penyusunan SKP mencakup delapan tahapan terstruktur, mulai dari menelaah Renstra dan Perjanjian Kinerja, membagi peran hasil kerja, menetapkan prioritas rencana kerja, hingga menyepakati sumber daya pendukung.",
    "6": "Pada unit audit ini, Anda diajak mengidentifikasi enam permasalahan umum dalam pengisian e-Kinerja tahun 2025. Cermati lembar simulasi dan temukan kekeliruan formulasi kata kerja serta bukti dukung.",
    "7": "Inginkah nilai e-Kinerja Anda melampaui ekspektasi pimpinan? Cermati tips strategis pada kartu interaktif berikut, mulai dari pemahaman mekanisme sistem hingga kolaborasi dan etika kerja harian.",
    "8": "Penilaian kinerja pegawai dinilai dari dua komponen kunci, yaitu aspek hasil kerja atau Key Performance Indicators dan aspek perilaku kerja core values BerAKHLAK yang memberi manfaat nyata bagi organisasi.",
    "9": "Surat Edaran Menpan RB Nomor 3 Tahun 2023 mengatur pola distribusi predikat kinerja pegawai. Gunakan simulator sandbox untuk melihat bagaimana capaian unit kerja Anda membatasi kuota predikat individu.",
    "10": "Pelaporan kinerja pegawai diwujudkan dalam Dokumen Evaluasi Kinerja Pegawai Format D.1.1. Perhatikan batas waktu legal empat belas hari kerja penyampaian oleh penilai dan pengembalian oleh pegawai.",
    "11": "Pemeringkatan kinerja dilakukan oleh Tim Penilai Kinerja untuk menyusun profil kinerja pegawai dalam satu unit kerja sebagai dasar pemetaan talenta aparatur.",
    "12": "Apabila merasa penilaian yang diberikan belum objektif, pegawai memiliki hak mengajukan keberatan secara berjenjang. Jalankan simulasi linimasa berikut dalam batasan hari kerja resmi.",
    "13": "Kinerja unggul mendatangkan apresiasi seperti kelompok rencana suksesi dan pembayaran tunjangan kinerja. Sebaliknya, bagi PPPK, ketidaktercapaian target perjanjian kerja berakibat pada pemutusan hubungan kerja.",
    "14": "Saatnya membuktikan ketuntasan kompetensi Anda melalui Kuis Evaluasi Akhir. Jawablah butir pertanyaan skenario ini dengan teliti untuk mencapai batas nilai kelulusan minimal tujuh puluh lima persen.",
    "15": "Selamat atas keberhasilan Anda menyelesaikan seluruh rangkaian modul manajemen kinerja. Terus pegang teguh prinsip objektivitas, transparansi, dan komitmen pelayanan terbaik bagi umat dan bangsa."
}

async def generate_audio_file(unit_id, text, output_path, voice, rate="+0%"):
    import edge_tts
    print(f"[*] Generating unit_{unit_id}.mp3 ({len(text)} chars)...")
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_path)
    print(f" [OK] Saved: {output_path}")

async def main_async(args):
    try:
        import edge_tts
    except ImportError:
        print("[!] Error: 'edge-tts' belum terinstall. Jalankan: pip install edge-tts")
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    voice = args.voice

    targets = NARRATIONS.items()
    if args.unit is not None:
        u_key = str(args.unit)
        if u_key not in NARRATIONS:
            print(f"[!] Unit {args.unit} tidak ditemukan.")
            sys.exit(1)
        targets = [(u_key, NARRATIONS[u_key])]

    print(f"=== Menghasilkan Audio Narasi ({len(targets)} unit) ===")
    print(f"Voice: {voice} | Output: {os.path.abspath(args.output_dir)}")
    print("-" * 50)

    for unit_id, text in targets:
        out_file = os.path.join(args.output_dir, f"unit_{unit_id}.mp3")
        try:
            await generate_audio_file(unit_id, text, out_file, voice, rate=args.rate)
        except Exception as e:
            print(f"[X] Gagal membuat audio unit {unit_id}: {e}")

    print("-" * 50)
    print("[OK] Seluruh audio narasi berhasil diproduksi!")

def main():
    parser = argparse.ArgumentParser(description="Edge-TTS Narration Generator for Manajemen Kinerja PPPK")
    parser.add_argument("--voice", default=VOICE_DEFAULT, help=f"Suara Edge-TTS. Default: {VOICE_DEFAULT}")
    parser.add_argument("--rate", default="+0%", help="Kecepatan. Default: +0%%")
    parser.add_argument("--output-dir", default="./audio", help="Folder output audio")
    parser.add_argument("--unit", type=int, help="ID unit spesifik (opsional)")

    args = parser.parse_args()
    asyncio.run(main_async(args))

if __name__ == "__main__":
    main()
