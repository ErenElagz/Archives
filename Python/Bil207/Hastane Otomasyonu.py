from abc import ABC, abstractmethod

class Hastane(ABC):
    def __init__(self,isim):
        super().__init__()
        self.isim = isim
        self.doktorlar = []
        self.hastalar = []
    
    def doktorEkle(self,doktor):
            self.doktorlar.append(doktor)

    def hastaEkle(self,hasta):
        self.hastalar.append(hasta)


    @abstractmethod
    def Yazdır():
        pass

class Doktor(Hastane):
    def __init__(self,isim,unvan,uzmanlık_alanları):
        super().__init__(isim)
        self.unvan = unvan
        self.uzmanlık_alanları = uzmanlık_alanları

    def Yazdır(self):
        print("Doktor adı           :",self.isim)
        print("Doktor unvanı        :",self.unvan)
        print("Doktorun uzmanlıkları:",self.uzmanlık_alanları)
    
    @staticmethod
    def Uzmanlık_Ekle():
        pass
    
    def unvanListele(self):
            print(self.unvan)

    def uzmanlikListele(self):
            print(self.uzmanlık_alanları)     

class Hasta(Hastane):
    def __init__(self,isim,hastalık,ilaclar):
        super().__init__(isim)
        self.hastalık = hastalık
        self.ilaclar = ilaclar

    def Yazdır(self):
        print("Hasta adı           :",self.isim)
        print("Hasta hastalığı     :",self.hastalık)
        print("Kullandığı ilaçlar  :",self.ilaclar)

    def ilacEkle(self):
        self.ilaclar = input("İlaç giriniz :")


    def hastalikEkle(self):
        self.hastalik = input("Hastalik giriniz:")

    def hastalikListele(self):
        print("hastalik : ",self.hastalik)

    def ilaclarListele(self):
           return("ilaclar :",self.ilaclar)


doktor_1 = Doktor("Eren","Prof",["Göz Sağlığı","Kulak Burun Boğaz"])
doktor_2 = Doktor("Eray","Doçent",["Kalp Sağlığı"])
doktor_3 = Doktor("Tolga","Ogrenci",["Diş Hastalıkları"])
doktor_listesi = [doktor_1,doktor_2,doktor_3]

hasta_1  = Hasta("Emre","Bel Ağrısı",{"krem": "Eren",
                                      "kas gevşetici": "Eray",
                                      })
hasta_2  = Hasta("Ahmet","Baş Ağrısı",{"parol": "Eren",
                                      })

hasta_3  = Hasta("Emre","Bel Ağrısı",{"antibiyotik": "Eren",
                                      "kas gevşetici": "Eray",
                                      })

hasta_listesi = [hasta_1,hasta_2,hasta_3]


for i in hasta_listesi:
    print("----------------")
    i.Yazdır()

for i in doktor_listesi:
    print("----------------")
    i.Yazdır()

doktor_1.doktorEkle("Emre")
doktor_2.doktorEkle("Emre")
doktor_3.doktorEkle("Emre")
hasta_1.hastaEkle("Atakan")
hasta_2.hastaEkle("Atakan")
hasta_3.hastaEkle("Atakan")

hasta_1.hastalikListele()
Doktor.doktorListele()
hasta_1.hastaListele()
hasta_1.ilaclarListele()