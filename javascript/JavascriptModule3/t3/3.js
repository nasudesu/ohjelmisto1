'use strict';
const names = ['John', 'Paul', 'Jones'];
for (let i = 0; i < names.length; i++) {
  const list = document.createElement(`li`)
  list.innerText = names[i]
  document.getElementById(`target`).appendChild(list)
}
const li1 = document.querySelectorAll('li')[1]
li1.innerHTML = '<li class="my-item">Second item</li>'
