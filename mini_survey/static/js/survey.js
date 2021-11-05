const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (survey) => {
  $.ajax({
    type: 'POST',
    url: 'search/',
    data: {
      'csrfmiddlewaretoken': csrf,
      'survey': survey,
    },
    success: (res) => {
      console.log(res.data)
      const data = res.data
      if (Array.isArray(data)) {
        resultsBox.innerHTML = ""
        data.forEach(survey => {
          resultsBox.innerHTML += `
            <a href="${url}${survey.id}" class="item">
              <div class="row mt-2 mb-2">
                <div class="col-2">
                  <h5>${survey.title}</h5>
                  <p class="text-muted">${survey.creator}</p>
                </div>
              </div>
            </a>
          `
        })
      } else {
        if (searchInput.value.length > 0) {
          resultsBox.innerHTML = `<b>${data}</b>`
        } else {
          resultsBox.classList.add('not-visible')
        }
      }
    },
    error: (err) => {
      console.log(err)
    }
  })
}

searchInput.addEventListener('keyup', e=> {

  if (resultsBox.classList.contains('not-visible')) {
    resultsBox.classList.remove('not-visible')
  }

  sendSearchData(e.target.value)
})