const alertBox = document.getElementById('alert-box')
const imgBox = document.getElementById('img-box')
const form = document.getElementById('p-form')

const nama = document.getElementById('id_Nama')
const tanggal = document.getElementById('id_Tanggal')
const waktu = document.getElementById('id_Waktu')
const media = document.getElementById('id_Media')
const tipe = document.getElementById('id_Tipe')
const deskripsi = document.getElementById('id_Deskripsi')
const url_event = document.getElementById('id_url')
const card_image = document.getElementById('id_Card_Image')
const page_image = document.getElementById('id_Page_Image')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const url = ""

const handleAlerts = (type, text) =>{
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                        ${text}
                        </div>`
}


form.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('Nama', nama.value)
    fd.append('Tanggal', tanggal.value)
    fd.append('Waktu', waktu.value)
    fd.append('Media', media.value)
    fd.append('Tipe', tipe.value)
    fd.append('url', url_event.value)
    fd.append('Deskripsi', deskripsi.value)
    fd.append('Card_Image', card_image.files[0])
    fd.append('Page_Image', page_image.files[0])

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response){
            console.log(response)
            const sText = `successfully saved`
            handleAlerts('success', sText)
            setTimeout(()=>{
                alertBox.innerHTML = ""
                imgBox.innerHTML = ""
                nama.value = ""
                tanggal.value = ""
                waktu.value = ""
                media.value = ""
                tipe.value = ""
                url_event.value = ""
                deskripsi.value = ""
                card_image.value = ""
                page_image.value = ""
            }, 3000)
        },
        error: function(error){
            console.log(error)
            handleAlerts('danger', 'ups..something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})
