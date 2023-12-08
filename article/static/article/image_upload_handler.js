tinymce.init({
    selector: 'form',
    theme: 'modern'
})

document.addEventListener('DOMContentLoaded', () => {
    const submit = document.querySelector('#id_submit');

    submit.addEventListener('click', () => {
        tinymce.activeEditor.uploadImages(function(success) {
            if (success) {
                document.forms[0].submit();
            }
        });
    });
});
