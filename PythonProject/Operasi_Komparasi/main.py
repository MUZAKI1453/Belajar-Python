""" 1. Operasi Komparasi digunakan untuk membandingkan nilai.
    2. hasil dari operasi komparasi adalah boolean,
       sehingga nilai nya akan ada True dan False.
    3. operatornya adalah :
       > , < , >= , <= , == , != , is , is not """

a = 4
b = 2

# lebih besar dari >
print("======= lebih besar dari (>) =======")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari <
print("========== kurang dari (<) ==========")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih dari sama dengan >=
print("===== lebih dari sama dengan (>=) =====")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari sama dengan >=
print("===== kurang dari sama dengan (<=) =====")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan ==
print("========== sama dengan (==) ==========")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = a == 3
print(a, '==', 3, '=', hasil)

# tidak sama dengan !=
print("========== tidak sama dengan (!=) ==========")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = a != 3
print(a, '!=', 3, '=', hasil)

# 'is' sebagai komparasi object identity
print("======= ini adalah object identity (is) =======")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ', x, ' ,id = ', hex(id(x)))
print('nilai y = ', y, ' ,id = ', hex(id(y)))
hasil = x is y
print('hasil x is y = ', hasil)

# 'is' sebagai komparasi object identity
print("==== ini adalah object identity (is not) ====")
x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ', x, ' ,id = ', hex(id(x)))
print('nilai y = ', y, ' ,id = ', hex(id(y)))
hasil = x is not y
print('hasil x is y = ', hasil)


