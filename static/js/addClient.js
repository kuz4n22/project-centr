document.getElementById('submitButton').addEventListener('click', function() {
  const form = document.getElementById('form-send');
  const formData = new FormData(form);

  let phoneNumber = formData.get('phone_number'); 
  console.log(phoneNumber);
  phoneNumber = phoneNumber.replace(/[\s()-]/g, '');
  console.log(phoneNumber);
  formData.set('phone_number', phoneNumber);

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
      alert("Успешно");
  })
  .catch(error => {
      alert('Ошибка: ' + error.message);
  });
});