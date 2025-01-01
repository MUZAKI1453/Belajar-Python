# Perulangan (For loop)

# for kondisi:
#    aksi

angka2_List = [1,2,3,4] # ini adalah list
print(angka2_List)

for i in angka2_List:
    print(f"i sekarang -> {i}")
    
print("ini adalah akhir dari program 1\n")

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("ini adalah akhir dari program 2\n")


# ini menggunakan pembatas awal dan pembatas akhir
angka2_range = range(1,6)

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("ini adalah akhir dari program 3\n")

# perulangan menggunakan string
daftar_string = "aku ganteng"

for huruf in daftar_string:
    print(huruf)
    
print("ini adalah akhir dari program 4\n")

