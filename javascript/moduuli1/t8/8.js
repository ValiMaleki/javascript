/*Write a program that prompts the user for the start and end year.
The program prints all leap years from the interval given by the user.
Printing is done in an unordered list to the HTML document. (3p)
Example output HTML code:*/

const start_year = parseInt(prompt('enter a starting year! '));
const end_year = parseInt(prompt('enter an ending year! '));
const target = document.querySelector('#target');

for (let year = start_year; year <= end_year; year++) {
  if (year % 400 == 0 || year % 4 == 0 && year % 100 != 0) {
    target.innerHTML += `<li>${year}</li>`;
    console.log(year);
  }
}


