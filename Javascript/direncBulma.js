var sayi1, sayi2, carpan, tolerans, carpanAdi;

sayi1 = prompt("İlk rengi giriniz?");

if ((sayi1 = "siyah")) {
  sayi1 = "0";
} else if (sayi1 = "kahverengi") {
  sayi1 = "1";
} else if (sayi1 = "kırmızı") {
  sayi1 = "2";
} else if (sayi1 = "turuncu") {
  sayi1 = "3";
} else if (sayi1 = "sarı") {
  sayi1 = "4";
} else if (sayi1 = "yeşil") {
  sayi1 = "5";
} else if (sayi1 = "mavi") {
  sayi1 = "6";
} else if (sayi1 = "mor") {
  sayi1 = "7";
} else if (sayi1 = "gri") {
  sayi1 = "8";
} else if (sayi1 = "beyaz") {
  sayi1 = "9";
}

sayi2 = prompt("İkinci rengi giriniz?");

if ((sayi2 = "siyah")) {
  sayi2 = "0";
} else if (sayi2 = "kahverengi") {
  sayi2 = "1";
} else if (sayi2 = "kırmızı") {
  sayi2 = "2";
} else if (sayi2 = "turuncu") {
  sayi2 = "3";
} else if (sayi2 = "sarı") {
  sayi2 = "4";
} else if (sayi2 = "yeşil") {
  sayi2 = "5";
} else if (sayi2 = "mavi") {
  sayi2 = "6";
} else if (sayi2 = "mor") {
  sayi2 = "7";
} else if (sayi2 = "gri") {
  sayi2 = "8";
} else if (sayi2 = "beyaz") {
  sayi2 = "9";
}

carpan = prompt("Carpan rengi Girin?");

if ((carpan = "siyah")) {
  carpan = 1;
  carpanAdi = "ohm";
} else if ((carpan = "kahverengi")) {
  carpan = 10;
  carpanAdi = "x10 ohm";
} else if ((carpan = "kırmızı")) {
  carpan = 100;
  carpanAdi = "x100 ohm";
} else if (carpan = "turuncu") {
  carpan = 1000;
  carpanAdi = "K ohm";
} else if (carpan = "sarı") {
  carpan = 10000;
  carpanAdi = "x10K  ohm";
} else if (carpan = "yeşil") {
  carpan = 100000;
  carpanAdi = "x100K ohm";
} else if (carpan = "mavi") {
  carpan = 1000000;
  carpanAdi = "1M ohm";
} else if (carpan = "mor") {
  carpan = 10000000;
  carpanAdi = "10M ohm";
} else if (carpan = "altın") {
  carpan = 0.1;
  carpanAdi = "x0.1 ohm";
} else if (carpan = "gümüş") {
  carpan = 0.01;
  carpanAdi = "x0.01 ohm";
}

tolerans = prompt("Tolerans rengi Girin?");

if ((tolerans = "kahverengi")) {
  tolerans = "+-%1";
} else if (tolerans = "kırmızı") {
  tolerans = "+-%2";
} else if (tolerans = "yeşil") {
  tolerans = "+-%0.5";
} else if (tolerans = "mavi") {
  tolerans = "+-%0.25";
} else if (tolerans = "mor") {
  tolerans = "+-%0.10";
} else if (tolerans = "altın") {
  tolerans = "+-%5";
} else if (tolerans = "gümüş") {
  tolerans = "+-%10";
}

console.log("Direnc Degeri:",(sayi1))