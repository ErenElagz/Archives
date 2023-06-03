#https://www.youtube.com/channel/UCSuZoI3MYLXn0VZn7IJagTA
#Bu Linkten Kanalın 2. videosunu lab 10 çalısmasını izleyebilrisniz

print("Üniversitesi Otomasyonu Uygulaması")

class University():
    def __init__(self,isim):
       self._isim = isim
       self.ogrenciler =  []

class Department(University):
    def __init__(self,isim,kurulus_tarihi):
        super().__init__(isim)
        self._isim = isim
        self._ders = []
        self._kurulus_tarihi = kurulus_tarihi

    def Ders_Isımlerini_Gir(self):
        print("- - - - - - - - - - - - - - - - - - - ")
        n = int(input("Kac Ders Girilecek"))
        for i in range(n):
            c = input("Bölüm Derslerini Giriniz")
            self._ders.append(c)

    def Ders_Isımlerini_Sil(self):
        print("Silinebilecek Dersler: ",str(self._ders))
        x = input("Ders İsmini Girin")
        self._isim.remove(x)

    def Bolum_Ismini_Duzenle(self):
        self._isim = input("Yeni Bölüm İsmini Düzenle")
    
    def Kurulus_Tarihini_Duzenle(self):
        self._kurulus_tarihi = input("Bölümün Kurulus Tarihini Düzenle")
    
    def Bolum_Bilgisi(self):
        print("- - - - - - - - - - - - - - - - - - - ")
        print(self._isim,"isimli Bölümün kurulus tarihi:",self._kurulus_tarihi)
        print("Bolum Dersleri:")
        print(str(self._ders))

class Student(University):
    def __init__(self, isim,soyisim,dogum_tarihi,ortalama):
        super().__init__(isim)
        self._isim = isim
        self._soyisim = soyisim
        self._dogum_tarihi = dogum_tarihi
        self._dersler = []
        self._ortalama = ortalama

    def Ogrenci_Ismini_Duzenle(self):
        self._isim = input("Ögrenci İsmini Düzenle")
        self._soyisim = input("Ögrenci Soyİsmini Düzenle")

    def Dogum_Tarihini_Duzenle(self):
        self._dogum_tarihi = input("Ögrenci Doğum Tarihini Düzenle")
    
    def Ortalama_Duzenle(self):
        self._ortalama = input("Ogrenci Ortalamsını Düzenleyin")
    
    def Alinan_Dersler(self):
        print("- - - - - - - - - - - - - - - - - - - ")
        a = int(input("Alınan Ders Sayısı Kactır"))
        for i in range(a):
            b = input("Ders İsmini Giriniz") 
            self._dersler.append(b)
        
    def Listeye_Ekle(self):
        ogrenci = (self._isim + self._soyisim)
        self.ogrenciler.append(ogrenci)

    def Ogrenci_Bilgisi(self):
        print("- - - - - - - - - - - - - - - - - - - ")
        print(self._isim,self._soyisim,"isimli ogrencinin dogum tarihi:",self._dogum_tarihi)
        print("Aldıgı Dersler:")
        print(str(self._dersler))

o1 = Student("Eray","Elagoz",2003,80)
o2 = Student("Eren","Kar",2000,75)

b1 = Department("Bilgisayar M.",2015)
b2 = Department("Elektrik M.",2011)

o1.Listeye_Ekle()
o2.Listeye_Ekle()
o1.Alinan_Dersler()
o2.Alinan_Dersler()

b1.Ders_Isımlerini_Gir()
b2.Ders_Isımlerini_Gir()

print(str(self.ogrenciler))

for i in [o1,o2]:
    i.Ogrenci_Bilgisi()

for i in [b1,b2]:
    i.Bolum_Bilgisi()










