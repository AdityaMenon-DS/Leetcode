var numDecodings = function(s) {
    if (s[0] === '0') {
        return 0;
    }

    let a = 1;
    let b = 1;

    for (let i = 1; i < s.length; i++) {
        let c = 0;

        if (s[i] !== '0') {
            c += b;
        }

        let x = Number(s.substring(i - 1, i + 1));

        if (x >= 10 && x <= 26) {
            c += a;
        }

        a = b;
        b = c;
    }

    return b;
};