function randomnumber(lol) {
  return Math.floor(Math.random() * lol) + 1
}

let userinput = parseInt(prompt(`Number of sides on the dice?`))

let run = true
while (run) {
  let number = randomnumber(userinput)
  if (number === userinput) run = false
  const node = document.createElement('li')
  node.innerText = number
  document.getElementById('target').appendChild(node)
}
