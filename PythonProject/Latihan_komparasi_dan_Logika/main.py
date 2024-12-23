# episode latihan logika dankomparasi
# membuat gabungan areaa rentang dari angka

inputUser = float(input("masukan angka yang bernilai kurang dari 3 "
                        "atau lebih dari 10 : "))

# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 : ", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 : ", isLebihDari)

# memeriksa angka lebih dari 10 atau kurang dari 3
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ", isCorrect)

print("\n", 10 * "=", "\n")
inputUser = float(input("masukan angka yang bernilai lebih dari 3 "
                        "atau kurang dari 10 : "))

# memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print("lebih dari 3 : ", isLebihDari)

# memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)
print("kurang dari 10 : ", isKurangDari)

# memeriksa angka lebih dari 3 dan kurang dari 10
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan : ", isCorrect)
