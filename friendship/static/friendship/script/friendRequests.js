document.addEventListener("click", handleFriendRequest);



async function handleFriendRequest(event) {
    const action = event.target.dataset.requestAction;
    if (action === undefined) {
        return;
    }

    const viewdUserId = event.target.closest("div[data-userId]").dataset.userid;
    
    const response = await fetch("/friendRequests", {
        method: "POST",
        body: JSON.stringify({
            action: action,
            viewdUserId: viewdUserId
        })
    });

}