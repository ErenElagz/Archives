function faktoriyel(sayi) {
    var carpim=1;
    for (; sayi > 0; sayi--) {
        carpim = carpim * sayi;
    }
    console.log(carpim);
}
faktoriyel(5);
