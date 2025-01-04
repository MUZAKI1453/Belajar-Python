print("=" * 60)
print("kumpulan data yang berurutan dan dapat diubah(mutable)")

# kumpulan data numbers
print("\n1. Kumpulan data numbers")
data_angka = [1,2,3,5,4]
print(f"\tini adalah list data numbers : {data_angka}")
print("\ttipe datanya adalah : ", type(data_angka))

# kumpulan data string
print("\n2. kumpulan data string")
data_string = ["struick, romeny, diks"]
print(f"\tini adalah list data string : {data_string}")
print("\ttipe datanya adalah : ", type(data_string))

# kumpulan data boolean
print("\n3. kumpulan data boolean")
data_boolean = [True, False, True, True]
print(f"\tini adalah list data boolean : {data_boolean}")
print("\ttipe datanya adalah : ", type(data_boolean))

# kumpulan data campuran
print("\n4. kumpulan data campuran")
data_campuran =["struick", 23, 44, "diks", False, True, 12, "romeny"]
print(f"\tini adalah list data campuran : {data_campuran}")
print("\ttipe datanya adalah : ", type(data_campuran))

# cara alternatif membuat list
print("\n5. cara alternatif membuat list")
data_range = range(0,10,2) # range awal, range akhir, step
print(f"\tini adalah data range  : {data_range}")
print("\ttipe datanya adalah : ", type(data_range))
data_list = list(data_range) # casting data range ke list
print("\ttipe datanya setelah diubah menjadi list adalah : ", type(data_list))
print(f"\tdata nya adalah : {data_list}")

#  membuat list dengan for loop, list comprehension
print("\n6. membuat list dengan for loop, list comprehension")
list_pake_for = [i for i in range(0,10)]
print(f"\tini adalah list dengan for loop : {list_pake_for}")
print("\ttipe datanya adalah : ", type(list_pake_for))

# membuat list dengan for loop dan if
print("\n7. membuat list dengan for loop dan if")
list_comprehensif = [i for i in range(0, 10) if i != 5]
print(f"\tini adalah list dengan for loop dan if : {list_comprehensif}")














