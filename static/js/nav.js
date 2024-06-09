document.addEventListener('DOMContentLoaded', () => {
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

});