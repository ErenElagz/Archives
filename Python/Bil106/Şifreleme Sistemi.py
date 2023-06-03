from abc import ABC, abstractmethod
import hashlib

text = "sifre"
hash_object = hashlib.md5(text.encode())
print("{} text verisinin md5 ile şifrelenmiş hali: {}".format(text,hash_object.hexdigest()))

class KontrolPanel:
    def __init__(self,isim,surum,url,sifre,durum):
        self.isim = isim
        self.surum =surum
        self.url =url
        self.sifre = hashlib.md5(sifre.encode())
        self.durum = False
    
    @abstractmethod
    def giris_yap(self):
        pass
    
    @abstractmethod
    def oturum_kontrol(self):
        pass
    
class VeriTabani(KontrolPanel):
    def __init__(self,veritabani_ismi,isim,surum,url,sifre,durum):
        self.isim = isim
        self.surum =surum
        self.url =url
        self.sifre = hash_object.hexdigest
        self.durum = False  
        
        self.liste = []
        self.tablo_sayısı=0
    def giris_yap(self,x):
        self.x = x
        
    def oturum_kontrol(self):
        if hashlib.md5(self.x.encode()) == self.sifre() :
            print("sifre basarılı")
        else:
            print("sifre yanlis")
    
    def yeni_tablo_ekle(self,ty):
        self.liste.append(ty)
    
    def tablo_sayisi_artir(self):
        self.tablo_sayısı=+1

class Sunucu(KontrolPanel):
    def __init__(self,isim,surum,url,sifre,durum):
        self.isim  = " "
        self.surum = " "
        self.url   = " "
        self.sifre = hash_object.hexdigest
        self.durum = False    
    
    def giris_yap(self,x):
        self.x = x
    
    def oturum_kontrol(self):
        if self.x == text :
            print("sifre basarılı")
        else:
            print("sifre yanlis")   
            
    def iki_farkli_sunucunun_versiyonlarini_goster(self):
        print(self.isim + " iisimli sunucunun  versiyonu: " + self.surum)

veritabani1 = VeriTabani("Mysql","12.01","127.0.0.1/mysql","veritabanisifresi","Otomasion","Dnemee")
sunucu1 = Sunucu("Apache","59.1","127.0.0.1/apache","apachesifresi","ry")
sunucu2 = Sunucu("Cats","12.54","127.0.0.1/cats","catssifre","try")


for i in [veritabani1,sunucu1,sunucu2]:
    i.giris_yap(input("sifre girniz: "))
    i.oturum_kontrol()

for i in [sunucu1,sunucu2]:
    i.iki_farkli_sunucunun_versiyonlarini_goster()
    
veritabani1.yeni_tablo_ekle("ogrenciler")
veritabani1.tablo_sayisi_artir()
veritabani1.yeni_tablo_ekle("siniflar")
veritabani1.tablo_sayisi_artir()













    