







let answer = 0
const question = parseFloat(prompt(`number of dice rolls?`))
for (let i = 0; i <= question; i++) {
  const throws = Math.floor(Math.random()*6)+1;
  console.log(throws);
  answer += throws;
}



