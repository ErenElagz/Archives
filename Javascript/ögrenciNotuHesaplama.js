var vize, final, proje, ortalama, harfNotu;

vize = prompt("Vize  Notunu Giriniz?");
final = prompt("Final Notunu Giriniz?");
proje = prompt("Proje Notunu Giriniz?");

ortalama = vize * 0.3 + final * 0.5 + proje * 0.2;

console.log("Ortalamanız:", ortalama);

if (ortalama >= 80) {
  console.log("Harf Notunuz: AA");
} else if (ortalama > 80) {
  console.log("Harf Notunuz: BB");
} else if (ortalama > 60) {
  console.log("Harf Notunuz: CC");
} else if (ortalama > 40) {
  console.log("Harf Notunuz: CC");
} else {
  console.log("Kaldınız Dersten.DD");
}
