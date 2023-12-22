document.addEventListener('DOMContentLoaded', () => {
    let pTags = document.querySelectorAll('.content p');

    for (let i = 0; i < pTags.length; i++) {
        let pTag = pTags[i];
        if (pTag.innerHTML.includes('&nbsp;') || pTag.innerHTML === '') {
            pTag.style.display = "none";
        }
    }
});