document.addEventListener("DOMContentLoaded", () => {
    const scrollToTopButton = document.querySelector('.scroll-to-top');

    scrollToTopButton.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            left: 0,
            behavior: "smooth"
        });
    });
});