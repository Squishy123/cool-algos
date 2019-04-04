function extraLongFactorials(n) {
    console.log(n);
    if (n <= 1)
        return 1;

    return n * extraLongFactorials(n - 1);

}

console.log(extraLongFactorials(45));