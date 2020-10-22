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


    if (response.ok) {
        const json = await response.json();
        const requestWrapper = event.target.closest(".request-control");
        newControl = "";
        if (action == "cancel" || action == "remove") {
            newControl = `<button class="btn btn-primary" data-request-action="add">ِAdd Friend</button>`;
        } else if (action == "confirm") {
            newControl = `<i class="fas fa-check-circle" title="Friends" style="color: green;"></i>`;
        } else if (action == "add") {
            newControl = `<button  class="btn btn-danger" data-request-action="cancel">Cancel Request</button>`;
        }
        requestWrapper.innerHTML = newControl;
    }

}