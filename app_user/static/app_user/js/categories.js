document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const overlay = document.querySelector(".overlay");

    menuToggle.addEventListener("click", function() {
        if (menu.style.display === "none" || menu.style.display === "") {
            // const viewportOffset = menu.getBoundingClientRect();
            // const top = viewportOffset.top;
            let top = 0;
            top = document.documentElement.scrollTop;
            menu.style.display = "block";
            menu.style.top = top + "px";
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