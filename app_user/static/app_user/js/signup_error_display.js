document.addEventListener("DOMContentLoaded", function() {
    const usernameContainer = document.querySelector("form .username_container input");
    const emailContainer = document.querySelector("form .email_container input");
    const passwordOneContainer = document.querySelector("form .password_container1 input");
    const passwordTwoContainer = document.querySelector("form .password_container2 input");

    const usernameErrorMessages = document.querySelectorAll("form .username_container span");
    const emailErrorMessages = document.querySelectorAll("form .email_container span");
    const passwordOneErrorMessages = document.querySelectorAll("form .password_container1 span");
    const passwordTwoErrorMessages = document.querySelectorAll("form .password_container2 span");

    if (usernameErrorMessages.length > 0) {
        usernameContainer.addEventListener("click", () => {
            usernameContainer.style.border = "1px solid #030303";
            usernameErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
    }

    if (emailErrorMessages.length > 0) {
        emailContainer.addEventListener("click", () => {
            emailContainer.style.border = "1px solid #030303";
            emailErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
    }

    if (passwordOneErrorMessages.length > 0) {
        passwordOneContainer.addEventListener("click", () => {
            passwordOneContainer.style.border = "1px solid #030303";
            passwordOneErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
    }

    if (passwordTwoErrorMessages.length > 0) {
        passwordTwoContainer.addEventListener("click", () => {
            passwordTwoContainer.style.border = "1px solid #030303";
            passwordTwoErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
    }
})