class shape():
    def __init__(self,uzun_kenar,kisa_kenar):
        self.uzun_kenar = uzun_kenar
        self.kisa_kenar = kisa_kenar
    
    def shape_create(self):
        print((self.uzun_kenar+2) * "*")
        for j in range(self.kisa_kenar):
            print("*" + (self.uzun_kenar*" ") + "*")
        print((self.uzun_kenar+2)*"*")
        print("-------------")
        print("> Uzun Kenar uzunluğu: "+str(self.uzun_kenar))
        print("> Kisa Kenar uzunluğu: "+str(self.kisa_kenar))
        print("-------------")



    def control_func(self):
        if self.uzun_kenar == self.kisa_kenar:
            print("> Evet, Karedir.") 
            print("-------------------------------------")

        else:
            print("> Hayir,Kare Değildir.")
            print("-------------------------------------")

    def set_uzun_kenar(self):
        self.uzun_kenar = int(input("> Uzun Kenarin Yeni Uzunluğunu Giriniz."))
        
    def get_uzun_kenar(self):
        print(self.uzun_kenar)
    
    def set_kisa_kenar(self):
        self.kisa_kenar = int(input("> Kisa Kenarin Yeni Uzunluğunu Giriniz."))

    def get_kisa_kenar(self):
        print(self.uzun_kenar)

shape_object = shape(12,5)

shape_object.shape_create()
shape_object.control_func()

shape_object.set_uzun_kenar()
shape_object.set_kisa_kenar()

shape_object.shape_create()
shape_object.control_func()
