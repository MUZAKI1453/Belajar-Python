# Latihan Perulangan Membuat Segitiga



# 1. menggunakan for
print(20 * "=")
print("\n1. menggunakan for")

sisi = 5

# dummy variable
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

# 2. menggunakan while
print(20 * "=")
print("\n2. menggunakan while")

# cara 1
print("\ncara 1")
# dummy variable
count = 1
while count <= sisi:
    print("*" * count)
    count += 1

# cara 2
print("\ncara 2")

sisi = 5

# dummy variabel
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

# 3. hanya ganjil saja
print(20 * "=")
print("\n3. hanya ganjil saja")

sisi = 10

# dummy variable
count = 1
while True:
    if (count % 2):
        # print jika ganjil
        print("*" * count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break


# 4. membuat segitiga sama kaki

print(20 * "=")
print("\n4. membuat segitiga sama kaki")

sisi = 10
spasi = int(sisi/2)
# dummy variable
count = 1
while True:
    if (count % 2):
        # print jika ganjil
        print(" " * spasi, "*" * count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break




