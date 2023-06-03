class Geometri():
    def __init__(self,kenar_sayisi):
        self.kenarlar = []
        self.kenar_sayisi = kenar_sayisi

    def kenarlari_gir(self):
        self.x = int(input("Kenar Degerini Giriniz. "))
        self.y = int(input("Kenar Degerini Giriniz. "))
        self.z = int(input("Kenar Degerini Giriniz. "))

        self.kenarlar.append(self.x)
        self.kenarlar.append(self.y)
        self.kenarlar.append(self.z)

    def kenarlari_listele(self):
        for i in self.kenarlar:
            print(i)


class Ucgen(Geometri):
    def __init__(self, kenarlar):
        super().__init__(kenarlar)

    def Hacim(self):
        self.hacim = (((sekil.x )* (sekil.y/2))*sekil.y)
        print("Hacim =" ,self.hacim )

    def Cevre(self):
        self.cevre = (sekil.y * sekil.z) + (sekil.x + sekil.z + sekil.y)
        print("Cevre =" ,self.cevre )

    def Alan(self):
        self.alan = ((sekil.x )* (sekil.y/2))
        print("Alan =" ,self.alan )


sekil = Geometri(3)
sekil.kenarlari_gir()
sekil.kenarlari_listele()


ucgen = Ucgen(3)
ucgen.kenarlari_gir()
ucgen.kenarlari_listele()
ucgen.Alan()
ucgen.Cevre()
ucgen.Hacim()

