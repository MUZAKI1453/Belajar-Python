# latiham konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nProgram Konversi Temperature\n")
celcius = float(input("Masukan Suhu dalam Celcius : "))
print("Suhu adalah : ", celcius, "Celcius")

# reamur
reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah : ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu dalam fahrenheit : ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin : ", kelvin, "Kelvin")