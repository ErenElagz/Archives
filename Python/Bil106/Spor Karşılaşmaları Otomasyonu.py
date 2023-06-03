print("Spor Karşılaşmaları Otomasyonu")
from abc import ABC, abstractmethod

class Sport():
    @abstractmethod
    def mac_sonucu(cls):
        pass

oyuncu_listesi = []

class Player(Sport):
    def __init__(self,isim,soyisim,dogum_tarihi,o1,o2,o3):
        self._isim           = isim
        self._soyisim        = soyisim
        self._dogum_tarihi   = dogum_tarihi
        self._o1             = o1
        self._o2             = o2 
        self._o3             = o3

    def OzellikleriDuzenle(self):
        self._o1 = input("Yeni Bir özellik Giriniz: ")
        self._o2 = input("Yeni Bir özellik Giriniz: ")
        self._o3 = input("Yeni Bir özellik Giriniz: ")
    
    def OyuncuBilgileriniDuzenle(self):
        self._isim           = input("İsmi Düzenleyin: ")
        self._soyisim        = input("Soyİsmi Düzenleyin: ")
        self._dogum_tarihi   = int(input("Dogum Tarihini Düzenleyin: "))

    def OyuncuBilgisi(self):
        print(self._isim, self._soyisim + " isimli oyuncunun dogum tarihi: ",str(self._dogum_tarihi))
        print("Özellikleri:" ,self._o1,self._o2,self._o3)
        print("- - - - - - - - - - - -")


    def ListeyeEkle(self):
        self.oyuncu = self._isim + self._soyisim
        oyuncu_listesi.append(self.oyuncu)

class Team(Sport):
    def __init__(self,isim,kurulus_tarihi,oynadiği_oyun,aldiği_sayi,yediği_sayi,puan):
        self._isim           = isim
        self._kurulus_tarihi = kurulus_tarihi
        self._oynadigi_oyun  = oynadiği_oyun
        self._aldigi_sayi    = aldiği_sayi
        self._yedigi_sayi    = yediği_sayi
        self._puan           = puan

    def TakimBilgisiDuzenle(self):
        self._isim           =  input("Yeni Takım Adı Giriniz: ")
        self._kurulus_tarihi =  input("Yeni Kurulus Tarihi Giriniz: ")

    def MacDetaylariDuzenle(self):
        self._oynadigi_oyun = int(input("Oynanan Oyun sayısını Girinizz: "))
        self._aldigi_sayi   = int(input("Macta kac sayı aldı: "))
        self._yedigi_sayi   = int(input("Macta kac sayı yediz: "))
        self._puan          = int(input("Güncel Skor: "))

    def TakimBilgisi(self):
        print(self._isim + " adlı takımın kurulus tarihi: ",str(self._kurulus_tarihi))
        print("Aldigi Sayı: " , str(self._aldigi_sayi))
        print("Yedigi Sayı: " , str(self._yedigi_sayi))
        print("Güncel Puanı: ", str(self._puan))
        print("- - - - - - - - - - - -")

    def TakimaOyunculari(self):
        print(str(oyuncu_listesi))

o1 = Player("Eren","Elagoz",2003,"Sert Şut","Depar","Savunma")
o2 = Player("Lorem","Ipsum",2001,"Gard","Çalım","Ofansif")
o3 = Player("Amor","Fati",2000,"Uzun Pas","Kondisyon","Dengeli")

t1 = Team("Besiktas",1903,16,41,28,36)
t2 = Team("Galatasaray",1905,14,39,31,40)
t3 = Team("Fenerbahce",1907,18,57,30,46)


for i in [o1,o2,o3]:
    i.OyuncuBilgisi()

for i in [t1,t2,t3]:
    i.TakimBilgisi()