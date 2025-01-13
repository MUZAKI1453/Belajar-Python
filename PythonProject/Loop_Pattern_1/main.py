tinggi = 5
counter = 1

for baris in range(1, tinggi + 1):
    for kolom in range(1, baris + 1):
        print(counter, end=' ')
        counter += 1
    print()