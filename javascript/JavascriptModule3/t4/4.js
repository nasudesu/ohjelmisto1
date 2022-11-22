'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let i = 0; i < students.length; i++) {
  const op = document.createElement('option')
  op.setAttribute("value", `${students[i].id}`)
  const node = document.createTextNode(`${students[i].name}`)
  op.appendChild(node)
  document.getElementById('target').appendChild(op)
}
