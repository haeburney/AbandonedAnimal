const toggleBtn = document.querySelector('.main_list_toogleBtn');
const menu = document.querySelector('#list_ul');
const icons = document.querySelector('#list_ul2');

toggleBtn.addEventListener('click',()=> {
  menu.classList.toggle('active');
  icons.classList.toggle('active');
});
