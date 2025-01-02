# break

# contoh pertama
print("contoh pertama")
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice !")
        break

    print("hello !")

print("the end")

# contoh kedua
print("\ncontoh kedua")
angka = 0
data_int = int(input("hitung sampai = "))

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("nice !")
        break

    print("hallo !")

print("The end")