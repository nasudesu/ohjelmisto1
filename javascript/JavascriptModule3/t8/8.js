function calculate() {
  let operation = document.getElementById(`operation`)
  let operational = operation.value
  let result = 0

  if (operational === "add") {
    let num1 = parseInt(document.getElementById(`num1`).value)
    let num2 = parseInt(document.getElementById(`num2`).value)
    result = num1 + num2
  }
  else if (operational === "sub") {
    let num1 = parseInt(document.getElementById(`num1`).value)
    let num2 = parseInt(document.getElementById(`num2`).value)
    result = num1 - num2
  }

  else if (operational === "multi") {
    let num1 = parseInt(document.getElementById(`num1`).value)
    let num2 = parseInt(document.getElementById(`num2`).value)
    result = num1 * num2
  }

  else if (operational === "div") {
    let num1 = parseInt(document.getElementById(`num1`).value)
    let num2 = parseInt(document.getElementById(`num2`).value)
    result = (num1 / num2).toFixed(2)
  }

  document.getElementById(`result`).innerText = `Result ${result}`
}

let button = document.querySelector("button")
button.addEventListener("click", calculate)