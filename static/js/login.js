// login 
document.getElementById('login-btn').addEventListener('click', function() {
  const form = document.getElementById('login-form');
  const formData = new FormData(form);

  let phoneNumber = formData.get('phone'); 
  phoneNumber = phoneNumber.replace(/[\s()-]/g, '');
  formData.set('phone', phoneNumber);

  fetch(form.action, {
      method: 'POST',
      headers: {
          'X-Requested-With': 'XMLHttpRequest', 
          'X-CSRFToken': '{{ csrf_token }}' 
      },
      body: formData
  })
  .then(function(response) {
      return response.json(); 
  })
  .then(function(data) {
      if (data.redirect_url) {
          window.location.href = data.redirect_url; 
      } else if (data.error) {
          if (data.error === "Необходимо указать телефон и пароль" || data.error === "Неверные данные") {
              alert(data.error);
          } else {
              alert('Произошла ошибка: ' + data.error);
          }
      } else {
          alert('Произошла неизвестная ошибка');
      }
  })
  .catch(function(error) {
      alert('Произошла ошибка при выполнении запроса: ' + error.message);
  });
});
