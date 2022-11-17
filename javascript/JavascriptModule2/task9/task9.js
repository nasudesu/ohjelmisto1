function even(array) {
  let numlist = []
  for (let i = 0; i < array.length+2; i++) {
    if (i % 2 === 0) numlist.push(i)
  }
  return console.log(numlist)
}

let numlist = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
console.log(numlist)
even(numlist)
