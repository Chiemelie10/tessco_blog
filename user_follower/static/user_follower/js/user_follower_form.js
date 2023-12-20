document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("id_user_follower_form");
    const submitBtn = document.getElementById("id_submit_btn");

    if (form !== null) {
        const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const following = document.getElementById("id_following").value;
        const followLetter = document.getElementById("id_follow");
        const spinner = document.getElementById("spinner");
        
        submitBtn.addEventListener("click", function (e) {
            e.preventDefault();
            spinner.style.display = 'block';

            function user_follower_form () {
                url = "/api/users/follow";
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfmiddlewaretoken,
                    },
                    body: JSON.stringify({
                        following: following,
                    }),
                })
                    .then((response) => {
                        if (!response.ok)
                            throw new Error('HTTP error: ' + response.message);
                        return response.json();
                    })
                    .then(data => {
                        if (data.new_state === 'Follow') {
                            followLetter.innerText = "Follow";
                            spinner.style.display = 'none';
                        } else {
                            followLetter.innerText = "Unfollow";
                            spinner.style.display = 'none';
                        }
                    })
                    .catch(error => {
                        spinner.style.display = 'none';
                        console.error(error);
                    });
            }
            user_follower_form();
        });
    }
});