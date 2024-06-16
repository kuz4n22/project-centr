document.getElementById('request-pass-btn').addEventListener('click', function() {
  // Получаем форму и данные из неё
  const form = document.getElementById('request-pass-form');
  const formData = new FormData(form);

  // Отправляем AJAX-запрос на сервер
  fetch(form.action, {
      method: 'POST',
      headers: {
          'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
          'X-Requested-With': 'XMLHttpRequest'
      },
      body: formData
  })
  .then(response => {
      if (response.ok) {
          return response.json(); 
      } else {
          return response.json().then(errorData => {
              throw new Error(errorData.error || 'Произошла ошибка при отправке запроса');
          });
      }
  })
  .then(data => {
      alert("Успешно");
  })
  .catch(error => {
      // Обрабатываем ошибки
      alert('Ошибка: ' + error.message);
  });
});