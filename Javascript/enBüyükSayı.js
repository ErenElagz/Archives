var sayi1, sayi2, sayi3;

sayi1 = prompt("1. Sayıyı Giriniz?");
sayi2 = prompt("2. Sayıyı Giriniz?");
sayi3 = prompt("3. Sayıyı Giriniz?");

if (sayi1 > sayi2 && sayi1 > sayi3) {
  console.log("En Büyük Sayı:", sayi1);
}
if (sayi2 > sayi1 && sayi2 > sayi3) {
  console.log("En Büyük Sayı:", sayi2);
}
if (sayi3 > sayi1 && sayi3 > sayi2) {
  console.log("En Büyük Sayı:", sayi3);
}
