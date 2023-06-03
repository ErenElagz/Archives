sayi = input("Lütfen sayı giriniz: ") #deger girme
a = len(str(sayi)) #a değişkenine sayinin basamak sayisiını atama

while a >= 1:
    for i in sayi:
        print( i + (a-1) * "0" ) #basamak sayisini a dan bir azaltarak olusturma
        a = a-1  #döngünün sınırları 