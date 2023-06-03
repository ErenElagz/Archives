print("Geometri Programı")

class Geometri():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.kenar= []

class DikPri(Geometri):
    def kenarlari_gir(self):
        self.x = int(input("ilk boyutu giriniz: "))
        self.y = int(input("ikinci boyutu giriniz: "))
        self.z = int(input("üçüncü boyutu giriniz: "))

    def kenarlari_listele(self):
        print("- - - - - - - - - - - - - - - ")
        print("Birinci Kenar Uzunluğu: " + str(self.x))
        print("İkinci  Kenar Uzunluğu: " + str(self.y))
        print("Üçüncü  Kenar Uzunluğu: " + str(self.z))

    def hacim_hesapla(self):
        self.hacim = (self.x)*(self.y)*(self.z)

    def alan_hesapla(self):
        self.alan = 2*((self.x*self.y)+(self.x*self.z)+(self.y*self.z))

    def cevre_hesapla(self):
        self.cevre =  ((self.x)+(self.y)+(self.z))*4

    def hesaplamalar(self):
        print("- - - - - - - - - - - - - - - ")
        print("Şeklin Hacmi:   "+ str(self.hacim))
        print("Şeklin Alanı:   "+ str(self.alan ))
        print("Şeklin Çevresi: "+ str(self.cevre))

dort1=DikPri()
dort1.kenarlari_gir()
dort1.kenarlari_listele()
dort1.hacim_hesapla()
dort1.alan_hesapla()
dort1.cevre_hesapla()
dort1.hesaplamalar()