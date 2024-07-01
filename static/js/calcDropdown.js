document.addEventListener('DOMContentLoaded', () => {
  const infoIcons = document.querySelectorAll('.checkbox-info');

  infoIcons.forEach(icon => {
      icon.addEventListener('click', () => {
          const screenWidth = window.innerWidth;
          if (screenWidth < 450) {
              const adviceContent = icon.closest('.checkbox-element').querySelector('.advice').innerHTML;

              let modal = document.querySelector('.modal');
              let overlay = document.querySelector('.modal-overlay');

              modal.innerHTML = adviceContent;
              modal.classList.add('show');
              overlay.classList.add('show');
              const closeBtns = document.querySelectorAll('.advice-close');

              closeBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                  modal.classList.remove('show');
                  overlay.classList.remove('show');
                });
              });

              overlay.addEventListener('click', () => {
                modal.classList.remove('show');
                overlay.classList.remove('show');
              });

          }
      });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const checkboxElements = document.querySelectorAll('.checkbox-element');
  checkboxElements.forEach(element => {
      const infoIcon = element.querySelector('.checkbox-info');
      const adviceContent = element.querySelector('.advice-content');
      
      const tooltip = document.createElement('div');
      tooltip.classList.add('tooltip');
      tooltip.textContent = adviceContent.textContent;
      element.appendChild(tooltip);

      infoIcon.addEventListener('mouseenter', function () {
          const screenWidth = window.innerWidth;
          if (screenWidth >= 450) {
            tooltip.style.display = 'block';
          }
      });

      infoIcon.addEventListener('mouseleave', function () {
          tooltip.style.display = 'none';
      });
  });
});