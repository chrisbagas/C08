const csrf = document.getElementsByName('csrfmiddlewaretoken')
const first_name = document.getElementById('id_first_name');
const last_name = document.getElementById('id_last_name');
const image = document.getElementById('id_image');
const bio = document.getElementById('id_bio');

form.addEventListener("submit", submitHandler);

function submitHandler(e) {
    e.preventDefault();

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('first_name', first_name.value)
    fd.append('last_name', last_name.value)
    fd.append('image', image.files[0])
    fd.append('bio', bio.value)

    $.ajax({
        type        : 'POST', 
        url         : "",
        enctype     : 'multipart/form-data',
        data        : fd,  
        dataType    : 'json',
        success     : function(msg) {
                        console.log(msg)
                        if (msg.message === 'success') {
                            alert('Profile updated!');

                        }
                    },
        cache       : false,
        contentType : false,
        processData : false,
    });
}