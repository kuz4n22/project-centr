

document.addEventListener('DOMContentLoaded', () => {

  // nav dropdown menu
  const servicesButton = document.getElementById('services-button');
  const servicesDropdown = document.getElementById('services-dropdown');
  const overlay = document.getElementById('overlay');
  const closeServices = document.getElementById('close-services');
  const nav = document.querySelector('nav');

  servicesButton.addEventListener('click', (e) => {
    e.preventDefault();
    setTimeout(() => {
      servicesDropdown.style.display = 'flex';
  }, 200);
    overlay.style.display = 'block';
    nav.style.height = '268px';
  });

  closeServices.addEventListener('click', () => {
    servicesDropdown.style.display = 'none';
    overlay.style.display = 'none';
    nav.style.height = '60px';
  });

  overlay.addEventListener('click', () => {
    closeServices.click();
  });

  // burger menu
  const burger = document.getElementById('burger-container');
  const openBurger = document.getElementById('burger-open-btn');
  const closeBurger =  document.getElementById('burger-close-btn');
  const burgerMainMenu =  document.getElementById('burger-nav-list');
  const burgerServices =  document.getElementById('burger-services-list');
  const openBurgerServices =  document.getElementById('burger-services-button');

  openBurger.addEventListener('click', () => {
    burger.style.display = 'flex';
    burgerMainMenu.style.display = 'flex';
    document.body.classList.add('no-scroll');
  });

  closeBurger.addEventListener('click', () => {
    burger.style.display = 'none';
    burgerServices.style.display = 'none';
    document.body.classList.remove('no-scroll');
  });

  openBurgerServices.addEventListener('click', () => {
    burgerServices.style.display = 'flex';
    burgerMainMenu.style.display = 'none';
  });

});