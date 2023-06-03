from abc import ABC, abstractmethod
from csv import list_dialects 

print("Kütüphane Otomasyonu uygulaması")

class Kutuphane(ABC):
    def __init__(self,isim):
        self.isim =isim

class Kitap(Kutuphane):
    def __init__(self, isim,yazar,yil):
        super().__init__(isim)
        self.yazar = yazar
        self.yil   = yil

    @classmethod
    def ismi_duzenle(self):
        self.isim =input("Yeni İsim Giriniz: ")
    
    def yili_duzenle(self):
        self.yil =input("Yeni Yılı Giriniz: ")

    def yazari_duzenle(self):
        self.yazar =input("Yeni Yazarı Giriniz: ")

    def bilgi(self):

        print("{} adlı kitabın yazarı {} ve çıkış tarihi {} 'dur ".format(self.isim,self.yazar,self.yil))

class Dergi(Kutuphane):
    def __init__(self, isim,yillar):
        super().__init__(isim)
        self.yillar =yillar
        self.yazar_listesi  = []
        self.editor_listesi = []

    def ismi_duzenle(self):
        self.isim =input("Yeni İsim Giriniz: ")

    def yazar_ekle(self):
        self.yazar_listesi.append(input("Yazar Giriniz"))

    def editor_ekle(self):
        self.editor_listesi.append(input("Editor Giriniz"))

    def bilgi(self):
        print("- - - - - - - - - - - - - - - - -")
        print("{} adlı kitabın yazarları {}, editorleri {} ve çıkış tarihi {} 'dur ".format(self.isim,self.yazar_listesi,self.editor_listesi,self.yillar))


k1 = Kitap("Otomatik Portakal","Anthony Burgess",1962)
k2 = Kitap("Hayvan Çiftliği","George Orwell",1945)

d1 = Dergi("SpaceX","yılda 3 kez")
d1.editor_ekle()
d1.yazar_ekle()

d2 = Dergi("National Geographic",1962)
d2.editor_ekle()
d2.yazar_ekle()

for i in [k1,k2]:
    i.bilgi()

for i in [d1,d2]:
    i.bilgi()