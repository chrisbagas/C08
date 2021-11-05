//// Get the modal
//var modal = document.getElementById("delete-modal");
//
//// Get the button that opens the modal
//var btn = document.getElementById("delete-post");

var primkey;
var id;

$(".delete-post").click( function() {
    primkey = $(this).children("input[name='post-prim-key']").attr("value");
    console.log(primkey);
    id = `.delete-modal-wrapper.${primkey}`;
    console.log(id);
    $(id).css("display", "block");
    $(".post-wrapper").css("--tw-blur", "blur(6px)");
    
    //$('#delete-form').wrapInner("<form id='delete-form' action='/blog/" + primkey + "' method='POST'></form>").unwrap();
});

$(".cancel").click(function () {
    $(id).css("display", "none");
    $(".post-wrapper").css("--tw-blur", "blur(0)");
});

$(window).click(function (event) {
    console.log($(id));
    console.log(event.target);
    if ($(event.target).attr("class") == $(id).attr("class")) {
        $(id).css("display", "none");
        $(".post-wrapper").css("--tw-blur", "blur(0)");
    }
});

$(".delete-form").submit(function (event) {
    event.preventDefault();
    $.ajax({
        url: $(this).attr("action"),
        type: "POST",
        data: $(this).serialize(),
        success: function (result) {
            //$(`.thumbnail-wrapper.${primkey}`).css({
            //    "height": 0,
            //    "min-height": 0,
            //    "opacity": 0,
            //    
            //});
            //$(`.header-wrapper.${primkey}, .info-wrapper.${primkey}, .info-footer.${primkey}`).css({
            //    "height": 0,
            //    "opacity": 0,
            //    
            //});

            $(`.thumbnail-wrapper.${primkey}`).animate({
                "height": 0,
                "min-height": 0,
                "opacity": 0,
            }, 600, "swing");
    
            $(`.header-wrapper.${primkey}, .info-wrapper.${primkey}, .info-footer.${primkey}`).animate({
                "height": 0,
                "min-height": 0,
                "opacity": 0,
            }, 600, "swing", function () {
                $(`.${primkey}`).remove(".thumbnail-wrapper, .header-wrapper, .info-wrapper, .info-footer");
            });

            //$(`.thumbnail-wrapper.${primkey}, .header-wrapper.${primkey}, .info-wrapper.${primkey}, .info-footer.${primkey}`).slideUp(12000, "linear");
            //$(`.${primkey}`).toggle(6000).slideUp(12000);
            $(id).css("display", "none");
            $(".post-wrapper").css("--tw-blur", "blur(0)");
        }
    });
});



//// When the user clicks the button, open the modal 
//btn.onclick = function() {
//  modal.style.display = "block";
//}
//
//// When the user clicks anywhere outside of the modal, close it
//window.onclick = function(event) {
//  if (event.target == modal) {
//    modal.style.display = "none";
//  }
//}