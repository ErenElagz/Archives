class Telefon:
    def __init__(self_numara):
        self.__numara = numara
        self.__arananlar_listesi = []
        self.__toplam_konusma_suresi = 0
       
    def arama_gerceklestir(self,aranan_numara):
        sure = int(input("ne kadar konusuldu:"))
        self.__toplam_konusma_suresi +- sure
        self.__arananlar_listesi.append(aranan_numara)
        print(f"{self.__numara} numarali telefon sahibi{aranan_numara} numarasını aradı. konusma suresi: {sure}")
        print(f"gerceklesen toplam arama suresi: {self.__toplam_konusma_suresi}")
        return "telefon numaranız: {}".format(self.telefon)
    def aranan_numarayi_arananlardan_sil(self,aranan_numara):
        for i in self.__arananlar_listesi:
            if i==aranan_numara:
                self.__arananlar_listesi.remove(aranan_numara)
               
    def numarani_goster(self):
        print(f"Telefon numaraniz:{self.__numara}")

telefon=Telefon("5467900420")

telefon.numarani_goster()
   
telefon.arama_gerceklestir("2311234243")
telefon.arama_gerceklestir("3242342342")
telefon.arama_gerceklestir("2131231233")
telefon.arama_gerceklestir("2131231234")
telefon.arama_gerceklestir("1234123124")
telefon.arama_gerceklestir("3243242342")
   
telefon.arananlari_listele()
   
telefon.aranan_numarayi_arananlardan_sil;("2311234243")
telefon.arananlari_listele()