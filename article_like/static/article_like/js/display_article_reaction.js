document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".share-like-comment .like");

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        const reactionValue = e.submitter.value;
        const pathname = window.location.pathname;

        splitedPathname = pathname.split('/');
        slug_text = splitedPathname[splitedPathname.length - 1];

        function submitReaction () {
            const url = `/api/articles/${slug_text}/like`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({
                    reaction: reactionValue,
                    pathname: window.location.pathname,
                }),
            })
                .then(response => {
                    if (response.redirected) {
                        window.location.href = response.url
                    } else if (!response.ok) {
                        throw new Error('HTTP error status: ' + response.status);
                    } else {
                        return response.json();
                    }
                })
                .then(data => {
                    const likeIcon = document.querySelector(".share-like-comment .like .like-btn-style");
                    const dislikeIcon = document.querySelector(".share-like-comment .like .dislike-btn-style");
                    const totalLikes = document.querySelector(".share-like-comment .total-likes");
                    const totalDislikes = document.querySelector(".share-like-comment .total-dislikes");

                    if (data.reaction === 'like') {
                        likeIcon.style.backgroundColor = "#00FF00";
                        dislikeIcon.style.backgroundColor = "white";
                        totalLikes.innerHTML = data.total_likes;
                        totalDislikes.innerHTML = data.total_dislikes;
                    } else if (data.reaction === 'dislike') {
                        likeIcon.style.backgroundColor = "white";
                        dislikeIcon.style.backgroundColor = "#00FF00";
                        totalLikes.innerHTML = data.total_likes;
                        totalDislikes.innerHTML = data.total_dislikes;
                    } else {
                        likeIcon.style.backgroundColor = "white";
                        dislikeIcon.style.backgroundColor = "white";
                        totalLikes.innerText = data.total_likes;
                        totalDislikes.innerText = data.total_dislikes;
                    }
                })
                .catch(error => {
                    console.error(error.message);
                });
        }
        submitReaction();
    });
});