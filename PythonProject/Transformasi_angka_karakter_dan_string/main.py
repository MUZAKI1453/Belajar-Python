print(50 * "=")
# Transformasi Angka, Karakter, dan String
print("Transformasi Angka, Karakter, dan String")

# 1. mengubah huruf besar dan kecil
print("\n1. mengubah huruf besar dan kecil")
teks = "HelLo WOrLd"
print("\ta. upper() = ", teks.upper())
print("\tb. lower() = ", teks.lower())

# 2. menghapus spasi putih
print("\n2. menghapus spasi putih")
kata_2 = "  hallo dunia  "
print("\ta. strip()  -> menghapus spasi putih diawal dan diakhir string = ", kata_2.strip())
print("\tb. lstrip() -> menghapus spasi putih diawal string             = ", kata_2.lstrip())
print("\tc. rstrip() -> menghapus spasi putih diakhir string            = ", kata_2.rstrip())

# 3. mengubah string menjadi list menggunakan method split()
print("\n3. mengubah string menjadi list")
teks = "hallo.dunia.sekarang"
teks_2 = "hallo dunia sekarang"

daftar_kata = teks.split(".") # memisahkan menggunakan titik
print("\ta. memisahkan / split menggunakan titik(.) = ", daftar_kata)
daftar_kata_2 = teks_2.split(" ") # memisahkan menggunakan spasi
print("\tb. memisahkan / split menggunakan spasi    = ", daftar_kata_2)

# 4. mengubah list menjadi string menggunakan method join()
print("\n4. mengubah list menjadi string")
daftar_kata = ['Hallo','dunia','sekarang']
teks = ','.join(daftar_kata)
print("\ta. mengubah list menjadi string = ", teks)

# 5. konversi list ke string tanpa menggunakan join()
print("\n5. konversi list ke string tanpa menggunakan join(), menggunakan loop")
daftar_kata = ['Hello','dunia','sekarang']
teks = ''
for kata in daftar_kata:
    teks += kata
print(f"\tkonversi list ke string tanpa menggunakan join() = {teks}")

# 6. konversi tipe data angka ke string dan sebaliknya
print("\n6. konversi tipe data ke string dan sebaliknya")
# tipe data angka ke string
angka = 2003
print("\ttipe data dari angka sebelum di casting ke string = ", type(angka))
teks = str(angka) # casting dari angka ke string
print("\ttipe data dari angka sesudah di casting ke string = ", type(teks), "yaitu = ", teks)

# tipe data string ke angka
angka = "2009"
print("\ttipe data dari string sebelum di casting ke angka / int = ", type(angka))
teks = int(angka)
print("\ttipe data dari string sesudah di casting ke angka / int = ", type(teks), "yaitu = ", teks)

# tipe data string ke float
teks = "2.50"
angka = float(teks)
print("\ttipe data dari string sebelum di casting ke angka / float = ", type(teks))
print("\ttipe data dari string sesudah di casting ke angka / float = ", type(angka), "yaitu = ", angka)

# 7. konversi string ke list karakter
print("\n7. konversi string ke list karakter")
teks = "python"
list_karakter = [karakter for karakter in teks]
print(f"\tlist karakter = {list_karakter}")

# 8. konversi string ke tuple
print("\n8. konversi string ke tuple")
teks = "python"
tuple_karakter = tuple(teks)
print(f"\ttuple karakter = {tuple_karakter}")

# 9. konversi list ke string tanpa pemisah
print("\n9. konversi list ke string tanpa pemisah")
daftar_angka = [1,3,2,5,6,4,2,1,8,11,2]
set_angka = set(daftar_angka)
print(f"\tlist ke string tanpa pemisah = {set_angka}")

# 10. konversi string heksadesimal ke integer
print("\n10. konversi string hexadesimal ke integer")
teks_hex = '1A'
angka_desimal = int(teks_hex,16)
print(f"\tstring hexsadesimal ke integer = {angka_desimal}")

# 11. konversi integer ke binary, octal, hexadesimal
print("\n11. konversi integer ke binary, octal, hexadesimal")

angka_desimal = 26

teks_binary = bin(angka_desimal)
print(f"\tini desimal ke biner = {teks_binary}")
teks_octal = oct(angka_desimal)
print(f"\tini desimal ke octal = {teks_octal}")
teks_hex = hex(angka_desimal)
print(f"\tini desimal ke hexadesimal = {teks_hex}")







