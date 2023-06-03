print("Sayının çarpanlarını bulan program")

sayi = int(input("Bir sayı giriniz: "))
 
for i in range(1,sayi+1):
    if sayi % i == 0:
        print(i)