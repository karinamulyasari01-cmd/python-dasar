# Bab 10: Dictionary
siswa = {"nama": "Karina", "kelas": "X", "nilai": 85}
print(siswa["nama"])

siswa["nilai"] = 90
siswa["hobi"] = "membaca"
print(siswa)

for kunci, isi in siswa.items():
    print(kunci, "=", isi)
