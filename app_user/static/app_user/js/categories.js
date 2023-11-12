document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const overlay = document.querySelector(".overlay");

    menuToggle.addEventListener("click", function() {
        if (menu.style.display === "none" || menu.style.display === "") {
            menu.style.display = "block";
            menu.scrollTop = 0;
            overlay.style.display = "block";
            document.body.style.overflow = "hidden";
        } else {
          menu.style.display = "none";
          overlay.style.display = "none";
          document.body.style.overflow = "auto";
        }
    });

    overlay.addEventListener("click", function() {
        if (overlay.style.display === "block") {
            overlay.style.display = "none";
            menu.style.display = "none";
            document.body.style.overflow = "auto";
        }
    });
});