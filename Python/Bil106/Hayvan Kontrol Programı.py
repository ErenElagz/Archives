print("Hayvan Kontrol Programı")

hayvanlar_listesi = []
toplam_hayvan_sayisi = 0

class Hayvanlar():
    def __init__(self,tur,yas,boy):
        self.isim = " "
        self.tur = tur
        self.yas = yas
        self.boy = boy

    def hayvanlar_listesine_ekle(self):
        veri = ( self.isim + " adlı hayvan " + str(self.tur) + " türünde olup" + " boyu: " + str(self.boy)  + " yası: " + str(self.yas))
        hayvanlar_listesi.append(veri)

    def arttir_hayvan_sayisi(self):
        toplam_hayvan_sayisi = toplam_hayvan_sayisi + 1

    def hayvan_ismi_guncelle(self,isim):
        self.isim = isim
    
    def hayvan_ismini_yazdir(self):
        print("Hayvan İsmi: "+ self.isim)

    def hayvan_sayisini_yazdir():
        print("Hayvan Sayısı: " + str(len(hayvanlar_listesi)))

    def hayvanlari_listele(self):
        print(str(hayvanlar_listesi))
    
    def metre_cinsinden_nesne_olustur(self,tur,yas,metre):
        self.tur = " "
        self.yas = " "
        self.metre = " "
        self.boy = int(self.metre*100)

hayvan1 = Hayvanlar("Deve",3,100)
hayvan1.hayvan_ismi_guncelle("Camel")
hayvan1.hayvan_ismini_yazdir()
hayvan1.hayvanlar_listesine_ekle()

hayvan2 = Hayvanlar("Koyun",5,25)
hayvan2.hayvan_ismi_guncelle("Sheep")
hayvan2.hayvan_ismini_yazdir()
hayvan2.hayvanlar_listesine_ekle()


hayvan3 =Hayvanlar("Tavuk",13,0.3)
hayvan3.hayvan_ismi_guncelle("Chicken")
hayvan3.hayvan_ismini_yazdir()
hayvan3.hayvanlar_listesine_ekle()


print(str(hayvanlar_listesi))

Hayvanlar.hayvan_sayisini_yazdir()
