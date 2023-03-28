'use strict'

let result, max;
function rollDice(max) {
    return 1 + Math.floor(Math.random() * max);
}

const ul = document.createElement("ul");

max = prompt("Enter the number of sides of the dice: ");

while (result != max) {
    result = rollDice(max);
    ul.innerHTML += `<li>${result}</li>`;
}

document.body.appendChild(ul);