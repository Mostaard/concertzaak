window.addEventListener('load', (event) => {
    document.querySelector('nav .hamburger')
        .addEventListener('click', event => toggleMenu(event.target));
})

function toggleMenu(button) {
    button = button.closest('button');
    const nav = button.closest('nav');
    nav.classList.toggle('opened');
    button.setAttribute('aria-expanded', nav.classList.contains('opened'));
}
