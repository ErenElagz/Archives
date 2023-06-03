function Palindrom(kelime) {
    console.log("Kelime:", kelime);
    kelime = kelime.toLowerCase();

    reverse_kelime = kelime.split("").reverse().join("");
    console.log("Kelimenin Tersi:", reverse_kelime);

    if (kelime == reverse_kelime) {
        console.log("Kelime Palindromdur");
    } else {
        console.log("Kelime Palindrom Değildir");
    }
}

Palindrom("Kelek");
