import numpy as np

boyut = int(input("Kaç Boyutlu Matris Oluşturulsun: "))
matris = []

for i in range(boyut):
    for j in range(boyut):
        eleman= int(input("{}. boyut {}. satırı giriniz: ".format(i,j)))
        matris.append(eleman)

matris = np.array(matris).reshape(boyut,boyut)
print(" ")
print(matris)

def Kontrol(matris, boyut):
    for i in range(boyut):
        for j in range(boyut):
            if (matris[i][j] != matris[j][i]):
                return False
    return True

if (Kontrol(matris,boyut)):
    print("Evet, Simetriktir.")
else:
    print("Hayır,Simetrik Değildir.")                                                              