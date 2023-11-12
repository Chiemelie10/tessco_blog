document.addEventListener("DOMContentLoaded", function () {
    const articleContainer = document.querySelector(".article-container");
    const eachArticleContainer = document.querySelector(".each-article-container");
    const loader = document.querySelector("#loading-symbol");

    currentPage = 1;
    pageSize = 8;
    let isLoadingPosts = false;
    let hasMorePages = true;
    history.scrollRestoration = 'manual';

    const fragment = document.createDocumentFragment();

    function createEachArticleContainer(article) {
        const articleClone = eachArticleContainer.cloneNode(true);

        articleClone.querySelector(".article-title span:last-child").textContent = article.title
        articleClone.querySelector(".article-title span:first-child").textContent = article.category_name
        articleClone.querySelector(".article-image-title .image img").src = article.thumbnail
        articleClone.querySelector(".article-image-title .image img").alt = article.title
        articleClone.querySelector(".article-performance .author-time").textContent = article.created_at

        fragment.appendChild(articleClone);
    }

    function fetchArticles(currentPage, pageSize) {
        if (!hasMorePages) {
            loader.style.display = "none"
            return;
        }

        url = `http://127.0.0.1:8000/api/articles/?page=${currentPage}&page-size=${pageSize}`;
        fetch(url)
            .then((response) => response.json())
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

                if (currentPage === data.total_pages) {
                    hasMorePages = false;
                } else {
                  hasMorePages = true;
                }

                isLoadingPosts = false;
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
                isLoadingPosts = false;
            });
    }

    window.addEventListener("scroll", function () {
        const {scrollTop, clientHeight, scrollHeight} = document.documentElement;
        if ((scrollTop + clientHeight + 250 >= scrollHeight) && !isLoadingPosts) {
            isLoadingPosts = true;
            loader.style.display = "block";
            currentPage++;
            fetchArticles(currentPage, pageSize);
        }
    });
})