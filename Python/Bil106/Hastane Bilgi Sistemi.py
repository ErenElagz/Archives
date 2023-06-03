import datetime

class HastaneBilgiSistemi():
    
    def __init__(self,isim,soyisim,hastalık,tedavi):
        
        self.hasta_liste = []
        
        x = str(datetime.datetime.now())
        self.tedavi    = x       
        
    def HastaEkle(self):
        
        self.isim      = input("Hasta ismi giriniz: ")
        self.soyisim   = input("Hasta soyismi giriniz: ")
        self.hastalık  = input("Hastalık giriniz:(1 = grip, 2 = covid,3= zaturre,4 =soguk algınligi")
        hastaliklar=[{'id': 1, 'hastalik': 'grip'}, {'id': 2, 'hastalik': 'covid'}, {'id': 3, 'hastalik': 'zaturre'}, {'id': 4,  'hastalik': 'soğuk algınlığı ' }] 
        
        self.hastalık = hastaliklar
        
    def HastaDuzenle(self):
        print("1.Hasta ismi ve soyismi düzenle")
        print("2.Hastalık düzenle")
        print("3.Tedavi düzenle")          
        
    def HastaListele(self):
#        print("- - - - - - - - - - - - - ")
#        print("Hasta Adı Soyadı = "  + self.isim  + " " + self.soyisim)
#        print("Hastalık Bilgisi  = " + self.hastalık  )
#        print("Tedavi Tarihi =  "    + self.tedavi) 
#        print("- - - - - - - - - - - - - ")
        
        hastabilgisi= {
            "Hasta_isim": self.isim,
            "Hasta_Soyisim":self.soyisim,
            "Hastalık_ismi": self.hastalık,
            "Tedavi_tarihi": self.tedavi
            }
        print(hastabilgisi)
        
h1=HastaneBilgiSistemi("isim","soyisim","Boş","Boş")
        
while True:

    print("Hastane Bilgi Sistemi")
    print("- - - - - - - - - - - - -")
    print("1. Hasta Ekle")
    print("2. Hasta Düzenle")
    print("3. Hastaları Listele")
    print("4. Çıkış")     
    print("- - - - - - - - - - - - -")
    
    giris = str(input("Lütfen yukarıdaki numaralardan hangi işlemi yapmak istediğinizi seçiniz : "))
    
    if giris ==  "1" :
        h1.HastaEkle()
    elif giris == "2" :    
        h1.HastaDuzenle()  
    elif giris == "3" :
        h1.HastaListele()
    elif giris == "4" :
        print("çıkış yapılıyor....")
        break
    else:
        print("Lütfen yukarıdaki numaralrdan birini giriniz")



    