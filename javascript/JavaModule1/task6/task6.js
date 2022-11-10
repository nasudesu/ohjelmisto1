const choice = confirm('Should I calculate the square root?');
if (choice === true) {
  const question1 = parseFloat(prompt(`Give me some number`));
  const answer = (Math.sqrt(question1));
  document.querySelector(
      '#target').innerHTML = `Square root of ${question1} is ${answer}`;
} else if (choice === false) {
  document.querySelector(
      '#target').innerHTML = `The square root is not calculated`;
}








