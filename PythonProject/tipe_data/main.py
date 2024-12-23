# a = 10, a adalah variabel dengan nilai 10

# tipe data standar
# tipe data: angka satuan (integer)
a = 10
print("data : " ,a )
print("bertipe : " ,type(a))

b = 20
print("data : " ,b)
print("bertipe : " ,type(b))

# tipe data: angka dengan koma (float)
c = 12.5
print("data : " ,c)
print("bertipe : " ,type(c))

# tipe data: kumpulan karakter (string)
d = "arif"
print("data : " ,d)
print("bertipe : " ,type(d))

# tipe data: biner = true/false (boolean)
e = True
print("data : " ,e)
print("bertipe : " ,type(e))
f = False
print("data : " ,f)
print("bertipe : " ,type(f))


# tipe data khusus
# bilangan kompleks
g = complex(10,2)
print("data : " ,g)
print("bertipe : " ,type(g))

""" tipe data dari c, bisa digunakan saat kita 
membutuhkan dengan syarat harus import library """

from ctypes import c_double # import library untk variabel double

h = c_double(10.5)
print("data : " ,h)
print("bertipe : " ,type(h))


