document.addEventListener("DOMContentLoaded", () => {
    const categoryErrorMessageContainer = document.querySelectorAll(".category_container span");
    const titleErrorMessageContainer = document.querySelectorAll(".title_container span");

    const categoryContainer = document.querySelector("#id_category");
    const titleContainer = document.querySelector("#id_title");

    if (categoryErrorMessageContainer.length > 0) {
        categoryContainer.addEventListener("click", () => {
            categoryContainer.style.border = "1px solid #030303";
            categoryErrorMessageContainer.forEach((span) => {
                span.style.display = "none";
            });
        });
    }

    if (titleErrorMessageContainer.length > 0) {
        titleContainer.addEventListener("click", () => {
            titleContainer.style.border = "1px solid #030303";
            titleErrorMessageContainer.forEach((span) => {
                span.style.display = "none";
            });
        });
    }
});