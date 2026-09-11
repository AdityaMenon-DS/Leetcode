var groupAnagrams = function(strs) {
    let m = new Map();

    for (let s of strs) {
        let k = s.split("").sort().join("");

        if (!m.has(k)) {
            m.set(k, []);
        }

        m.get(k).push(s);
    }

    return Array.from(m.values());
};