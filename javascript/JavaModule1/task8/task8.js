


let start = parseInt(prompt(`Give me start yer`))
let end = parseInt(prompt(`Give me end yer`))

//let times = end - start

for (let i = start; i <= end ; i++) {
  //  let yearling = start+i

  const node = document.createElement("li");
  node.innerText = i;
  //const textnodes = document.createTextNode(i);
  //node.appendChild(textnodes);

  if (0 === i % 4 && (0 !==  i % 100 || 0 === i % 400)) {
    document.getElementById("target").appendChild(node);
}}
