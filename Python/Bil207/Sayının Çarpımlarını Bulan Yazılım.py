sayi = int(input("0-100 Arası Bir Değer Giriniz: "))

a = 1
b = 0
carpim_sayaci = 0

for i in range(1,sayi+1):
    if sayi%i == 0:
        b = sayi/i
        b = int(b)
        print( str(i) + " x " + str(b) + " = " + str(sayi) )
        carpim_sayaci = carpim_sayaci+1    
    else :
        i+1

print("Toplam " + str(carpim_sayaci) + " farklı çarpım bulunmuştur.")