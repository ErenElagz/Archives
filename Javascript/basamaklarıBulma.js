function Basamak(sayi) {
    string_sayi = sayi.toString();
    for (let rakam of string_sayi) {
        for (let i = string_sayi.length; i > 0; i--) {
            console.log(rakam + ("0" * i));
        }
    }
}

Basamak(1327);
