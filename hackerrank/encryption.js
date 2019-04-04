function encryption(s) {
    let encryp = [];
    s = s.replace(/" "/g, "");
    let rowLen;
    if (Math.sqrt(s.length) < Math.floor(Math.sqrt(s.length) + 0.5))
        rowLen = Math.sqrt(s.length + 1);
    else
        rowLen = Math.floor(Math.sqrt(s.length));
    let colLen = Math.ceil(s.length / rowLen);


    for (let i = 0; i < s.length; i++) {
        if (encryp[i % colLen])
            encryp[i % colLen] += s[i];
        else
            encryp[i % colLen] = s[i];
    }
    let str = "";
    encryp.forEach((e) => {
        str += e + " ";
    })
    return str;
}