# Youtube-Donwloades

Batch YouTube downloader untuk mengunduh audio dari video atau playlist YouTube dan mengubahnya menjadi MP3.

Cocok untuk mengunduh banyak lagu sekaligus tanpa perlu copy URL video satu per satu.

## ✨ Features

- 🎵 Download video YouTube menjadi MP3.
- 📂 Support URL video individual.
- 📜 Support seluruh playlist YouTube.
- 🔁 Tidak mengunduh ulang video yang sudah berhasil diproses.
- 💾 MP3 output:
  - 128 kbps CBR
  - 44.1 kHz
  - Stereo
- 🔄 Automatic retry ketika download gagal.
- ❌ URL yang gagal disimpan ke `failed.txt`.
- 🗃️ Menggunakan `archive.txt` untuk mencatat video yang sudah berhasil diproses.
- ⚡ Menggunakan Deno sebagai JavaScript runtime untuk YouTube extraction.

---

## 📋 Requirements

Pastikan sistem sudah memiliki:

- Python 3.10+
- FFmpeg
- Deno 2.3+
- yt-dlp
- yt-dlp-ejs

### Windows

#### 1. Install Python

Download Python dari:

https://www.python.org/downloads/

Pastikan Python sudah tersedia:

```powershell
python --version
```

Contoh:

```text
Python 3.12.10
```

---

#### 2. Install FFmpeg

Pastikan `ffmpeg` tersedia di PATH.

Cek:

```powershell
ffmpeg -version
```

Jika berhasil, akan muncul informasi versi FFmpeg.

---

#### 3. Install Deno

Jika menggunakan Windows Package Manager:

```powershell
winget install DenoLand.Deno
```

Setelah instalasi selesai, tutup dan buka kembali PowerShell.

Cek:

```powershell
deno --version
```

Disarankan menggunakan Deno 2.3 atau lebih baru.

---

## 📦 Install Python Dependencies

Clone repository:

```powershell
git clone https://github.com/DesKaOne/Youtube-Donwloades.git
```

Masuk ke directory:

```powershell
cd Youtube-Donwloades
```

Install dependency:

```powershell
python -m pip install -U -r requirements.txt
```

Atau langsung:

```powershell
python -m pip install -U "yt-dlp[default]"
```

Cek instalasi:

```powershell
python -m yt_dlp --version
```

Cek EJS:

```powershell
python -m pip show yt-dlp-ejs
```

Cek Deno:

```powershell
deno --version
```

Cek FFmpeg:

```powershell
ffmpeg -version
```

---

# 🚀 Usage

Buat file:

```text
urls.txt
```

Kemudian masukkan URL YouTube.

## Video Individual

Contoh:

```text
https://www.youtube.com/watch?v=XXXXXXXXXXX
https://www.youtube.com/watch?v=YYYYYYYYYYY
https://www.youtube.com/watch?v=ZZZZZZZZZZZ
```

Setiap URL akan diproses menjadi satu file MP3.

---

## Playlist

Tidak perlu memasukkan URL video satu per satu.

Cukup masukkan URL playlist:

```text
https://www.youtube.com/playlist?list=PLXXXXXXXXXXXX
```

Atau URL video yang sekaligus memiliki parameter playlist:

```text
https://www.youtube.com/watch?v=XXXXXXXXXXX&list=PLXXXXXXXXXXXX
```

Program akan memproses seluruh playlist.

Contoh:

```text
Playlist
├── Lagu 01
├── Lagu 02
├── Lagu 03
├── Lagu 04
└── ...
```

Akan menghasilkan:

```text
music/
├── Lagu 01.mp3
├── Lagu 02.mp3
├── Lagu 03.mp3
├── Lagu 04.mp3
└── ...
```

---

# ▶️ Run

Jalankan:

```powershell
python main.py
```

Contoh output:

```text
============================================================
 YouTube → MP3 Downloader
============================================================
Total URL    : 37
Output       : E:\Youtube-Donwloades\music
MP3          : 128 kbps CBR
Sample Rate  : 44100 Hz
Channel      : Stereo
============================================================
```

---

# 🎵 Audio Output

Output audio dikonversi menggunakan FFmpeg menjadi:

```text
Format      : MP3
Bitrate     : 128 kbps CBR
Sample Rate : 44100 Hz
Channel     : Stereo
```

Konfigurasi ini dipilih untuk mendapatkan keseimbangan antara:

- kualitas suara
- ukuran file
- kompatibilitas perangkat
- kapasitas flashdisk / microSD

128 kbps MP3 juga sangat umum digunakan oleh berbagai MP3 player, speaker aktif, head unit, dan perangkat audio lainnya.

---

# 🗃️ Download Archive

Program menggunakan:

```text
archive.txt
```

untuk mencatat video yang sudah berhasil diproses.

Contohnya:

```text
youtube ABC123 has been downloaded
youtube DEF456 has been downloaded
```

Jika program dijalankan kembali, video yang sudah tercatat di archive akan dilewati.

Ini sangat berguna ketika menggunakan playlist.

Misalnya playlist memiliki 100 lagu:

```text
Run #1
100 lagu
↓
100 lagu selesai
```

Kemudian playlist bertambah 5 lagu:

```text
Run #2
100 lagu lama → SKIP
5 lagu baru   → DOWNLOAD
```

Jadi tidak perlu mengunduh ulang semuanya.

---

# ❌ Failed Downloads

Jika terdapat URL yang gagal diproses, URL tersebut akan disimpan ke:

```text
failed.txt
```

Contoh:

```text
https://www.youtube.com/watch?v=XXXXXXXX
https://www.youtube.com/watch?v=YYYYYYYY
```

Setelah masalah selesai, URL tersebut dapat dicoba kembali.

---

# 📁 Directory Structure

Setelah digunakan, struktur directory kurang lebih:

```text
Youtube-Donwloades/
│
├── main.py
├── requirements.txt
├── urls.txt
├── archive.txt
├── failed.txt
│
└── music/
    ├── Lagu 01.mp3
    ├── Lagu 02.mp3
    ├── Lagu 03.mp3
    └── ...
```

`archive.txt` dan `failed.txt` akan dibuat otomatis oleh program.

---

# 💡 Example

Misalnya `urls.txt` berisi:

```text
# Lagu individual
https://www.youtube.com/watch?v=AAAAAAAAAAA

# Playlist
https://www.youtube.com/playlist?list=PLBBBBBBBBBBB

# Playlist lainnya
https://www.youtube.com/watch?v=CCCCCCCCCCC&list=PLDDDDDDDDDDD
```

Kemudian:

```powershell
python main.py
```

Program akan:

```text
Video individual
        ↓
      MP3

Playlist
        ↓
  Semua video
        ↓
      MP3

Video + Playlist
        ↓
  Semua video playlist
        ↓
      MP3
```

---

# ⚙️ Configuration

Konfigurasi utama berada di `main.py`:

```python
MP3_BITRATE = "128"
SAMPLE_RATE = "44100"
CHANNELS = "2"
```

Bitrate dapat diubah jika diperlukan:

```python
MP3_BITRATE = "128"
```

atau:

```python
MP3_BITRATE = "192"
```

atau:

```python
MP3_BITRATE = "256"
```

atau:

```python
MP3_BITRATE = "320"
```

Untuk perangkat audio umum, `128 kbps` sudah cukup dan menghasilkan ukuran file yang lebih kecil.

---

# ⚠️ Copyright

Gunakan program ini hanya untuk konten yang memang boleh Anda unduh atau gunakan.

Pastikan proses pengunduhan, penyimpanan, dan distribusi audio sesuai dengan hak cipta, lisensi, dan ketentuan layanan yang berlaku.

---

# 📜 License

Belum ditentukan.

---

## 👨‍💻 Author

**DesKaOne**

GitHub:

https://github.com/DesKaOne

Repository:

https://github.com/DesKaOne/Youtube-Donwloades