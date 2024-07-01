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

          } else {
              console.log("dropdown big");
          }
      });
  });
});