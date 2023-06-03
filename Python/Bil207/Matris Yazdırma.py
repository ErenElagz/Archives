import numpy as np

class Matris():
    def __init__(self,satir,sutun):
        self.satir = 2
        self.sutun = 2

        self.matris1 = []

        #matris 1 in boyutlandırılması 
        for i in range(self.satir):
            for j in range(self.sutun):
                eleman1= int(input("{}. boyut {}. satırı giriniz: ".format(i,j)))
                self.matris1.append(eleman1)
        self.matris1 = np.array(self.matris1).reshape(self.satir,self.sutun)

    def indekse_gore_guncelle(self):
        self.matris_yazdir()
        print("Hangi Satırı Düzenlemek İstiyorsunuz.")


    def deger_getir(self,x,y):
        print(self.matris1[0,0] + "1.sutun 1.satır")
        print(self.matris1[1,0] + "2.sutun 1.satır")
        print(self.matris1[1,0] + "2.sutun 1.satır")
        print(self.matris1[1,1] + "2.sutun 2.satır")

    def satir_getir(self):
        print(self.satir)
    
    def sutun_getir(self):
        print(self.sutun)

    def matris_yazdir(self):
        print(self.satir)
        print(self.sutun)

    def iki_matrisi_toplam_ve_yazdir():
        C = [[0 for i in range(n)] for i in range(m)]
        # İç içe döngü kullanarak karşılıklı elemanların toplanması
        for i in range(m):
            for j in range(n):
                C[i][j] = matris[i][j] + matris3[i][j]
        # Sonucun yazdırılması
        print(C)

    def matris_ile_nesne_olustur(satir,sutun):
        matris2 = np.array(matris2).reshape(satir,sutun)

matris = Matris([],[])
matris.matris_yazdir()
print(matris.matris1)

matris3 = Matris([],[])
matris.matris_yazdir()

