# continue, pass, break

# loop biasa
print("A. loop biasa")
angka = 0

while angka < 4:
    angka += 1
    if angka == 3:
        print("Hello !")

    print(angka)

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi / tdk akan diimplementasikan
print("\nB. loop dengan pass")
angka = 1

while angka < 4:
    angka += 1
    if angka == 3:
        pass # ini tdk akan dieksekusi

    print(angka)


# continue
print("\nC. loop dengan continue")
angka = 0

while angka < 4:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice to meet you to")
        continue

    print("nice to meet you")

print("bye!")