#library ve atama bölümü
import random
x=0
a=0
liste1 = []

#Listeye 100 adet random değer girmek için kullandığım döngü
while x <= 100: 
    a = random.uniform(1,10000) #sayiların float uzunlugu cok uzun oluyor
    h = round(a,2)  # bu nedenle virgülden sonra sadece 2 haneyi alıyoruz bu kodla
    liste1.append(h) #listeye ekleme
    x=x+1
    
    
#I took this function in StackOverFlow.
# https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function

def sort(liste):
    for i in range(len(liste)):                             
        for j in range(len(liste)):
            if liste[i] < liste[j]:
                liste[j],liste[i] = liste[i],liste[j]
    return liste

#Sonucları yazdırma
print(sort(liste1))
