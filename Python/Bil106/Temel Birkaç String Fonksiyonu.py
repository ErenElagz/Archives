#Kaynak
# https://www.kemalsahin.com/docs/python-egitimi/veri-yapilari/metin-string-methodlari/

#capitalize()
# kelimenin ilk harfini büyük harf yapar.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#casefold()
# tüm karakterleri küçük harfe çevirir.
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center()
# belirtilen sayı kadar boşluk ekleyip ortalanmış olarak döndürür.
txt = "banana"
x = txt.center(20)
print(x)

#count()
# Belirtilen metin ifadesi, ana metin ifadesinde kaç kere geçtiğini bulup döndürür.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode()
# metin ifadesini UTF-8 olarak kodlayıp döndürür.
txt = "My name is Ståle"
x = txt.encode()
print(x)

#endswith()
# Metin ifadesi belirtilen metin ifadesi ile bitiyorsa TRUE değeri döndürür.
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#expandtabs()
# Tab boşluğunun miktarının özelleştirilmesini sağlar.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

#find()
# Metin ifadesi içerisinde belirtilen metin ifadesini arar ve bulduğu index değerini döndürür.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#format()
# Metin ifadesini biçimlendirir.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#format_map()
# format_map() verilen dizeyi biçimlendirir ve onu döndürür.
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))
point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

#index()
# Find metodu gibi çalışır. Metin ifadesi içerisinde belirtilen metin ifadesini arar ve bulduğu index değerini döndürür.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isalnum()
# Metin ifadesindeki tüm karakterler alfanumerik ise TRUE değeri döndürür.
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha()
# Metin ifadesindeki tüm karakterler alfabetik ise TRUE değeri döndürür.
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isdecimal()
# Metin ifadesindeki tüm karakterler sayı (kodlanmış olsa bile) ise TRUE değeri döndürür.
x = txt.isdecimal()
print(x)

#isdigit()
# Metin ifadesindeki tüm karakterler rakam ise TRUE değeri döndürür.
txt = "50800"
x = txt.isdigit()
print(x)

#islower()
# Metin ifadesindeki tüm karakterler küçük harf ise TRUE değeri döndürür.
txt = "hello world!"
x = txt.islower()
print(x)

#isnumeric()
# Metin ifadesindeki tüm karakterler sayı ise TRUE değeri döndürür.
txt = "565543"
x = txt.isnumeric()
print(x)

#isprintable()
# Metin ifadesindeki tüm karakterler yazdırılabilir ise TRUE değeri döndürür.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

#join()
# Belirtilen bir karakteri kullanarak, bir dizgideki tüm öğeleri bir metin ifadesinde birleştir.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#ljust()
# Metin ifadesini sola yaslayarak döndürür.
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#lower()
# Metin ifadesindeki tüm karakterleri küçük harfe döndürür.
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#lstrip()
# Metin ifadesinin sol tarafındaki boşluk karakterleri temizleyerek döndürür.
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#replace()
# Metin ifadesinde, belirtilen metin ifadelerini değiştirir.
txt = "I like bananas"
x = txt.replace("bananas", "apples")

print(x)
#rfind()
# Metin ifadesi içerisinde belirtilen ifadeyi arar, son bulduğu konumdaki index değerini döndürür.
txt = "Mi casa, su casa."
x = txt.rfind("casa")

print(x)
#rindex()
# rfind() metodu gibi, metin ifadesi içerisinde belirtilen ifadeyi arar, son bulduğu konumdaki index değerini döndürür.
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#rpartition()
# Metin ifadesi içerisinde belirli bir ifadenin en son geçtiği yeri bulur ve ifadeyi üçe böler. Üç elemanlı diziye dönüştürür.
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#split()
# Metin ifadesini belirtilen karaktere göre alt metin ifadelerine böler. Yeni bir liste meydana getirir.
txt = "welcome to the jungle"
x = txt.split()
print(x)

#startswith()
# Metin ifadesinin başlangıcında belirli bir metin ifadesi ile başlayıp başlamadığını kontrol eder, başlıyorsa TRUE değerinin döndürür.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

#strip()
# Metin ifadesini sağından ve solundan boşluk karakterlerini siler.
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#zfill()
# Metin ifadesinin sol tarafına belirtilen sayı kadar sıfır ekler.
txt = "50"
x = txt.zfill(10)
print(x)
