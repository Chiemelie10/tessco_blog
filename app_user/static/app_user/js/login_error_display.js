document.addEventListener("DOMContentLoaded", function() {
    const usernameContainer = document.querySelector("form .username_container input");
    const passwordContainer = document.querySelector("form .password_container input");

    const nonFieldErrorMessages = document.querySelectorAll("form .alert_non_field_error span");
    const usernameErrorMessages = document.querySelectorAll("form .username_container span");
    const passwordErrorMessages = document.querySelectorAll("form .password_container .display_error");

    if (nonFieldErrorMessages.length > 0) {
        usernameContainer.style.border = "1px solid #ba2121";
        passwordContainer.style.border = "1px solid #ba2121";

        usernameContainer.addEventListener("click", () => {
            usernameContainer.style.border = "1px solid #030303";
            passwordContainer.style.border = "1px solid #030303";
            nonFieldErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
        passwordContainer.addEventListener("click", () => {

            passwordContainer.style.border = "1px solid #030303";
            usernameContainer.style.border = "1px solid #030303";
            nonFieldErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });    
    }

    if (usernameErrorMessages.length > 0) {
        usernameContainer.addEventListener("click", () => {
            usernameContainer.style.border = "1px solid #030303";
            usernameErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
    }

    if (passwordErrorMessages.length > 0) {
        passwordContainer.addEventListener("click", () => {
            passwordContainer.style.border = "1px solid #030303";
            passwordErrorMessages.forEach((span) => {
                span.style.display = "none";
            });
        });
    }
})