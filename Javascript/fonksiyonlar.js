function Hello(melba) {
    console.log("Denemeler", melba);
}
Hello("merhabalar");

function Kereyazdir(adet) {
    for (let i = 0; i < adet; i++) {
        console.log("merhaba");
    }
}
Kereyazdir(20);

function Alan(kisa, uzun) {
    let alan = kisa * uzun;
    let cevre = (kisa + uzun) * 2;
    console.log("Alan", alan);
    console.log("Cevre", cevre);
}

Alan(20, 5);

function Dice() {
    let sayi = Math.random() * 10;
    if (sayi > 5) {
        console.log("tura");
    } else {
        console.log("yazı");
    }
}
Dice();

function Toplam() {
    let sonuc = 0;
    console.log(arguments); //fonk içindeki eleman syısı farketmeksizin işlem yapabilir

    for (let sayi of arguments) {
        sonuc = sonuc+sayi
    }
    console.log(sonuc)
}
Toplam(4,6,12,42)