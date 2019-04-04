function birthday(s, d, m) {
    let p = 0;
    for (let i = 0; i < s.length; i++) {
        let sum = 0;
        let c = 0;
        for (let j = i; j < s.length; j++) {
            sum += s[j];
            c++;
            if (sum >= d)
                break;
            if (c > m)
                break;
        }
        if (sum == d && c == m)
            p++;
    }
    return p;
}