print("Palindrom Bulma Programı")

yazı = input("Lütfen kelime giriniz: ")
yazı = yazı.lower()

ters = yazı[::-1]
ters = ters.lower()

if yazı == ters :
    print("Evet kelime palindromdur")
else :
    print("Palindrom Değildir")