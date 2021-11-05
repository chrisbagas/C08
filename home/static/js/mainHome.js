function myFunc(){
    let user = document.getElementById("logged-in");
    let anon = document.getElementById("anonymous");

    if (user === null){
        let x = document.getElementById("status-container");
        if (x.style.display === "none") {
            x.style.display = "block";
        }
        // Success! Reload the page
        $("#status").text("You must be signed in if you want to give the review");
    } else if (anon === null){
        window.location.href = "/feedback";
    }
}

$(document).ready(function(){
    $("#click").click(function(){
        $.ajax({
            url: "",
            success: function() {
                myFunc();
            }
        });
    });
});