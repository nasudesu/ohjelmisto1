






let start = parseInt(prompt(`Give me start yer`))
let end = parseInt(prompt(`Give me end yer`))

let times = end - start
for (let i = 0; i <= times ; i++) {
  let yearling = start+i
  const node = document.createElement("li");
  const textnodes = document.createTextNode(yearling);
  node.appendChild(textnodes);
  if (0 === yearling % 4 && (0 !==  yearling % 100 || 0 === yearling % 400)) {
    document.getElementById("target").appendChild(node)
}}
