const open_menu_btn = document.querySelector(".open__menu");
const close_menu_btn = document.querySelector(".close__menu");
const menu = document.querySelector(".mobile__menu");
open_menu_btn.addEventListener("click", () => {
  menu.classList.remove("hidden");
});
close_menu_btn.addEventListener("click", () => {
  menu.classList.add("hidden");
});
