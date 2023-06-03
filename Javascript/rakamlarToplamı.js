function RakamlarToplamı(sayi) {
    var toplam = 0;
    console.log("Sayı:", sayi);

    for(let i of sayi.toString()){
        console.log("Rakam:",i);
        toplam = toplam+Number(i)

    }
    console.log("Rakamlar Toplamı:", toplam);

}

RakamlarToplamı(23434);
