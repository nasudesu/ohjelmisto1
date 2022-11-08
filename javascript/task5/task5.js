

const number = parseInt(prompt('Gimmy number'))
if (0 === number % 4 && (0 !==  number % 100 || 0 === number % 400)) {
  console.log('knjnjn')
  document.querySelector('#target').textContent = "Vuosi on karkaus vuos" + number;
} else {
  document.querySelector('#target').textContent = "Vuosi ei ole karrkaus vuos" + number;
}
