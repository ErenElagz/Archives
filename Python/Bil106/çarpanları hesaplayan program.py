ust_sinir = int(input("bir sayi giriniz ")) #en buyuk degeri isteme
liste = [] #liste olusturma

for sayi in range(1,ust_sinir):  
    #en buyuk deger ile 1 arasindadki tüm sayilari teker teker modüler bölme ile eğer kalan sifir ise atlayarak degilse listeye atarak deniyor taa ki son degere kadar
   if sayi > 1:  
       for i in range(2,sayi):  
           if (sayi % i) == 0:  #moduler bolme eger kalan 0 ise
               break  # sayı atlanıyor
       else:  
           liste.append(sayi) #degile  asal sayilari listeye ekliyor
           
print( str(len(liste)) + " Adet asal sayı bulundu" ) #listenin uzunluğunu hesaplayarak kac tane oldugunu yazdırıyor
print(liste) #ekrana yazdırma