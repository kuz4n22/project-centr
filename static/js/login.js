document.getElementById('login-btn').addEventListener('click', function() {
  var form = document.getElementById('login-form');
  var formData = new FormData(form);

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