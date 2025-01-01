# Latihan Membuat Kalkulator Sederhana

# 1.mengambil data user berupa : angka 1, angka2, dan operator
# 2.percabangan menggunakan if, elif, dan else
# 3.menampilkan hasil dari kalkulator

print(10 * "=")
print("Kalkulator Sederhana")

angka_1  = float(input("masukkan angka ke-1 = "))
operator = input("operator (+, -, x, /) : ")
angka_2  = float(input("masukkan angka ke-2 = "))


if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasil nya adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah = {hasil}")
else :
    print("maaf, salah input, coba ulangi")



