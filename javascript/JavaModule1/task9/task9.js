









let num = parseInt(prompt(`Gimmy a number`));

for (let i = 2; i <= num; i++) {
  if (num % i === 0) {
    if (i !== num) {
      document.querySelector('#target').innerHTML = `${num} ei ole alkuluku`;
      break;
    } else {
      document.querySelector('#target').innerHTML = `${num} on alkuluku`;
    }
  }
}

