function validAnagramSelf(str1, str2){
    if (str1.length !== str2.length) {
        return false;
    }
    let frequency1 = {};
    let frequency2 = {};
    
    for (let val of str1) {
        frequency1[val] = (frequency1[val] || 0) +1;
    }
    for (let val of str2) {
        frequency2[val] = (frequency2[val] || 0) +1;
    }
    console.log(frequency1, frequency2);
    for (let key in frequency1) {
        if (frequency1[key] !== frequency2[key]) {
            return false;
        }
    }
    
    return true;
}

function validAnagramSol(first, second) {
    if (first.length !== second.length) {
        return false;
    }

    const lookup = {};

    for (let i = 0; i < first.length; i++) {
        let letter = first[i];
        // if letter exists, increment, otherwise set to 1
        lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1;
    }
    console.log(lookup)

    for (let i = 0; i < second.length; i++) {
        let letter = second[i];
        // can't find letter or letter is zero then it's not an anagram
        if (!lookup[letter]) {
            return false;
        } else {
            lookup[letter] -= 1;
        }
    }

    return true;
}

console.log(validAnagramSelf('', ''));
console.log(validAnagramSelf('anagrams', 'nagaramm'));