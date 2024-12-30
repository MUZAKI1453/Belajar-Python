# Date and Time (latihan)

import datetime # import library

hari_ini = datetime.date.today()
print(hari_ini)
# ini menggunakan format string untuk menampilkan hari %A
print(f"hari ini adalah hari = {hari_ini:%A}") 

# contoh import library data and time ke-2
import datetime as dt

tanggal = dt.date(2003,8,9)
print(tanggal)
# ini menggunakan format string untuk menampilkan hari %A
print(f"hari ini adalah hari = {tanggal:%A}")