document.getElementById('request-pass-btn').addEventListener('click', function() {
  const form = document.getElementById('request-pass-form');
  const formData = new FormData(form);

  fetch(form.action, {
      method: 'POST',
      headers: {
          'X-CSRFToken': '{{ csrf_token }}', 
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
      alert("Сообщение отправлено. Проверьте ваш email.");
  })
  .catch(error => {
      alert('Ошибка: ' + error.message);
  });
});