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
matris1 = np.array(matris1).reshape(satir1*sutun1,1)
print("matris")
print(matris1)

liste1=[]

for i in matris1:
    for x in i:
        liste1.append(x)

liste1.sort()

print("En Buyuk Deger:",liste1[-1])
print("En Kucuk Deger:",liste1[0])

liste1 = np.array(liste1).reshape(satir1*sutun1,1)
a= liste1[0] 
liste1[0] =liste1[-1]
liste1[0]= a

print(liste1)
print(a)