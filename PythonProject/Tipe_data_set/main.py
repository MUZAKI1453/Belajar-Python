# Program untuk mengelola anggota klub menggunakan tipe data set

# mendefinisikan 2 set anggota klub
club = {"jajang", "sukirman", "maman", "didi"}
national_team = {"jajang", "sadiman", "maman", "revaldi", "yayan", "didi"}

# menampilkan anggota gabungan dari kedua club
anggota_gabungan = club.union(national_team)
print("anggota gabungan club dan national team : ", anggota_gabungan)

# menampilkan anggota yang merupakan anggota keduanya (irisan)
anggota_bersama = club.intersection(national_team)
print("anggota bersama club dan national team : ", anggota_bersama)

# menampilkan anggota yang hanya terdapat di club
anggota_club = club.difference(national_team)
print("anggota club : ", anggota_club)

# menampilkan anggota yang hanya terdapat di national team
anggota_national = national_team.difference(club)
print("anggota national team : ", anggota_national)