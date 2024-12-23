# operasi assignment adalah operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment
from operator import truediv

a = 5 # ini adalah assignment
print("nilai a = ", a)

a += 1 # ini artinya adalah a = a + 1
print("nilai a += 1, nilainya a menjadi ", a)

a -= 2 # ini artinya a = a - 2
print("nilai a -= 2,  nilainya a menjadi ", a)

a *= 5 # ini artinya a = a * 5
print("nilai a *= 5, nilainya a menjadi ", a)

a /= 2 # ini artinya a = a / 2
print("nilai a /= 2, nilainya a menjadi ", a)

b = 10

b %= 3 # ini artinya b = b % 3
print("nilai a %= 3, nilainya a menjadi ", b)

c = 10
c //= 3 # ini artinya c = c // 3, habis pembagian sisa bagi
print("nilai c //= 3, nilainya c menjadi ", c)

d = 5
d **= 3 # ini artinya a = a * a * a
print("nilai d **= 3, nilainya d menjadi ", d)

# operasi bitwise

# OR
c = True
print("\nnilai c = ", c)
c |= False
print("nilai c |= False, nilainya c menjadi ", c)

# and
c = True
print("\nnilai c = ", c)
c &= True
print("nilai c &= True, nilainya c menjadi ", c)
c &= False
print("nilai c &= False, nilainya c menjadi ", c)

# xor
c = True
print("\nnilai c = ", c)
c ^= True
print("nilai c ^= True, nilainya c menjadi ", c)
c ^= False
print("nilai c ^= False, nilainya c menjadi ", c)


# shifting / geser - geser
f = 0b0100
print("\nnilai f = ", format(f, '04b'))
f >>= 2
print("nilai f >>= 2, nilainya f menjadi ", format(f, '04b'))