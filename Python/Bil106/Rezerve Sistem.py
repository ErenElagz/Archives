print("10 kişilik olan bir minibüste rezerve yapılan program")

bos   = [1,2,3,4,5,6,7,8,9,10]
dolu  = []

while True:
    print("- - - - - - - - - - - - - - - ")
    print("rezerve olan koltuklar: " + str(dolu))
    print("rezerve olmayan koltuklar: " +str(bos))
    print("- - - - - - - - - - - - - - - ")

    secim = int(input("Lütfen rezerve edeceğiniz numarayı giriniz(sıfıra basıp cıkış yapabilirsiniz): "))

    if secim == 0:
        break

    elif 1<= secim <=10 :
        if secim in dolu:
            print("bu kolyuk alınmış")
        else:    
            bos.remove(secim)
            dolu.append(secim)
        
    else:
        print("Hatalı koltuk numarası. Lütfen sadece belirlenen koltukları giriniz")

