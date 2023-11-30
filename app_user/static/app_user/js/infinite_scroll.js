document.addEventListener("DOMContentLoaded", function () {
    let currentPage = 1;
    const pageSize = 8;
    let isLoadingPosts = false;
    let hasMorePages = true;
    history.scrollRestoration = 'manual';

    // Selection of key elements from article container
    const articleContainer = document.querySelector(".article-container");
    const eachArticleContainer = document.querySelector(".each-article-container")
    const loader = document.querySelector("#loading-symbol");
    const articleTotalPages = JSON.parse(document.getElementById("total_pages_id").textContent);

    const fragment = document.createDocumentFragment();

    // Function for creating each article container
    function createEachArticleContainer(article) {
        // Cloned each article container
        const articleClone = eachArticleContainer.cloneNode(true);

        // Removed the first each article container displayed by html
        if (eachArticleContainer) {
            eachArticleContainer.remove();
        }

        // Make article container visible
        articleContainer.style.display = "flex";

        const titleContainer = articleClone.querySelector(".article-title span:last-child")
        const categoryContainer = articleClone.querySelector(".article-title span:first-child")
        const img = articleClone.querySelector(".article-image-title .image img")
        const timeContainer = articleClone.querySelector(".article-performance .author-time")

        titleContainer.textContent = article.title;
        categoryContainer.textContent = article.category_name;
        timeContainer.textContent = article.created_at;

        img.loading = "lazy";
        img.style.opacity = 0; // Hide image to avoid displaying until fully loaded
        img.src = article.thumbnail;

        // Display image after it is fully loaded.
        function loaded() {
            img.style.opacity = 1;
        }

        // Check if image has finished loading
        if (img.complete) {
            loaded()
        } else {
            img.addEventListener("load", loaded)
        }

        fragment.appendChild(articleClone);
    }

    // Function to fetch data from API
    function fetchArticles(currentPage, pageSize) {
        if (!hasMorePages) {
            loader.style.display = "none";
            return;
        }
        const abortController = new AbortController()
        const signal = abortController.signal

        const timeoutId = setTimeout(() => abortController.abort(), 20000);

        isLoadingPosts = true;

        url = `http://127.0.0.1:8000/api/articles/?page=${currentPage}&page-size=${pageSize}`;
        fetch(url, { signal })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('HTTP error code: ' + response.status)
                }
                return response.json()
            })
            .then((data) => {
                data.articles.forEach((article) => {
                    const timeDifference = moment(article.created_at).fromNow();

                    if (timeDifference.startsWith('a')) {
                        const modifiedString = '1' + timeDifference.slice(1);
                        article.created_at = modifiedString;
                    } else {
                        article.created_at = timeDifference;
                    }

                    createEachArticleContainer(article);
                    articleContainer.appendChild(fragment);
                });

                loader.style.display = "none";

                if (currentPage >= data.total_pages) {
                    hasMorePages = false;
                } else {
                    hasMorePages = true;
                }

                isLoadingPosts = false;

                clearTimeout(timeoutId);
            })
            .catch(error => {
                if (error.name === 'AbortError') {
                    loader.style.display = "none";
                    console.log("Request timed out.");
                    isLoadingPosts = false;
                    hasMorePages = false;
                    return;
                } else if (error instanceof TypeError) {
                    console.log(error);
                    isLoadingPosts = false;
                    hasMorePages = false;
                } else {
                    console.log(error);
                    isLoadingPosts = false;
                    hasMorePages = false;
                }
            });
    }

    if (articleTotalPages > 0) {
        if (currentPage === 1) {
            isLoadingPosts = true;
            fetchArticles(currentPage, pageSize);
            currentPage++;
        }
        window.addEventListener("scroll", function () {
            const {scrollTop, clientHeight, scrollHeight} = document.documentElement;
            if ((scrollTop + clientHeight >= scrollHeight) && !isLoadingPosts) {
                isLoadingPosts = true;
                loader.style.display = "block";
                fetchArticles(currentPage, pageSize);
                currentPage++;
            }
        });
    }
})