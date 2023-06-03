let sayilar = [1, 2, 5, 12, 78, 55, 46, 30, 45, 97, 78, 56];
for (let sayi of sayilar) {
    console.log(sayi * sayi);
}

for (let sayi of sayilar) {
    if (sayi % 5 == 0) {
        console.log(sayi);
    }
}

var toplam = 0;
for (let sayi of sayilar) {
    if (sayi % 2 == 0) {
        toplam = toplam + sayi;
    }
}
console.log(toplam);

let urunler = ["a", "ab", "asd", "awds", "aaa"];
for (let urun of urunler) {
    urun = urun.toUpperCase();
    console.log(urun);
}

let urun = [
    "Samsung S20",
    "Samsung S7 Edge",
    "Huawei P20",
    "Huawei Mate 10 Lite",
    "Iphone 14 Pro",
];
for (let telefon of urun) {
    if (telefon.includes("Samsung")) {
        console.log("Samsung Cihaz Var");
    } else {
        console.log("Samsung Cihaz Yok");
    }
}

let ogrenciler = [
    { ad: "Eren", notlar: [100, 90, 80], bilgi: "sdc", ortalama: 0 },
    { ad: "Mert", notlar: [80, 60, 70], bilgi: "sdc", ortalama: 0 },
    { ad: "Ali", notlar: [20, 30, 90], bilgi: "sdc", ortalama: 0 },
];

for (let ogrenci of ogrenciler) {
    for (let not of ogrenci.notlar) {
        ogrenci.ortalama = ogrenci.ortalama + not;
    }
    ogrenci.ortalama = ogrenci.ortalama / 3;

    if (ogrenci.ortalama > 80) {
        ogrenci.bilgi = "başarılı";
    } else if (ogrenci.ortalama > 80) {
        ogrenci.bilgi = "başarılı";
    } else if (ogrenci.ortalama > 50) {
        ogrenci.bilgi = "orta seviye";
    } else {
        ogrenci.bilgi = "düşük seviye seviye";
    }
};

for (let ogrenci of ogrenciler) {
    console.log(
        `${ogrenci.ad} adlı ögrencinin ,notları ${ogrenci.notlar}, ortlaması ${ogrenci.ortalama} ,durumu ${ogrenci.bilgi}`
    );
};
