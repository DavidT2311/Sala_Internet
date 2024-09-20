document.addEventListener("DOMContentLoaded", () => {
    const menuDashboard = document.querySelector(".menu-dash");
    const iconMenu = document.querySelector(".toggle i");

    function updateMenuState(isOpen) {
        menuDashboard.classList.toggle("open", isOpen);
    }

    menuDashboard.addEventListener("mouseenter", () => {
        updateMenuState(true);
    });

    menuDashboard.addEventListener("mouseleave", () => {
        updateMenuState(false);
    });
});
