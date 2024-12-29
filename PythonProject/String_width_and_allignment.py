# width and multiline

# Data

data_nama      = "vicky prasetyo"
data_umur      = 34
data_tinggi    = 180
data_no_sepatu = 44
 
# string standar
data_string = f"nama = {data_nama}, umur = {data_umur},tinggi = {data_tinggi}, no sepatu = {data_no_sepatu}"
print("\n" + 5 * "=" + "String Standar" + 5 * "=" )
print(data_string)

# string multiline (dengan menggunakan enter atau newline --> \n)
data_string = f"nama = {data_nama},\numur = {data_umur},\ntinggi = {data_tinggi},\nno sepatu = {data_no_sepatu}"
print("\n" + 5 * "=" + "String Multiline \n" + 5 * "=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama      = {data_nama}
umur      = {data_umur}
tinggi    = {data_tinggi}
no sepatu = {data_no_sepatu}
"""
print("\n" + 5 * "=" + "String Multiline kutip 3" + 5 * "=")
# """ string triplets """
print(data_string)

# merapihkan tampilan data dengan menggeser >5
data_string = f"""
nama      = {data_nama: >5}
umur      = {data_umur: >5}
tinggi    = {data_tinggi: >5}
no sepatu = {data_no_sepatu: >5}
"""
print("\n" + 5 * "=" + "merapihkan tampilan data dengan menggeser >5" + 5 * "=")
# """ string triplets """
print(data_string)