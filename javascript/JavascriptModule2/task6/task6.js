function randomnumber() {
  return Math.floor(Math.random() * 6) + 1
}


let run = true
while (run) {
  let number = randomnumber()
  if (number === 6) run = false
  const node = document.createElement('li')
  node.innerText = number
  document.getElementById('target').appendChild(node)
}
