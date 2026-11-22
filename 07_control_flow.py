# Bab 7: Control Flow
nilai = 85
if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
else:
    print("Grade C")

for i in range(1, 6):
    print("For ke-", i)

n = 3
while n > 0:
    print("Hitung mundur:", n)
    n -= 1

for i in range(10):
    if i == 3:
        continue
    if i == 6:
        break
    print("i =", i)
