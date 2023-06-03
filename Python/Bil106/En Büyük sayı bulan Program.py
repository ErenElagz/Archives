def en_buyuk_sayi(sayi1,sayi2,sayi3,sayi4,sayi5):
    
    enbuyuk = 0
    
#en buyuk sayı icin karsilastırma
   
    if    (sayi1 > sayi2) and (sayi1 > sayi3) and (sayi1 > sayi4) and (sayi1 > sayi5):
        enbuyuk = sayi1
        
    elif  (sayi2 > sayi3) and (sayi2 > sayi4) and (sayi2 > sayi5):
        enbuyuk = sayi2
        
    elif  (sayi3 > sayi4) and (sayi3 > sayi5):
        enbuyuk = sayi3
        
    elif  (sayi4 > sayi5 ):
        enbuyuk = sayi4
        
    else:
        enbuyuk = sayi5
        
    return enbuyuk 

#degerleri isteme
   
sayi1=float(input("sayı_1 gir  "))

sayi2=float(input("sayı_2 gir  "))

sayi3=float(input("sayı_3 gir  "))

sayi4=float(input("sayı_4 gir  "))

sayi5=float(input("sayı_5 gir  "))

print("liste içindeki en buyuk değer: ", en_buyuk_sayi(sayi1, sayi2, sayi3, sayi4, sayi5))
 
# US ALMA FONKSIYONU

def us_al(us_alınacak_deger,us):
     
    sonuc=1
    
    for i in range(us):
        
        sonuc=sonuc*us_alınacak_deger
        
    return sonuc  

#Deger isteme mekanı

s=float(input("sayıyı gir :  "))

u=int(input("üs gir :   "))

print(us_al(s, u))