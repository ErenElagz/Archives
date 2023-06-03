from mimetypes import init


class Araba():
    def __init__(self,marka,model,uretim_yili,benzin_kapasitesi,kalan_benzin):
        self.marka             = marka
        self.model             = model
        self.uretim_yili       = uretim_yili
        self.benzin_kapasitesi = benzin_kapasitesi
        self.kalan_benzin      = 0
    
    def print(self):
        print(self.marka + " markanın " + self.model + " modelindeki aracın üretim yılı: "+str(self.uretim_yili)+ " benzin kapasitesi: " + str(self.benzin_kapasitesi) + " kalan benzini ise: " + str(self.kalan_benzin))

    def set_marka(self,yeni_deger):
        self.marka = yeni_deger
    def get_marka(self):
        print(self.marka)

    def set_model(self,yeni_deger):
        self.model = yeni_deger
    def get_model(self):
        print(self.model)    
    
    def set_yil(self,yeni_deger):
        self.yil = yeni_deger
    def get_yil(self):
        print(str(self.yil))

    def set_benzin_kap(self,yeni_deger):
        self.benzin_kapasitesi = yeni_deger
    def get_benzin_kap(self):
        print(str(self.benzin_kapasitesi))

    def set_kalan_benzin(self,yeni_deger):
        if yeni_deger > self.benzin_kapasitesi:
            print("benzin kapasitesinin üzerinde değer girildi. lütfen tekrar deneyin")
        else:
            self.kalan_benzin = yeni_deger

    def get_kalan_benzin(self):
        print(str(self.kalan_benzin))

    def arttir_kalan_benzin(self,yeni_deger):
        if yeni_deger + self.kalan_benzin >= self.benzin_kapasitesi:
            print("benzin kapasitesinin üzerine çıkıldı. lütfen tekrar deneyin")
        else:
            self.kalan_benzin = yeni_deger + self.kalan_benzin 

car1 = Araba("ford","connect",2012,40,0)

car1.get_benzin_kap()
car1.set_benzin_kap(50)
car1.get_benzin_kap()
car1.get_kalan_benzin()
car1.set_kalan_benzin(20)
car1.arttir_kalan_benzin(15)
car1.get_kalan_benzin()
car1.print()