# operasi logika atau boolean
# not, or, and, xor

# NOT
print("=== NOT ===")
a = True
b = not a
print("data a = ", a)
print("----------NOT")
print("data c = ", b)

print("")

# OR = jika salah satu bernilai true, maka hasilnya true
print("=== OR ===")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)

a = True
b = True
c = a or b
print(a, ' OR', b, '=', c)

print("")

# and = jika 2 buah nilai true, maka hasil true
# atau jika salah satu false maka hasilnya false
print("=== and ===")
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)

a = False
b = True
c = a and b
print(a, 'and', b, '=', c)

a = True
b = False
c = a and b
print(a, ' and', b, '=', c)

a = True
b = True
c = a and b
print(a, ' and', b, '=', c)

print("")

# XOR = nilainya akan true jika salah satu true, sisanya false
print("=== XOR ===")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, ' XOR', b, '=', c)