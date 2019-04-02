function gcd(n, m) {
    if (m == 0)
        return n;
    return gcd(m, n % m);
}

function lcm(n, m) {
    return (n * m) / gcd(n, m);
}

function gcdArr(arr) {
    let res = arr[0];
    for (let i = 1; i < arr.length; i++) {
        res = gcd(arr[i], res);
    }

    return res;
}

function lcmArr(arr) {
    let res = arr[0];
    for (let i = 1; i < arr.length; i++) {
        res = lcm(arr[i], res);
    }

    return res;
}

function getTotalX(a, b) {
    let gcdB = gcdArr(b);
    let lcmA = lcmArr(a);

    let tot = [];
    for (let i = lcmA; i <= gcdB; i += lcmA) {
        let check = true;
        b.forEach((be) => {
            if (be % i != 0)
                check = false;
        });
        if (check)
            tot.push(i);
    }

    return tot.length;
}

console.log(getTotalX([2, 4], [16, 32, 96]))