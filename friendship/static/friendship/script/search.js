const searchInput = document.getElementById('search-input');
if (searchInput !== null) {
    searchInput.addEventListener('input', toggleSearchResult);


    searchInput.addEventListener('blur', () => {
        setTimeout(() => {
            document.getElementsByClassName('search-result')[0].innerHTML = "";
        }, 200);
    });
    
}


async function toggleSearchResult(event) {
    const ul = document.getElementsByClassName('search-result')[0];

    if (event.target.value === "") {
        ul.innerHTML = "";
        return;
    }
    ul.innerHTML = "";
    const name = event.target.value;
    const response = await fetch(`/search?name=${name}`);

    if (response.ok) {
        const json = await response.json();
        for (let [userId, userInfo] of Object.entries(json)) {
            ul.insertAdjacentHTML("beforeend", 
            `<li class="list-group-item search-result-item">
            <a href="/profile/${userId}">
              <img src="${userInfo.avatar}" alt="">
            </a>
            <strong>${userInfo.username}</strong>
        </li>`);
        }
    }


}