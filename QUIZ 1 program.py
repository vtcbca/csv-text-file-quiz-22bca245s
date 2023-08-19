
# # 7.  Write a program to create "intro.txt" file.  Print only even number of row.

# # WRITING 
from csv import writer

info=[["My name is Roshni Singh."],
["I am 18 years old"],
["I live in surat."],
["I Have completed 12th."],
["My hobby is Drawing,travelling,Dancing"],
["I study in VTCBCSR College."],
["I want to become a Software engineer."],
["Currently i am doing BCA."],
["My Favourite colour is Black."],
["My dream place is KEDARNATH."]]
with open("C:\\22bca245\\python\\intro.txt",'w',newline='') as a:
    s=writer(a)
    s.writerows(info)
    print(info)


# # READING FILE
from csv import reader
with open("C:\\22bca245\\python\\intro.txt",'r',newline='') as s:
    a=s.readlines()[::2]
    for i in a:
        print(i)
        



