const items = ["First item", "Second item", "Third item"]
for (let i = 0; i < items.length; i++) {
  const list = document.createElement(`li`)
  list.innerText = items[i]
  document.getElementById(`target`).appendChild(list)
}
const li1 = document.querySelectorAll('li')[1]
li1.innerHTML = '<li class="my-item">Second item</li>'