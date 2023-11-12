document.addEventListener("DOMContentLoaded", function() {
    const headlineContainer = document.querySelector(".headline-container");
    const headlineLink = document.querySelector(".each-headline-link");

    const fragment = document.createDocumentFragment();

    function createHeadline(article) {
        const articleClone = headlineLink.cloneNode(true);

        articleClone.querySelector(".headline-image").src = article.thumbnail;
        articleClone.querySelector(".headline-image").alt = "Article Image";
        articleClone.querySelector(".headline-category-title span:last-child").textContent = article.title;
        articleClone.querySelector(".headline-category-title span:first-child").textContent = article.category_name;

        fragment.appendChild(articleClone)
    }

    function fetchHeadline() {
        url = "http://127.0.0.1:8000/api/articles/headlines";
        fetch(url)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                if (data.length > 0) {
                    i = 0;
                    headlineContainer.innerHTML = "";
                    createHeadline(data[i]);
                    headlineContainer.appendChild(fragment);

                    i += 1

                    setInterval(() => {
                        headlineContainer.innerHTML = "";
                        createHeadline(data[i]);
                        headlineContainer.appendChild(fragment);
                        i += 1;
                        if (i === data.length) {
                            i = 0;
                        }
                    }, 10000);
                } else {
                  headlineContainer.innerHTML = "No headline available";
                }
            })
            .catch((error) => {
                console.error("Error fetching data: ", error);
            });
    }
    fetchHeadline();
})