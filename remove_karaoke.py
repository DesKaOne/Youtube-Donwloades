from pathlib import Path

MUSIC_DIR = Path("music")

# Kata yang dianggap menandakan lagu karaoke
KEYWORDS = [
    "karaoke",
    "minus one",
    "instrumental",
    "backing track",
    #"MV",
]

if not MUSIC_DIR.exists():
    print(f"Folder tidak ditemukan: {MUSIC_DIR}")
    raise SystemExit(1)

files = [
    f for f in MUSIC_DIR.iterdir()
    if f.is_file() and f.suffix.lower() == ".mp3"
]

if not files:
    print("Tidak ada file MP3 di folder music.")
    raise SystemExit(0)

print("=" * 60)
print(" Hapus Lagu Karaoke")
print("=" * 60)

matched = []

for file in files:
    name = file.stem.lower()

    if any(keyword.lower() in name for keyword in KEYWORDS):
        matched.append(file)

if not matched:
    print(f"Tidak ditemukan lagu dengan kata '{', '.join(KEYWORDS)}'.")
    raise SystemExit(0)

print(f"Ditemukan {len(matched)} file:")
print()

for file in matched:
    print(f"  - {file.name}")

print()
print("=" * 60)
answer = input("Hapus semua file tersebut? [y/N]: ").strip().lower()

if answer != "y":
    print("Dibatalkan.")
    raise SystemExit(0)

deleted = 0

for file in matched:
    try:
        file.unlink()
        print(f"[HAPUS] {file.name}")
        deleted += 1
    except Exception as e:
        print(f"[GAGAL] {file.name}: {e}")

print()
print("=" * 60)
print(f"Selesai. {deleted} file dihapus.")
print("=" * 60)