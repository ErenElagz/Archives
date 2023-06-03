class Ucgen():
    def __init__(self,kenar1,kenar2,kenar3):
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.kenar3 = kenar3
        
    def Cevre(self):
        return self.kenar1 + self.kenar2 + self.kenar3

    def Alan(self):
        alan_ucgen = self.kenar1 + self.kenar2 + self.kenar3
        print("Ucgen Alan",alan_ucgen)

class Dortgen(Ucgen):
    def __init__(self, kenar1, kenar2, kenar3,kenar4):
        super().__init__(kenar1, kenar2, kenar3)
        self.kenar4 = kenar4

    def Cevre(self):
        cevre_dort = super().Cevre + self.kenar4
        print("Dortgen Cevresi",cevre_dort)


sekil1 = Ucgen(1,2,3)
sekil1.Alan()
sekil1.Cevre()

sekil2 = Dortgen(1,2,3,4)
sekil2.Cevre()