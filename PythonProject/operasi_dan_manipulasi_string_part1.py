# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "muhamad"
nama_tengah  = "arif"
nama_akhir   = "muzaki"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string
a = "jaja mi harja"
b = "jaja"
status = b in a
print(b + " ada di " + a + " = " + str(status))

# mengulang string
print("wk" * 3)
print(3 * "wk")

# indexing
z = "ztsubatsaz"
print("index ke  2 : " + z[1])
print("index ke  3 : " + z[5])
print("index ke -1 : " + z[-1])
print("index ke -2 : " + z[-2])
print("index ke [0:3] : " + z[0:3]) # indexing dengan menggunakan rentang
print("index ke [4:8] : " + z[4:8]) # menggunakan : sebagai mencsri rentang
print("indexing ke 0,2,4,6 : " + z[0:10:2])

# item string paling kecil
c = "aku"
print("item string paling kecil : " + min(c))
# item string paling besar
print("item string paling besar : " + max(c))

# operator dalam bentuk  method
data   = "ular meliur-liur melulur bulu ular"
jumlah = data.count("u")
print("jumalah u pada " + data + " = " + str(jumlah))