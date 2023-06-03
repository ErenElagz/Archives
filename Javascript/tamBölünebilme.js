var bol1, bol2, sayi;

sayi = prompt("Bölünecek Sayıyı Giriniz?");

bol1 = prompt("Bölecek İlk Sayı Giriniz?");
bol2 = prompt("Bölecek İkinci Sayı Giriniz?");

if (sayi % bol1 == 0) {
  if (sayi % bol2 == 0) {
    console.log(
      sayi,
      "sayısı hem",
      bol1,
      "hemde",
      bol2,
      "sayısına tam bölünebiliyor."
    );
  } else {
    console.log("Sayı", bol2, "ye bölünemiyor");
  }
} else {
  console.log(
    sayi,
    "sayısı hem",
    bol1,
    "hemde",
    bol2,
    "sayısına tam bölünemiyor."
  );
};
