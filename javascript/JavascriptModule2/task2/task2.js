

const participantslist = []

let participants = parseInt(prompt(`Number of participants?`))

for (let i = 1; i < participants+1; i++) {
  let names = participantslist.push(prompt(`Participant ${i} name?`))
}
participantslist.sort()

for (let i = 0; i < participantslist.length; i++) {
  const node = document.createElement("li")
  const text = document.createTextNode(participantslist[i])
  node.appendChild(text)
  document.getElementById("target").appendChild(node)
}
