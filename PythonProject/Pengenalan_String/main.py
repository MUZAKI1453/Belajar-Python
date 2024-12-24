data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
    1. dengan menggunakan sigle  quote '...'
    2. dengan menggunakan double quote "..."
"""

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print("'ini contoh string'")
print('"ini contoh string juga"')

# 2. menggunakan tanda \ (back slash)

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('isn\'t it ?')
print('g\'day')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\tmakan\tlontong")
print("aku\tlapar")

# backspace
print("ma     \bkan")

# newline
print("baris pertama\nbaris kedua")
print("baris ketiga\r\nbaris keempat")

# 3. string literal atau raw


# menggunakan raw string -> r
print(r'C:\new \t\r\b\\folder')

# multiline literal string
print("""
        nama : usup
        kelas : 3 sd
        """)

# multiline literal string dan raw
print(r"""
            nama : usup
            kelas : 3 sd
            """)
