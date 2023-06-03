var boy, kilo, endeks;

boy = prompt("Boyunuzu Giriniz?");
kilo = prompt("Kilonuzu Giriniz?");

endeks = 100 * (kilo / ((boy * boy) / 100));
console.log("kitle endeksiniz:", endeks);

if (endeks < 18.5) {
  console.log("Zayıf");
} else if (endeks <= 24.9) {
  console.log("Normal");
} else if (endeks <= 29.9) {
  console.log("Kilolu");
} else if (endeks <= 34.9) {
  console.log("1.Derece Obezite");
} else if (endeks >= 39.9) {
  console.log("2.Derece Obezite");
} else {
  console.log("3. Derece Obezite");
}
