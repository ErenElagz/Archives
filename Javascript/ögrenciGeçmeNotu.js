var ogrenciNotu, ogrenciHarfNotu;

ogrenciNotu = prompt("Ögrenci Notunu Giriniz?");

if (ogrenciNotu >= 80) {
    console.log("AA Harf Notuyla Geçtiniz, Tebrikler");
}
else if (ogrenciNotu <= 79) {
    console.log("BB Harf Notuyla Geçtiniz, Çalışmaya Devam");
}
else if (ogrenciNotu <= 49) {
    console.log("CC Harf Notuyla Geçtiniz, Ucu Ucuna");
}
else {
    console.log("DD Harf Notuyla Geçtiniz, Dersten Kaldınız ");
}