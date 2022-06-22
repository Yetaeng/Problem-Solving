// Restrictions - Time: O(n), Space: O(n)
// Bonus - Time: O(n log n), Space: O(1)
// 가변 인자, 전달된 인자 사이에 중복이 있으면 true

// Using Frequency Counter
function areThereDuplicates(...args) {
    let collection = {};
    for (let v of args) {
        collection[v] = (collection[v] || 0) +1;
    }
    for (let i in collection) {
        if (collection[i] > 1) {
            return true;
        }
    }
    return false;
};

// Using Multiple Pointers
function areThereDuplicatesSol(...args) {
    // Two pointers
    args.sort((a, b) => a > b);
    let start = 0;
    let next = 1;
    while (next < args.length) {
        if (args[start] === args[next]) {
            return true
        }
        start++
        next++
    }
    return false
}

// One Liner Solution
function areThereDuplicatesSol2() {
    return new Set(arguments).size !== arguments.length;
}

console.log(areThereDuplicates(1, 2, 3));
console.log(areThereDuplicates("a", "b", "c", "a"));