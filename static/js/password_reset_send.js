document.getElementById('new-pass-btn').addEventListener('click', function() {
  const form = document.getElementById('new-pass-form');
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
      alert("Пароль изменен");
  })
  .catch(error => {
      alert('Ошибка: ' + error.message);
  });
});