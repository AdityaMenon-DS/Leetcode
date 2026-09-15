var isNumber = function(s) {
    let digit = false;
    let dot = false;
    let exp = false;
    let digitAfterExp = true;

    for (let i = 0; i < s.length; i++) {
        let c = s[i];

        if (c >= '0' && c <= '9') {
            digit = true;

            if (exp) {
                digitAfterExp = true;
            }
        }

        else if (c === '+' || c === '-') {
            if (i > 0 && s[i - 1] !== 'e' && s[i - 1] !== 'E') {
                return false;
            }
        }

        else if (c === '.') {
            if (dot || exp) {
                return false;
            }

            dot = true;
        }

        else if (c === 'e' || c === 'E') {
            if (exp || !digit) {
                return false;
            }

            exp = true;
            digitAfterExp = false;
        }

        else {
            return false;
        }
    }

    return digit && digitAfterExp;
};