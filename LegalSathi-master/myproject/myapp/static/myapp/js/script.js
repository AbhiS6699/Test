document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.getElementById('menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const modal = document.getElementById('modal');
    const requestServiceButton = document.getElementById('request-service-button');
    const closeModalButton = document.getElementById('close-modal');

    menuButton.addEventListener('click', function () {
        mobileMenu.classList.toggle('hidden');
    });

    requestServiceButton.addEventListener('click', function () {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    });

    closeModalButton.addEventListener('click', function () {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    });

    document.getElementById('request-form').addEventListener('submit', function (event) {
        event.preventDefault();
        // Add form submission logic here
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        alert('Service request submitted!');
    });
});
