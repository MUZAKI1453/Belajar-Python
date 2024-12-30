# latihan Date and Time
import datetime as dt

print("silahkan masukkan tanggal,\nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan   = int(input("Bulan   \t:"))
tahun   = int(input("Tahun   \t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"umur anda adalah : {umur_tahun} tahun")