function solution(nums) {
    const countedTypes = nums.reduce((allTypes, type) => {
          if (type in allTypes) {
              allTypes[type]++
          } else {
              allTypes[type] = 1
          }
          return allTypes;
      }, {});
    
    let max = nums.length / 2;
    let selectedTypes = Object.keys(countedTypes).length;
    
    return max > selectedTypes ? selectedTypes : max;
}