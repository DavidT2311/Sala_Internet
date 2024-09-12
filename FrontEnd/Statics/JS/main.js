document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector(".toggle");
    const menuDashboard = document.querySelector(".menu-dash");
    const iconMenu = toggle.querySelector("i");
    const linksMenu = document.querySelectorAll(".enlace");

    function updateMenuState(isOpen) {
        menuDashboard.classList.toggle("open", isOpen);
        iconMenu.classList.toggle("bx-menu", !isOpen);
        iconMenu.classList.toggle("bx-x", isOpen);
    }

    function closeMenuAfterDelay() {
        setTimeout(() => {
            updateMenuState(false);
        }, 100000);
    }

    toggle.addEventListener("click", () => {
        const isOpen = menuDashboard.classList.contains("open");
        updateMenuState(!isOpen);
        if (!isOpen) {
            closeMenuAfterDelay();
        }
    });

    linksMenu.forEach(enlace => {
        enlace.addEventListener("click", () => {
            updateMenuState(true);
            closeMenuAfterDelay();
        });
    });

    const menuOpen = menuDashboard.classList.contains("open");
    if (menuOpen) {
        closeMenuAfterDelay();
    }
});
