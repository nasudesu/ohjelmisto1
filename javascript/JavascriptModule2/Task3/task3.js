

const participantslist = []


for (let i = 1; i < 7; i++) {
  let names = participantslist.push(prompt(`Names of six dogs ${i}`))
}
participantslist.sort()
participantslist.reverse()

for (let i = 0; i < participantslist.length; i++) {
  const node = document.createElement("li")
  const text = document.createTextNode(participantslist[i])
  node.appendChild(text)
  document.getElementById("target").appendChild(node)
}
console.log(participantslist)