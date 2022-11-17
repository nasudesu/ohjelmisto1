

let numlist = []

let on = true
let userinput = parseInt(prompt(`Anna kokonais luku`))
numlist.push(userinput)
while (on) {
  if (userinput in numlist) {
    console.log(`${userinput} On jo listassa`)
    break
  }
  userinput = parseInt(prompt(`Anna kokonais luku`))
  numlist.push(userinput)
}
numlist.pop()
console.log(numlist)
