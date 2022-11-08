

const num1 = parseFloat(prompt('Gib number'));
const num2 = parseFloat(prompt('Gib number'));
const num3 = parseFloat(prompt('Gib number'));


document.querySelector("#target1").innerHTML = num1 + num2 + num3;
document.querySelector("#target2").innerHTML = num1 * num2 * num3;
document.querySelector("#target3").innerHTML = num1+num2+num3 / 3;