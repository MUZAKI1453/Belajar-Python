# format string

# contoh generic
# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 0.98
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"

# bilangan dengan ordo ribuan
angka = 30000
format_str = f"ribuan {angka: ,}"
print(format_str)

# bilangan desimal
angka = 34.56433 # --> menampilkan angka dibelakang koma
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan tanda + dan -
angka_minus  = -9
angka_plus   = 10.231
format_minus = f"minus = {angka_minus:-d}"
format_plus  = f"plus  = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)


# memformat persen
persen = 0.07
format_persen = f"persen = {persen:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 20000
jumlah = 2
format_string = f"harga total = rp. {harga * jumlah}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 225
format_binary = f"binary = {bin(angka)}"
format_octal  = f"octal  = {oct(angka)}"
format_hex    = f"hex    = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)












