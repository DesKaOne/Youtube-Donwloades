import yt_dlp
from pathlib import Path


# ============================================================
# CONFIG
# ============================================================

OUTPUT_DIR = Path("music")
URLS_FILE = Path("urls.txt")
FAILED_FILE = Path("failed.txt")

# Bitrate MP3:
# 128, 192, 256, 320
MP3_BITRATE = "128"

# Audio:
SAMPLE_RATE = "44100"
CHANNELS = "2"


# ============================================================
# PREPARE
# ============================================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not URLS_FILE.exists():
    print(f"File {URLS_FILE} tidak ditemukan.")
    raise SystemExit(1)


with URLS_FILE.open("r", encoding="utf-8") as f:
    urls = [
        line.strip()
        for line in f
        if line.strip() and not line.lstrip().startswith("#")
    ]


if not urls:
    print("Tidak ada URL di urls.txt")
    raise SystemExit(0)


print("=" * 60)
print(" YouTube → MP3 Downloader")
print("=" * 60)
print(f"Total URL    : {len(urls)}")
print(f"Output       : {OUTPUT_DIR.resolve()}")
print(f"MP3          : {MP3_BITRATE} kbps CBR")
print(f"Sample Rate  : {SAMPLE_RATE} Hz")
print(f"Channel      : Stereo")
print("=" * 60)


# ============================================================
# YT-DLP OPTIONS
# ============================================================

options = {

    # Ambil audio terbaik yang tersedia
    "format": "bestaudio/best",

    # Nama file berdasarkan judul video
    "outtmpl": str(
        OUTPUT_DIR / "%(title)s.%(ext)s"
    ),

    # Playlist diperbolehkan
    "noplaylist": False,

    # Catat video yang sudah berhasil didownload
    "download_archive": "archive.txt",

    # Jangan download ulang file yang sudah ada
    "overwrites": False,

    # Download tetap bisa dilanjutkan
    "continuedl": True,

    # JavaScript runtime untuk YouTube
    "js_runtimes": {
        "deno": {}
    },

    # Retry otomatis
    "retries": 5,
    "fragment_retries": 5,

    # Kalau ada error, lanjut ke URL berikutnya
    "ignoreerrors": True,

    # ========================================================
    # CONVERT AUDIO
    # ========================================================

    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": MP3_BITRATE,
        }
    ],

    # Paksa format audio agar kompatibilitas maksimal
    "postprocessor_args": [
        "-ar", SAMPLE_RATE,
        "-ac", CHANNELS,
        "-b:a", f"{MP3_BITRATE}k",
    ],

    # Output normal yt-dlp
    "quiet": False,

    # Jangan tampilkan warning terlalu banyak
    "no_warnings": False,
}


# ============================================================
# DOWNLOAD
# ============================================================

failed_urls = []


with yt_dlp.YoutubeDL(options) as ydl:

    for i, url in enumerate(urls, 1):

        print()
        print("=" * 60)
        print(f"[{i}/{len(urls)}]")
        print(f"URL: {url}")
        print("=" * 60)

        try:

            result = ydl.download([url])

            # yt-dlp biasanya mengembalikan 0 jika sukses
            if result not in (None, 0):
                failed_urls.append(url)

        except Exception as e:

            print()
            print(f"GAGAL: {e}")
            failed_urls.append(url)


# ============================================================
# SAVE FAILED URL
# ============================================================

if failed_urls:

    with FAILED_FILE.open("w", encoding="utf-8") as f:
        for url in failed_urls:
            f.write(url + "\n")

    print()
    print("=" * 60)
    print(f"Ada {len(failed_urls)} URL yang gagal.")
    print(f"Daftar disimpan di: {FAILED_FILE}")
    print("=" * 60)

else:

    # Hapus failed.txt lama jika semua sukses
    if FAILED_FILE.exists():
        FAILED_FILE.unlink()

    print()
    print("=" * 60)
    print("SEMUA DOWNLOAD BERHASIL 😁")
    print("=" * 60)


print()
print("Selesai.")
