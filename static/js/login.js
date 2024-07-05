document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById('login-btn');

  const telInput = document.getElementById('customer-tel');
  const passInput = document.getElementById('customer-password');
  const telLabel = document.getElementById('customer-tel-label');
  const passLabel = document.getElementById('customer-password-label');

  const loginError = document.getElementById('login-response-text');
  const passError = document.getElementById('pass-response-text');

  button.addEventListener('click', function() {

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
          if (data.error === "Необходимо указать телефон и пароль") {
            loginError.textContent = "Обязательное поле";
            passError.textContent = "Обязательное поле";
            telInput.style.borderColor = 'red';
            telLabel.style.color = 'red';
            passInput.style.borderColor = 'red';
            passLabel.style.color = 'red';
          } else if (data.error === "Неверные данные") {
            loginError.textContent = "Некорректный номер телефона";
            passError.textContent = "Некорректный пароль";
            telInput.style.borderColor = 'red';
            telLabel.style.color = 'red';
            passInput.style.borderColor = 'red';
            passLabel.style.color = 'red';
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

// validate

  telInput.addEventListener('input', () => validateInput(telInput, telLabel));
  passInput.addEventListener('input', () => validateInput(passInput, passLabel));

  function validateInput(input, messageElement) {
    if (valid(input)) {
      input.style.borderColor = 'green';
      messageElement.style.color = 'green';
      if (input.type === 'tel') {
        loginError.textContent = "";
      }
      if (input.type === 'password') {
        passError.textContent = "";
      }
    } else {
      input.style.borderColor = 'red';
      messageElement.style.color = 'red';
      if (input.type === 'tel') {
        loginError.textContent = "Некорректный номер телефона";
      }
      if (input.type === 'password') {
        passError.textContent = "Обязательное поле";
      }
    }
  }
  
  function valid(input) {
    const value = input.value.trim();
    const type = input.type;
  
    if (type === 'password') {
      return value !== '';
    } else if (type === 'email') {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    } else if (type === 'tel') {
      const numericValue = value.replace(/\D/g, '');
      return /^\d{11,11}$/.test(numericValue);
    }
    return false;
  }

});