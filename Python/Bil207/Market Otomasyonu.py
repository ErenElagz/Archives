class Market():
    def __init__(self,market_ismi,sermaye,urun_listesi):
        self.market_ismi = market_ismi
        self.sermaye =  sermaye
        self.urun_listesi = urun_listesi

    def urun_ekle(self,urun_id,urun_adi,urun_miktari,urun_satis_degeri,urun_alis_degeri):
        self.urun_id           = urun_id
        self.urun_adi          = urun_adi
        self.urun_miktari      = urun_miktari
        self.urun_satis_degeri = urun_satis_degeri
        self.urun_alis_degeri  = urun_alis_degeri

        self.urun_listesi.append({"urun_id":urun_id,
                                  "urun_adi":urun_adi,
                                  "urun_miktari":urun_miktari,
                                  "urun_alis_degeri":urun_alis_degeri,
                                  "urun_satis_degeri":urun_satis_degeri})

        self.sermaye = self.sermaye - (int(urun_alis_degeri)*int(urun_miktari))

    def urun_sat(self,urun_adi,urun_miktari):
        self.urun_adi     = urun_adi
        self.urun_miktari = urun_miktari

        for i in self.urun_listesi:
            pass

    def urunleri_goster(self):
        for i in self.urun_listesi:
            print("- - - - - - - - - -")
            print("Ürün Id          : " + str(urun_id))
            print("Ürün Adı         : " + str(urun_adi))
            print("Ürün Miktarı     : " + str(urun_miktari))
            print("Ürün Alış Değeri : " + str(urun_alis_deger))
            print("Ürün Satış Degeri: " + str(urun_satis_deger))   
            print("- - - - - - - - - -")

    def sermayeyi_goster(self):
        print("> Güncel Sermayeniz: " + str(self.sermaye))

    def sermayeyi_guncelle(self):
        self.sermaye = (int(input("Güncel sermaye değerini giriniz: ")))

    def market_ismi_getir(self):
        print("> Market İsmi: " + self.market_ismi)

market = Market("Hitit Market",10000,[])
market.market_ismi_getir()
market.urun_ekle("1","2","3","4","5")
market.urun_ekle("5","1","3","2","4")
while True:
    secenek = input("--------------------------------\n > Ürün eklemek için 1\n > Ürün satmak için 2\n > Sermayeyi görmek için 3\n > Sermayeyi güncellemek için 4\n > Çıkmak için 5 yazarak Enter'a basınız: \n--------------------------------")

    if secenek == "1":
        urun_id = int(input("Ürün id'sini giriniz: "))
        urun_adi = input("Ürün adını giriniz: ")
        urun_miktari = int(input("Ürün miktarini giriniz: "))
        urun_satis_deger = int(input("Ürün satış değerini giriniz: "))
        urun_alis_deger = int(input("Ürün alış değerini giriniz: "))

        market.urun_ekle(urun_id,urun_adi,urun_miktari,urun_alis_deger,urun_satis_deger)

    elif secenek == "2" :
        market.urunleri_goster()
        urun_id = int(input("Ürün id'sini giriniz: "))
        urun_miktari = int(input("Almak istediğiniz ürün miktarı: "))
        market.urun_sat(urun_id, urun_miktari)

    elif secenek == "3":
        print("-----------------")
        market.sermayeyi_goster()
        print("-----------------")

    elif secenek == "4":
        print("-----------------")
        market.sermayeyi_goster()
        market.sermayeyi_guncelle()
        print("-----------------")

    elif secenek == "5":
        print("\nCıkış Yapıldı.")
        break

    else : print("Yalızca Belirlenen degerleri giriniz.")