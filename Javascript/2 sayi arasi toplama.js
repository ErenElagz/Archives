function Sayilar(ilk, son) {
    var toplam = 0;

    for (; ilk <= son; ilk++) {
        toplam = toplam + ilk;
    }

    console.log(toplam);
}
Sayilar(4, 8);
