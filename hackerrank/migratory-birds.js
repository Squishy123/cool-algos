function migratoryBirds(arr) {
    let map = {};
    arr.forEach((a) => {
        if (!map[a])
            map[a] = 1;
        else
            map[a]++;
    });

    let keys = Object.keys(map);
    let max = keys[keys.length-1];
    let val = map[max];

    for (let i = keys.length; i >= 0; i--) {
        if (map[keys[i]] >= val) {
            max = keys[i];
            val = map[keys[i]];
        }
    }

    return max;
}

console.log(migratoryBirds([1, 4, 4, 4, 5, 3]));