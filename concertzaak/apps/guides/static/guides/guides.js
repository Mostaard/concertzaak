window.addEventListener('load', (event) => {
    document.querySelectorAll('.guide__title').forEach(title => {
        title.addEventListener('click', event => {
            event.target.closest('.guide').classList.toggle('open');
        })
    })

})
