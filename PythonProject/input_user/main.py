# mengambil input data dari user

# data yang dimasukan pasti string
data = input("masukan data : ")
print("data = " ,data, " ,tipe = " ,type(data))

# jika kita ingin mengambil data integer
data_integer = int(input("masukan data : "))
print("data = " ,data_integer, " ,tipe = " ,type(data_integer))

# jika kita ingin mengambil data boolean
biner = bool(int(input("masukan data : ")))
print("data = " ,biner, " ,tipe = " ,type(biner))