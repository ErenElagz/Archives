import time

class Dosyalama():
    def __init__(self,dosya_adi, dosya_formati, dosya_oluşturma_tarihi, dosya_guncelleme_tarihi, dosyalama_yolu, dosya_icerigi_listesi):
        self._dosya_adi = dosya_adi
        self._dosya_formati = dosya_formati
        self.dosya_olusturulma_tarihi = time.asctime()
        self._dosya_guncelleme_tarihi = dosya_guncelleme_tarihi
        self._dosyalama_yolu = dosyalama_yolu
        self._dosya_icerigi_listesi = dosya_icerigi_listesi

    # getter method
    def get_dosya_adi(self):
        return self._dosya_adi
    # setter method
    def set_dosya_adi(self, x):
        self._dosya_adi = x

    # getter method
    def get_dosya_formati(self):
        return self._dosya_formati
    # setter method
    def set_formati(self, y):
        self._dosya_formati = y

    # getter method
    def get_dosya_guncelleme_tarihi(self):
        return self._dosya_guncelleme_tarihi
    # setter method
    def set_dosya_guncelleme_tarihi(self, z):
        self._dosya_guncelleme_tarihi = z

    # getter method
    def get_dosyalama_yolu(self):
        return self._dosyalama_yolu
    # setter method
    def set_dosyalama_yolu(self, v):
        self._dosyalama_yolu = v

    # getter method
    def get_dosya_icerigi_listesi(self):
        return self._dosya_icerigi_listesi
    # setter method
    def set_dosya_icerigi_listesi(self, c):
        self._dosya_icerigi_listesi = c

    def print_file(self):
        print("Dosya Adı:")
        print(self.get_dosya_adi())
        print("-----------------")
        print("Dosya Formatı:")
        print(self.get_dosya_formati())
        print("-----------------")
        print("Dosya Olusturulma Tarihi:")
        print(self.dosya_olusturulma_tarihi)
        print("-----------------")
        print("Dosya Güncellenme Tarihi:")
        print(self._dosya_guncelleme_tarihi)
        print("-----------------")
        print("Dosylama Yolu:")
        print(self.get_dosyalama_yolu())
        print("-----------------")
        print("Dosya İçerği:")
        print(self.get_dosya_icerigi_listesi())

dosya1 = Dosyalama("Deneme","Deneme",time.asctime(),time.asctime(),"txt","Boş")
dosya1.print_file()