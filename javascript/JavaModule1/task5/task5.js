

const number = parseInt(prompt('Gimmy number'))
if (0 === number % 4 && (0 !==  number % 100 || 0 === number % 400)) {
  console.log('knjnjn')
  document.querySelector('#target').textContent =
      `${number} on karvuos`
} else {
  document.querySelector('#target').textContent =
      `${number} ei ole karkaus vuos`
}
