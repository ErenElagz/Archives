import random

savasci1_can =200
savasci2_can =200


maxsaldiri1 = int(input("1.oyuncunun saldırı gücünü seçiniz "))
maxsaldiri2 = int(input("2.oyuncunun saldırı gücünü seçiniz "))

maxsavunma1 = int(input("1.oyuncunun savunma gücünü seçiniz "))
maxsavunma2 = int(input("2.oyuncunun savunma gücünü seçiniz "))

print("Savaş Başladı")    

while savasci1_can > 0 and savasci2_can > 0 :
    
    print("---------1. savaşcı saldırıyor--------")
    
    saldiri1 = random.randint(0,maxsaldiri1)
    
    print("1. savaşcının saLdırı gücü: " + str(saldiri1))
    
    savunma2 = random.randint(0,maxsavunma2)
    
    print("2. savaşcının savunma gücü: " + str(savunma2))
    
    hasar1 = saldiri1-savunma2
    
    print("1. oyuncunun hasarı: " + str(hasar1))
    
    savasci2_can -= hasar1
    
    print("2. savaşcının kalan canı: " +  str(savasci2_can))

    print("--------------------------------------------------")
    
        
    if savasci2_can <=0 :
        print("savascı1 kazandı")
        break
    
 
    print("-----------2. savaşcı saldırıyor---------")
    
    saldiri2 = random.randint(0,maxsaldiri2) 
    
    print("2. savaşcının saLdırı gücü: " + str(saldiri2))
    
    savunma1 = random.randint(0,maxsavunma1)
    
    print("1. savaşcının savunma gücü: " + str(savunma1))
    
    hasar2 = saldiri2-savunma1
    
    print("2. oyuncunun hasarı: " + str(hasar2))
    
    savasci1_can -= hasar2
    
    print("1. savaşcının kalan canı: " + str(savasci1_can))
    
    print("--------------------------------------------------")
    
    if savasci1_can <=0 :
        print("savascı2 kazandı")
        break