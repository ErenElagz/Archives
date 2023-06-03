# Kanal Linki 
# https://www.youtube.com/channel/UCSuZoI3MYLXn0VZn7IJagTA
# upload uzun sürdügü iciç biraz zmaana alcak benim icin lain kanaldaki videolar kısmından izelyebilirsiniz
from abc import ABC, abstractmethod

doktorverisi = []
hastaverisi = []

uzmanliklar = []
ilaclar = []

class Hastane(ABC):
    def __init__(self,isim):        
        self.isim = isim

class Doktor(Hastane):
    def __init__(self,isim,unvan):
        super().__init__(isim)
        self.unvan = unvan
        
    def UzmanlikEkle (self,uzmanlik):
        self.uzmanlik = uzmanlik 
        uzmanliklar.append(self.uzmanlik)

    def ListeyeEkle(self):    
        veri = str(self.isim + " adlı doktorun ünvanı " + self.unvan + " . Uzmanlıkları ise şöyledir : " + str(uzmanliklar))
        doktorverisi.append(veri)

    def BilgileriYazdir(self):
        print("- - - - - - - - -")   
        print("DoktorAdı: " + self.isim)
        print("Ünvanı: " + self.unvan)
        print("UzmanlıkAlanı: " + str(uzmanliklar))
        print(doktorverisi)
        print("- - - - - - - - -")        

class Hasta(Hastane):
    def __init__(self,isim,hastalik):
        super().__init__(isim)

        self.isim = isim
        self.hastalik = hastalik

    def ListeyeEkle(self):
        hastaveri = (self.isim + " adlı hastanın hastalığı " + self.hastalik + " kullandığı ilaçlar " + self.ilac + "verem doktorlar " + self.verendoktor )
        hastaverisi.append(hastaveri)

    def Ilac(self,ilac,verendoktor):
        self.ilac = ilac
        self.verendoktor = verendoktor
             
    def BilgileriYazdir(self):
        print("- - - - - - - - -")   
        print("HastaAdı: " + self.isim)
        print("Hastalık: " + self.hastalik)
        print("Kullandığı İlac: " + self.ilac)
        print("Veren Doktor: " + self.verendoktor)
        print(hastaverisi)
        print("- - - - - - - - -")        

hasta1 = Hasta("ErenElagoz","Grip")
hasta1.Ilac("Vermidon","AykutElmas")

hasta2 = Hasta("denemeelagoz","bas agrisi")
hasta2.Ilac("parol","denmee")

doktor1 = Doktor("AykutElmas","Profesör")
doktor1.UzmanlikEkle("GenelCerrah")
doktor1.UzmanlikEkle("DişDoktoru")

hasta1.ListeyeEkle()
hasta1.BilgileriYazdir()

hasta2.ListeyeEkle()
hasta2.BilgileriYazdir()

doktor1.ListeyeEkle()
doktor1.BilgileriYazdir()

print(hastaverisi)












