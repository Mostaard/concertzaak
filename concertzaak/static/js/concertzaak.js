window.addEventListener('load', (event) => {
    document.querySelector('nav .hamburger')
        .addEventListener('click', event => toggleMenu(event.target));
    const dropdown = document.querySelector('nav .dropdown-toggle')
    if (dropdown) {
        dropdown.addEventListener('click', event => toggleDropdown(event))
    }
    document.addEventListener('click', () =>
        document.querySelectorAll('.dropdown-menu.open')
            .forEach(dropdown => dropdown.classList.remove('open')));

})

function toggleMenu(button) {
    button = button.closest('button');
    const nav = button.closest('nav');
    nav.classList.toggle('opened');
    button.setAttribute('aria-expanded', nav.classList.contains('opened'));
}

function toggleDropdown(event) {
    event.preventDefault();
    setTimeout(() => {
        event.target.closest('.dropdown').querySelector('.dropdown-menu').classList.toggle('open');
    }, 0)

}