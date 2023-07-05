const menu = document.querySelector(".menu");
const open_menu = document.querySelector(".open-menu");
const close_menu = document.querySelector(".close-menu");

function toggleMenu() {
    menu.classList.toggle("menu_opened");

}

open_menu.addEventListener("click", toggleMenu);
close_menu.addEventListener("click", toggleMenu);