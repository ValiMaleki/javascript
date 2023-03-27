/*Write a program that rolls user defined number of dice and displays the sum of the
results of the dice rolls.(2p)
First, program asks the user for the number of dice rolls.
Then the program throws a die as many times as the user defined.
Print the sum of the results in the console or in the HTML document.*/

let dice_roll,target1, randomNum, sum = 0;
target1 = document.querySelector('#target1')
dice_roll = parseInt(prompt('Enter the number of dice rolls:'));

for (let i = 1; i <= dice_roll; i++) {
  randomNum = Math.floor(Math.random() * 6) + 1;
//  document.querySelector('#target').innerHTML = i+'. dice'+ randomNum;
  target1.innerHTML += "<br>"+randomNum
  console.log(i + 'and ' + randomNum);
  sum += randomNum;

}
document.querySelector('#target').innerHTML = 'sum of dices ' + sum;






