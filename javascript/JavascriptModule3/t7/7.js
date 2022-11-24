function mouseover() {
  document.querySelector(`#target`).setAttribute(`src`, `img/picB.jpg`)

}

function mouseout() {
  document.querySelector(`#target`).setAttribute(`src`, `img/picA.jpg`)

}


const trigger = document.getElementById(`trigger`)
trigger.addEventListener('mouseover', mouseover)
trigger.addEventListener('mouseout', mouseout)



