function dice_roll() {
  randomNum = Math.floor(Math.random() * 6) + 1;

  return randomNum;
}

let result, dice_list = [], cont = true;

do {
  result = dice_roll();
  if (result == 6) {
    cont = false;
  }
  dice_list.push(result);

} while (cont);
const list = document.getElementById('dice_list');

for (let i = 0; i < dice_list.length; i++) {
  const li = document.createElement('li');
  li.innerText = 'dice roll---'+dice_list[i];
  list.appendChild(li);
}