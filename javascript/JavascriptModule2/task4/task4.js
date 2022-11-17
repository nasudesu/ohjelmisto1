


let numlist = []
let userinput;
do {
  userinput = parseInt(prompt(`Give me numbers`));
  if (userinput !== 0)
    numlist.push(userinput);
} while (userinput !== 0);
numlist.sort((a,b) => a-b);
numlist.reverse()
for (let i = 0; i < numlist.length; i++) {
  console.log(numlist[i])
}
