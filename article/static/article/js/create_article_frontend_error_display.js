document.addEventListener('DOMContentLoaded', () => {
    const submit = document.querySelector('#id_submit');

    submit.addEventListener('click', (e) => {
        const titleValue = document.getElementById('id_title').value;
        const categoryValue = document.getElementById('id_category').value;

        if (categoryValue.trim() === '') {
            e.preventDefault();
            const errorMessage = document.querySelector('.category_frontend_error_alert');
            const selectBox = document.getElementById('id_category');

            errorMessage.style.display = "block";
            selectBox.style.border = "1px solid #ba2121";

            selectBox.addEventListener("click", () => {
                errorMessage.style.display = "none";
                selectBox.style.border = "1px solid #030303";
            });
        }
        
        if (titleValue.trim() === '') {
            e.preventDefault();
            const errorMessage = document.querySelector('.title_frontend_error_alert');
            const titleField = document.getElementById('id_title');

            errorMessage.style.display = "block";
            titleField.style.border = "1px solid #ba2121";

            titleField.addEventListener("click", () => {
                errorMessage.style.display = "none";
                titleField.style.border = "1px solid #030303";
            });
        }

        const activeEditor = tinymce.activeEditor;
        const wordcount = activeEditor.plugins.wordcount;
        const numOfWords = wordcount.body.getWordCount();

        const activeEditorContent = activeEditor.getContent();
        const tempDiv = document.createElement("div");
        tempDiv.innerHTML = activeEditorContent;

        const imgTags = tempDiv.querySelectorAll('img');

        if (numOfWords < 10) {
            e.preventDefault();
            const errorMessage = document.querySelector('.content_frontend_error_alert');

            errorMessage.style.display = "block";
                
            activeEditor.on("click", () => {
                errorMessage.style.display = "none";
            });
        } else if (imgTags.length === 0) {
            e.preventDefault();
            const errorMessage = document.querySelector('.no_img_error_alert');

            errorMessage.style.display = "block";
            
            activeEditor.on("click", () => {
                errorMessage.style.display = "none";
            });
        } else if (imgTags.length > 3) {
            e.preventDefault();
            const errorMessage = document.querySelector('.excess_img_error_alert');

            errorMessage.style.display = "block";

            activeEditor.on("click", () => {
                errorMessage.style.display = "none";
            });
        }
    });
});
