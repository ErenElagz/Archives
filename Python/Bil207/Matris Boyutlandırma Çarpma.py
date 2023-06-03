import numpy as np

#matris 1
satir1 = int(input("1. Matris İçin Kaç Satırlı Matris Oluşturulsun: "))
sutun1 = int(input("1. Matris İçin Kaç Sütunlu Matris Oluşturulsun: "))
matris1 = []

#matris 1 in boyutlandırılması 
for i in range(satir1):
    for j in range(sutun1):
        eleman1= int(input("{}. boyut {}. satırı giriniz: ".format(i,j)))
        matris1.append(eleman1)
matris1 = np.array(matris1).reshape(satir1,sutun1)
print("1. matris")
print(matris1)

#matris carpım kuralı icin uyarı
satir2 = sutun1
print("matris çarpımının olması için 2. dizinin satır sayısı " + str(sutun1) + " olarak belirlenmiştir." )

#matris 2
sutun2 = int(input("2. Matris İçin Kaç Sütunlu Matris Oluşturulsun: "))
matris2 = []

# matris 2 nin boyutlandırılması
for i in range(satir2):
    for j in range(sutun2):
        eleman2= int(input("{}. boyut {}. satırı giriniz: ".format(i,j)))
        matris2.append(eleman2)
matris2 = np.array(matris2).reshape(satir2,sutun2)
print("2. matris")
print(matris2)

#Matris Carpımı
res = np.dot (matris1, matris2)
print("\nMatris Carpım Sonucu:")
print(res)