import numpy as np

class MatrisClass():
    def __init__(self,satir,sutun):
        self.satir = satir
        self.sutun = sutun
        self.matris = []

        #matris 1 in boyutlandırılması 
        for i in range(2):
            for j in range(2):
                eleman1= int(input("{}. boyut {}. satırı giriniz: ".format(i,j)))
                self.matris.append(eleman1)
        self.matris = np.array(self.matris).reshape(2,2)

    def indekse_gore_guncelle(self):
        self.matris_yazdir()
        print("Hangi Satırı Düzenlemek İstiyorsunuz.")
        x = int(input("Kacıncı Satır? "))
        y = int(input("Kacıncı Sutun? "))
        print(self.matris[x,y])
        yeni_deger = int(input("Yeni Degeri Girin: "))
        self.matris[x,y] = yeni_deger

    def deger_getir(self,x,y):
        print("Matrisin İstenen Degerleri:",self.matris[x,y])

    def satir_getir(self):
        print(self.satir)
    
    def sutun_getir(self):
        print(self.sutun)

    def matris_yazdir(self):
        print(self.matris)

    def matris_ile_nesne_olustur(satir,sutun):
        matris_nesne = np.array(matris_nesne).reshape(2,2)

def iki_matrisi_carpma_ve_yazdir(x,y):
    sonuc = np.multiply(x,y)
    print(sonuc)

matris = MatrisClass([],[])
matris.matris_yazdir()
matris.deger_getir(1,0)

matris2 = MatrisClass([],[])
matris2.matris_yazdir()

matris.indekse_gore_guncelle()
print(matris.matris)

iki_matrisi_carpma_ve_yazdir(matris,matris2)