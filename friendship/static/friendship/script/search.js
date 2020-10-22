const searchInput = document.getElementById('search-input');
if (searchInput !== null) {
    searchInput.addEventListener('input', toggleSearchResult);


    searchInput.addEventListener('blur', () => {
        document.getElementsByClassName('search-result')[0].innerHTML = "";
    });
    
}


async function toggleSearchResult(event) {
    const ul = document.getElementsByClassName('search-result')[0];

    if (event.target.value === "") {
        ul.innerHTML = "";
        return;
    }
    const name = event.target.value;
    const response = await fetch(`/search?name=${name}`);

    if (response.ok) {
        const json = await response.json();
        console.log(json);
    }
}