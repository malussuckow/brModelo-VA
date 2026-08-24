const btnMenu = document.getElementById("btn-dash");
const sidebar = document.querySelector(".dash-aside");

btnMenu.addEventListener("click", function () {
    sidebar.classList.toggle("fechada");
});