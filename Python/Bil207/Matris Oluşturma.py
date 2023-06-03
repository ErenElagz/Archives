import numpy as np

filter_matrix = [[1,2,3],[2,4,2],[1,2,1]]
main_matrix = []
temp_matrix = []
result_matrix =[]

deger = 4
toplam_deger = 0
toplam = 0

# 8x8 Matrix 
for i in range(deger):
    for j in range(deger):
        eleman= int(input("{}. boyut {}. satırı giriniz: ".format(i,j)))
        main_matrix.append(eleman)
main_matrix = np.array(main_matrix).reshape(deger,deger)
print(main_matrix)

#filtre matris toplamı
for i in range(3):
    for j in range(3):
        toplam_deger = toplam_deger + j
        
#matriste kaydırma islemleri icin değiskenler        
satir1 = 0
satir2 = 0
sutun1 = 0
sutun2 = 0

#matris işlemi
for i in range(6):
    for j in range(6):
        for x in range(i,i+2):
            for z in range(i,i+2):
                toplam = toplam + (main_matrix[x][z]*filter_matrix[x][z])
                
                #satır atlama
                result_matrix[satir1][sutun1] = toplam/toplam_deger
                satir1 = satir1 + 1
                sutun1 = sutun1 + 1
                
print(result_matrix)

                