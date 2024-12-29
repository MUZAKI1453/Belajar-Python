# operator dalam bentuk method

# merubah case dari string

# merubah semua string menjadi upper case (huruf besar)
p = "balap"
print("normal     = " + p)
p = p.upper()
print("gak normal = " + p)

# merubah semua string menjadi lower case (huruf kecil)
p = "MANCING"
print("normal     = " + p)
p = p.lower()
print("gak normal = " + p)

# pengecekan dengan isX method
# contoh pengecekan lower case
p = "balap"
apakah_lower = p.islower() # hasilnya nilai boolean
print(p + (" is lower = ") + str(apakah_lower))
apakah_upper = p.isupper() # hasilnya boolean
print(p + (" is upper = ") + str(apakah_upper))

# isalpha()   <-- untuk mengecek semuanya huruf
# isalnum()   <-- untuk mengecek huruf dan angka saja
# isdecimal() <-- untuk mengecek angka saja
# isspace()   <-- untuk mengecek spasi, tab, newline \n
# istitle()   <-- untuk mengecek semua kata dimulai dengan huruf besar

k = "Aku"
apakah_isalpha = k.isalpha()
print(k + (" isalpha = ") + str(apakah_isalpha))

apakah_isalnum = k.isalnum()
print(k + (" isalnum = ") + str(apakah_isalnum))

apakah_isdecimal = k.isdecimal()
print(k + (" isdecimal = ") + str(apakah_isdecimal))

apakah_isspace = k.isspace()
print(k + (" isspace = ") + str(apakah_isspace))

apakah_istitle = k.istitle()
print(k + (" istitle = ") + str(apakah_istitle))

# mengecek apakah komponen string diawali atau diakhiri dengan string tsb ?
# startswith
cek_start = "python mudah".startswith("python")
print("start = " + str(cek_start))

# endswith
cek_end = "python mudah".endswith("mudah")
print("end = " + str(cek_end))

# penggabungan komponen string pada tipe data list dengan join(), split()
pisah    = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah) # ini dipisahkan oleh koma
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah) # ini dipisahkan oleh spasi
print(gabungan)

gabungan = "akusayangkamu"
print(gabungan.split('sayang'))


# alokasi karakter rjust(), ljust(), center()
# rjust() / rata kanan, right justify
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

# ljust() / rata kiri, left justify
kiri = "kiri".ljust(10)
print("'" + kiri + "'")

# center() / rata tengah, center justify
tengah = "tengah".center(10)
print("'" + tengah + "'")






















