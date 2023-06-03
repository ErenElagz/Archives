sayi = input("Lütfen Sayı Giriniz: ")
toplam = 0

for rakam in str(sayi):
    toplam = toplam + int(rakam)
 
print( "sayının rakamları toplamı: "+ str(toplam))