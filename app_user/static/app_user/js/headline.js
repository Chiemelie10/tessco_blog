document.addEventListener("DOMContentLoaded", function() {
    const headlineContainer = document.querySelector(".headline-container");
    const headlineLink = document.querySelector(".each-headline-link");
    const headlineImageContainer = document.querySelector(".headline-image-container");

    const fragment = document.createDocumentFragment();

    function createHeadline(article) {
        const articleClone = headlineLink.cloneNode(true);

        const img = articleClone.querySelector(".headline-image")
        const title = articleClone.querySelector(".headline-category-title span:last-child")
        const category = articleClone.querySelector(".headline-category-title span:first-child")

        title.textContent = article.title;
        category.textContent = article.category_name;

        img.loading = "lazy";
        img.style.opacity = 0;
        img.src = article.thumbnail;

        function loaded() {
            img.style.opacity = 1;
        }

        if (img.complete) {
            loaded()
        } else {
            img.addEventListener("load", loaded)
        }

        fragment.appendChild(articleClone)
    }

    function fetchHeadline() {
        url = "/api/articles/headlines";
        fetch(url)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                if (data.length > 0) {
                    headlineImageContainer.style.display = "flex"
                    if (data.length === 1) {
                        i = 0;
                        headlineContainer.innerHTML = "";
                        createHeadline(data[i]);
                        headlineContainer.appendChild(fragment);
                    } else if (data.length > 1) {
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
                    }
                } else {
                    headlineContainer.innerHTML = "";
                    // headlineContainer.style.display = "flex";
                    // headlineContainer.style.alignItems = "center";
                    // headlineContainer.style.backgroundColor = "#2a597e";
                    // headlineContainer.style.color = "#ffffff";
                    // headlineContainer.style.fontSize = "16px";
                    const movingTextContainer = document.createElement("span");
                    headlineContainer.classList.add("no-headline-container");
                    movingTextContainer.classList.add("no-headline-container-content");
                    movingTextContainer.textContent = `
                        Today's trending stories to be uploaded soon, 
                        meanwhile checkout other interesting articles below.
                    `;
                    headlineContainer.appendChild(movingTextContainer);
                }
            })
            .catch((error) => {
                console.error("Error fetching data: ", error);
            });
    }
    fetchHeadline();
})