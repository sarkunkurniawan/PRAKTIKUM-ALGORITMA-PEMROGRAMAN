# data = "ini adalah string" 
# print(data) 
# print(type(data))


# # 1. cara membuat string


# '''

# 1.	dengan menggunakan single quote '...'

# 2.	dengan menggunakan double quote "..."

# '''


# data = 'Menggunakan single quote' 
# print(data)


# data = "Menggunakan double quote" 
# print(data)
# print('"Halo, apa kabar?"')

# print("'Halo, apa kabar?'") 
# print("ini adalah hari jum'at")


# # 2. Menggunakan tanda \


# # membuat tanda ' menjadi string print('mari shalat jum\'at') print('g\'day, isn\'t it?')


# # backlash print("C:\\user\\Ucup")


# # tab

# print("ucup\t\t\totong, semakin jauhan")


# # backspace

# print("ucup \botong, jadi deketan")


# # newline

# print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
# print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
# print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

#  3. String literal atau raw


# hati-hati

print('C:\nnew folder') # akan salah pathnya


# menggunakan raw string 
print(r'C:\new folder')


# multiline literal string
print('##############################') 
print("""
NAMA : SARKUN KURNIAWAN 
NIM  : 2270231087
KELAS: A2 T1 INFORMATIKA
""")
print('##############################') 


# multiline literal string dan RAW 
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal 
Website : www.ucup.com/newID 
""")