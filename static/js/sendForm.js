document.getElementById('form-send').addEventListener('submit', function(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  fetch(form.action, {
      method: form.method,
      headers: {
        'X-Requested-With': 'XMLHttpRequest', 
        'X-CSRFToken': '{{ csrf_token }}'
      },
      body: formData
  })
  .then(response => {
      if (response.status === 200) {
          window.location.href = '/form-sent/';
      } else {
          alert('Ошибка при отправке формы');
      }
  })
  .catch(error => {
      alert('Ошибка при отправке формы');
      console.error('Error:', error);
  });
});