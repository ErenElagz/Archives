vize1 = input("Lütfen vize 1 in sonucunu giriniz: ")
vize2 = input("Lütfen vize 2 in sonucunu giriniz: ")
final = input("Lütfen final in sonucunu giriniz: ")

ortalama = float(vize1)*0.25 + float(vize2)*0.25 + float(final)*0.50

if ortalama <= 40:
   harfnotu= "FF"
   
elif ortalama <= 50:
   harfnotu= "DD"
   
elif ortalama <= 60:
   harfnotu= "CC"
   
elif ortalama <= 65:
   harfnotu= "BB"
   
elif ortalama <= 75:
   harfnotu= "BA"

elif ortalama <= 85:
   harfnotu= "AA"

print("ortalamanız :" + str(ortalama)+ "harfnotunuz : " + harfnotu)