class Urun():
    def __init__(self,isim):
        self.isim = isim
        self.alis   = 0
        self.satis  = 0
        self.miktar = 0
        
    def urunismi(self):
        return self.isim
        
    def urun_miktari(self):
        return self.miktar   
        
    def urun_ekle(self):
        miktar = int(input(self.isim + " için kaç tane ürün eklemek istersiniz: "))
        self.miktar = self.miktar + miktar     
        
    def urun_kaldir(self):
        miktar = int(input(self.isim + " için kaç tane ürün kaldırmak istersiniz: "))
        self.miktar = self.miktar - miktar
    
    def urunleri_listele():        
        for i in urunler:
            return "{0} adlı ürün için {1} adet stok vardır.".format(str(i),i.urun_miktari())
    
    def alis_fiyati(self):
        self.alis  = int(input(self.isim + " Yeni Alış fiyatını giriniz: "))  
    
    def satis_fiyati(self):
        self.satis = int(input(self.isim + " Yeni Satış fiyatını giriniz: ")) 
        
        
class Denge():
    def __init__(self,para):
        self.para = para
    
    def gelir_ekle(self):
        gelen = int(input("Cüzdana ne kadar para eklendi: "))
        self.para =self.para + gelen            
    
    def gelir_azalt(self):
        giden = int(input("Cüzdandan ne kadar para eksildi: "))
        self.para =self.para + giden            
    
    def cuzdan_goruntule(self):
        return str(self.para)
        
        
para = Denge(1000)        
urunler =[]

urunler.append(Urun("Gomlek"))
urunler.append(Urun("Pantolon"))

while True :
    print("---------------------------")
    print("Lütfen bir işlem seçiniz")
    print("1- Ürün Alımı")
    print("2- Ürün Satımı")
    print("3- Ürünleri Listele")
    print("4- Ürün Fiyatlarını Güncelle")
    print("5- Sermayeyi Görüntüle")
    print("0- Çıkış")
    secim = int(input("Bir sayı giriniz: "))
    print("---------------------------")

    if  secim == 0:
        break

    elif secim == 1:
        print("Bir ürün seçiniz")
        print("0- Gömlek")
        print("1- Pantolon")
        urunsecim = int(input("Bir sayı giriniz: "))
        
        urunmiktari = urunler[urunsecim].urun_miktari()
        print(str(urunmiktari) + " adet ürün vardır")   
        urunmiktari = urunler[urunsecim].urun_ekle() 
        print(str(urunmiktari) + " adet ürün olarak güncellenmiştir")   
        
    elif secim ==2:
        print( "Bir ürün seçiniz")
        print("0- Gömlek")
        print("1- Pantolon")
        urunsecim =int(input("Bir sayı giriniz: "))

        urunmiktari = urunler[urunsecim].urun_miktari()
        print(str(urunmiktari) + " adet ürün vardır")   
        urunmiktari = urunler[urunsecim].urun_kaldir()
        print(str(urunmiktari) + " adet ürün olarak güncellenmiştir")   
        

    elif secim == 3:
        for i in urunler:
            print("{0} adlı ürün için {1} adet stok vardır.".format(str(i),str(i.urun_miktari())))

    elif secim == 4:
        for i in urunler:
            i.alis_fiyati()
            i.satis_fiyati()

    elif secim == 5 :  
        print("Kalan sermayeniz : " + str(para.cuzdan_goruntule()))       
        
    else :
        print("Hata! Lütfen belirtilen tuşlardan birini giriniz")   
        
        
    
    