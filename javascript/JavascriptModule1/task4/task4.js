


const name = prompt('What is your name');
const hat = Math.random();
if (hat <= 0.25) {
  document.querySelector('#target1').innerHTML = `${name} you are Daredevil`
} else if (hat >= 0.26 && hat <= 0.50) {
  document.querySelector('#target1').innerHTML = `${name} you are Slytherin`
} else if (hat >= 0.51 && hat <= 0.75) {
  document.querySelector('#target1').innerHTML = `${name} you are Hufflepuff`
} else if (hat >= 0.76 && hat <= 1) {
  document.querySelector('#target1').innerHTML = `${name} you are Ravenclaw`
}
