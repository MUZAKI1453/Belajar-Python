# if dan else statement merupakan contoh dari control flow

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("Siapa nama anda : ?")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline
#if nama == "ucup" : print("kamu ganteng !")
#print("akhir dari program")

# 2. program if indentation
if nama == "ucup":
    print(f"{nama} kamu ganteng banget !")
    print(f"{nama} kamu keren banget !")
print(f"terima kasih {nama}")

# 3. else statement
if nama == "diks":
    print(f"{nama} kamu pemain fc copanhagen")
    print(f"{nama} kamu pemain timnas indonesia")
else :
    print(f"{nama} kamu bukan pemain fc copanhagen")
    print(f"{nama} kamu bukan pemain timans indonesia")