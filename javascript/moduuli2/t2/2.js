/*Write a program that asks the user for the number of participants.
 After this, the program asks for the names of all participants.
  Finally, the program prints the names of the participants
  on the web page in an ordered list (<ol>) in alphabetical order. (2p)*/

let names, participants;
const name_list = [];
const target = document.querySelector('#target');
participants = parseInt(prompt('how many r gonna participate? '));
do {
  names = prompt('Enter the names! ');
  name_list.push(names);

} while (name_list.length < participants);
name_list.sort();
for (let i = 0; i < name_list.length; i++) {

  target.innerHTML = `<ol>${name_list}</ol>`;
  console.log(name_list[i])

}

