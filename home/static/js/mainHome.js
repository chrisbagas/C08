function myFunction() {
    var x = document.getElementById("status-container");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
} 

$(document).ready(function(){
    $("#click").click(function(){
        $.ajax({
            url: "",
            statusCode: {
                200: function() {
                    // Success! Reload the page
                    $("#status").text("You must be signed in if you want to give the review");
                },
                401: function() {
                    // Unauthorized, redirect to home
                    window.location.href = "/feedback";
                },
            }, 
        });
    });
});