print("Kullanıcının girdiği N sayısına göre NxN’lik matrisin simetrik olup olmadığını bulan program")

matris = []

boyut = int(input("Kac Boyutlu Olsun"))
x = 0
y = 0
a = True

for i in range(boyut ** 2):
    yazi = input("Lütfen dizinin {}. satır {}.sütununu giriniz : ".format(x,y))
    y += 1
    matris.append(yazi)
    if y == boyut:
        x += 1
        y -= y
print(str(matris))

for i in range(len(matris)): 
    for n in range(len(matris[i])): 
        if matris[i][n] != matris[n][i]:
            a = False
            break
    if not a:
        break

print(f"Matris Simetrik mi? {a}")