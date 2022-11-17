function listofcandy(kek) {
  let candidates = [];
  for (let i = 0; i < kek; i++) {
    let candidate = {
      name: '',
      votes: 0,
    };
    candidates.push(candidate);
    let userinput2 = prompt(`Name of the ${i + 1} candidate`);
    candidates[i].name = `${userinput2}`;
  } return candidates
}

let userinput = prompt(`Number of candidates`)
let candidate = listofcandy(userinput)
let voters = prompt(`Number of voters`)
console.log(candidate)
for (let i = 0; i < voters; i++) {
  let vote = prompt(`Voter ${i+1} chose candidate to vote for`)
  for (let j = 0; j < candidate.length; j++) {
    if (vote === candidate[j].name) {
      candidate[j].votes += 1
    }
  }
}
console.log(candidate)

