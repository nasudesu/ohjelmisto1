








let dicenum = parseInt(prompt('Give me dice numbers'));
let sumOFdice = parseInt(prompt('Give me sum on dices'));
let chanse = 0;

for (let i = 0; i <= 10000; i++) {
  let sum = 0;
  for (let j = 0; j < dicenum; j++) {
    let dice = Math.floor(Math.random() * 6) + 1;
    sum += dice;
  }
  if (sum === sumOFdice) {
    chanse++;
  }
}
let probability = ((chanse / 10000) * 100).toFixed(1);
document.querySelector(
    '#target').innerHTML = `Nopat: ${dicenum} Summa: ${sumOFdice} Mahdollisuus: ${probability}%`;