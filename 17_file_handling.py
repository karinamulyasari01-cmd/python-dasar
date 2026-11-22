# Bab 17: File Handling (Read & Write File)
with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

with open("catatan.txt", "a", encoding="utf-8") as f:
    f.write("Baris ketiga\n")

with open("catatan.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("catatan.txt", "r", encoding="utf-8") as f:
    for nomor, baris in enumerate(f, start=1):
        print(nomor, baris.strip())
