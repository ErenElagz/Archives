kelime =input("Lütfen kelime giriniz: ") #input
buyuk=kelime.upper()  #kelimeyi büyük harfere çevirme
a=1
while a <= len(buyuk):
    for i in buyuk:
        print(a*"*"+i)   #her harften önce birden başlayacak sekilde 2 şer attirarak alt alta yazdırma
        a=a+2    #döngü sinirlari