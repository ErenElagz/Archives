from abc import ABC,abstractmethod

class Sport(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def Print(self):
        pass

class Team(Sport):
    def __init__(self,isim,oyun,aldigi_sayi,yedigi_sayi,puan,kurulus_tarihi):
        super().__init__()
        self.isim = isim
        self.oyun = oyun
        self.aldigi_sayi = aldigi_sayi
        self.yedigi_sayi = yedigi_sayi
        self.puan = puan
        self.kurulus_tarihi = kurulus_tarihi
        
        Team.nesneler = []

        Team.takimlar = []
    
    def Print(self):
        print(self.isim,"adlı takımın kuuulus tarihi",self.kurulus_tarihi,"'dir.")
        print("Oynadıgı Oyun Sayısı",self.oyun)
        print("Aldıgı sayı",self.aldigi_sayi,"yediği sayi",self.yedigi_sayi)
        print("puanı",self.puan)

    @classmethod
    def Listeye_Ekle(cls,takim):
        cls.takimlar.append(takim)


    @classmethod
    def Takimlar_Listesi(cls):
        for i in Team.takimlar:
            i.Print()


    @classmethod
    def TumOyuncularıGetir(cls):
        for i in Team.nesneler:
            i.Print()

    @staticmethod
    def Takim_Maclari(takim_1,takim_2):
        print("                 ",takim_1.isim," - ",takim_2.isim)
        print("Attığı Sayıılar:",takim_1.aldigi_sayi,"   ",takim_2.aldigi_sayi)


class Player(Sport):
    def __init__(self,isim,soyisim,dogum_tarihi,ozellik_1,ozellik_2,ozellik_3):
        super().__init__()
        self.isim = isim
        self.soyisim = soyisim
        self.dogum_tarihi = dogum_tarihi
        self.ozellik_1 = ozellik_1
        self.ozellik_2 = ozellik_2
        self.ozellik_3 = ozellik_3

    def Print(self):
        print(self.isim,self.soyisim,"adlı oyuncunun dogum tarihi",self.dogum_tarihi,"'dir.")
    
    @classmethod
    def Takıma_Ekle(cls,oyuncu):
        Team.nesneler.append(oyuncu)

    def Ozellik_Gor(self):
        print(self.ozellik_1)
        print(self.ozellik_2)
        print(self.ozellik_3)

    def Ozellik_Degistir(self):
        self.ozellik_1 = input("Yeni Ozellik Giriniz")
        self.ozellik_2 = input("Yeni Ozellik Giriniz")
        self.ozellik_3 = input("Yeni Ozellik Giriniz")



Team_1 = Team("Besiktas",3,3,5,19,1903)
Team_2 = Team("Galatasaray",6,1,3,14,1905)

oyuncu_1 = Player("Eren","Elagoz",2003,"","","")
oyuncu_2 = Player("Erkan","Elz",1964,"","","")
oyuncu_3 = Player("Emre","Elagz",1978,"","","")

oyuncu_1.Takıma_Ekle(Team_1)
oyuncu_2.Takıma_Ekle(Team_2)
oyuncu_3.Takıma_Ekle(Team_2)

for i in (oyuncu_3,oyuncu_2,oyuncu_1):
    i.Ozellik_Gor()

Team.Takim_Maclari(Team_1,Team_2)

Team.Listeye_Ekle(Team_1)
Team.Listeye_Ekle(Team_2)

Team.Takimlar_Listesi()

for i in (oyuncu_3,oyuncu_2,oyuncu_1):
    i.Print()

for i in (Team_1,Team_2):
    i.Print()