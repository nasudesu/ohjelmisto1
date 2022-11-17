function contact(users) {
  document.querySelector('#target').innerHTML = `${users[0]}${users[1]}${users[2]}${users[3]}`
}
let users = ['Johnny', 'DeeDee', 'Joey', 'Marky']
contact(users)

/* Kokeile kans prompti tapa :)
function contact2(users) {
  document.querySelector('#target2').innerHTML = `${users[0]}${users[1]}${users[2]}${users[3]}`
}

let users2 = []
for (let i = 0; i < 4; i++) {
  let usernput = prompt(`Give me name ${4-i}`)
  users2.push(usernput)
}
contact2(users2)
*/

