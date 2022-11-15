
numberslist = [];

for (let i = 0; i < 5; i++) {
  const numbers = parseInt(prompt(`Give me five numbers`));
  numberslist.push(numbers)
}
for (let i = numberslist.length-1; i >= 0; i--) {
  console.log(numberslist[i])
}
