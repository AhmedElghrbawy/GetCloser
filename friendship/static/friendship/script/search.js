const searchInput = document.getElementById('search-input');
if (searchInput !== null) {
    searchInput.addEventListener('input', toggleSearchResult);


    searchInput.addEventListener('blur', () => {
        document.getElementsByClassName('search-result')[0].innerHTML = "";
    });
    
}


function toggleSearchResult(event) {
    const ul = document.getElementsByClassName('search-result')[0];

    if (event.target.value === "") {
        ul.innerHTML = "";
        return;
    }
    ul.insertAdjacentHTML("beforeend", `<li class="list-group-item"> ${event.target.value}</li>`);
}