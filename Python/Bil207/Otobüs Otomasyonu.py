class Otobus():
    def __init__(self,otobusun_markasi,soforlerin_listesi,maksimum_yolcu_koltugu,toplam_seyahat_eden_yolcu_sayisi):
        self.__otobusun_markasi                 = otobusun_markasi
        self.__soforlerin_listesi               = soforlerin_listesi
        self.__maksimum_yolcu_koltugu           = maksimum_yolcu_koltugu
        self.toplam_seyahat_eden_yolcu_sayisi = 0

    # getter method
    def get_otobus_marka(self):
        return self.__otobusun_markasi
    # setter method
    def set_otobus_marka(self, x):
        self.__otobusun_markasi = x

    # getter method
    def get_soforler(self):
        return self.__soforlerin_listesi
    # setter method
    def set_soforler(self, y):
        self.__soforlerin_listesi = y

    # getter method
    def get_max_koltuk(self):
        return self.__maksimum_yolcu_koltugu
    # setter method
    def set_max_koltuk(self, z):
        self.__maksimum_yolcu_koltugu = z

    def yolculuk(self,kalkis_noktalari_listesi,varis_noktalari_listesi):
        self.kalkis_noktalari_listesi  = kalkis_noktalari_listesi
        self.varis_noktalari_listesi   = varis_noktalari_listesi

        kalkis_noktalari = ["Mersin","Ankara"]
        varis_noktalari  = ["Erzurum","Kars" ]
        sofor_liste      = ["Mehmet","Ahmet" ]
        
        yolcu_sayisi = int(input("Yolcu Sayısını Giriniz: "))
        if yolcu_sayisi + self.toplam_seyahat_eden_yolcu_sayisi > self.maksimum_yolcu_koltugu:
            print("O kadar Kişilik Yer Yok. Tekrar Deneyin")
        else:
            self.toplam_seyahat_eden_yolcu_sayisi = yolcu_sayisi + self.toplam_seyahat_eden_yolcu_sayisi 

        for i in sofor_liste:
            print(">"+ i)
            sofor = input("Sofor Seciniz.")

        print("Kalkış Noktası Seçiniz.")
        for i in kalkis_noktalari:
            print(">"+ i)
        kalkis_noktasi = input("Sehir Seciniz: ")
        for i in kalkis_noktalari:
            if kalkis_noktasi == i:
                self.kalkis_noktalari_listesi = kalkis_noktasi
            else:
                print("Hatalı Secim.")

        print("Varış Noktası Seçiniz.")
        for i in varis_noktalari:
            print(">"+ i)
        varis_noktasi = input("Sehir Seciniz: ")
        for i in varis_noktalari:
            if varis_noktasi == i:
                self.varis_noktalari_listesi = varis_noktasi
            else:
                print("Hatalı Secim.")
        
        print("Yolculuk Detayları")
        print(" > Şoför               : " + sofor)        
        print(" > Kalkış Yeri         : " + kalkis_noktasi)
        print(" > Varış Yeri          : " + varis_noktasi)
        print(" > Yolcu Sayısı        : " + str(yolcu_sayisi))
        print(" > Toplam Yolcu Sayısı : " + str(self.toplam_seyahat_eden_yolcu_sayisi))


bus_1 = Otobus("Mercedes-Benz",[],100,0)
bus_1.yolculuk("Ankara","Erzurum")
bus_1.yolculuk("Mersin","Kars")