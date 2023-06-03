var carpimToplami = 0;

console.log(
    "Mükemmel sayı sayının kendi hariç carpımlarının toplamının sayının kendisine eşit olmasıdır."
);

function CarpimBul(x) {
    for (let i = 0; i < x; i++) {
        if (x % i == 0) {
            console.log(i, "x", x / i, "=", x);
            carpimToplami = i + carpimToplami;
        }
    }
    if (carpimToplami == x) {
        console.log(x, "sayısı mükemmel sayıdır");
    } else {
        console.log(x, "sayısı mükemmel sayı değildir.");
    }
}
CarpimBul(28);
