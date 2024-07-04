document.addEventListener("DOMContentLoaded", () => {
  const textInput = document.getElementById('customer-name');
  const emailInput = document.getElementById('customer-email');
  const telInput = document.getElementById('customer-tel');
  const checkboxInput = document.getElementById('customCheckbox');
  const nameMessage = document.getElementById('name-response-text');
  const telMessage = document.getElementById('tel-response-text');
  const emailMessage = document.getElementById('email-response-text');
  const checkboxMessage = document.getElementById('checkbox-response-text');

  textInput.addEventListener('input', () => validateInput(textInput, nameMessage));
  emailInput.addEventListener('input', () => validateInput(emailInput, emailMessage));
  telInput.addEventListener('input', () => validateInput(telInput, telMessage));
  checkboxInput.addEventListener('input', () => validateInput(checkboxInput, checkboxMessage));

  function validateInput(input, messageElement) {
    if (valid(input) === 'empty') {
      input.style.border= '1px solid #FF0F00';
      if (input.type === 'text') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Обязательное поле";
      }
      if (input.type === 'tel') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Обязательное поле";
      }
      if (input.type === 'email') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Обязательное поле";
      }
    } else if (valid(input)) {
      input.style.border= '1px solid #1DBC19';
      if (input.type === 'text') {
        messageElement.style.display = "none";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "";
      }
      if (input.type === 'tel') {
        messageElement.style.display = "none";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "";
      }
      if (input.type === 'email') {
        messageElement.style.display = "none";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "";
      }
      if (input.type === 'checkbox') {
        messageElement.style.display = "none";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "";
      }
    } else {
      input.style.border= '1px solid #FF0F00';
      if (input.type === 'text') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Обязательное поле";
      }
      if (input.type === 'tel') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Некорректный номер телефона";
      }
      if (input.type === 'email') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Некорректный Email";
      }
      if (input.type === 'checkbox') {
        messageElement.style.display = "flex";
        const messageContent = messageElement.querySelector('p');
        messageContent.textContent = "Необходимо дать своё согласие";
      }
    }
  }

  function valid(input) {
    const value = input.value.trim();
    const type = input.type;
    if (value === '' ) {
      return "empty";
    } else if (type === 'text') {
      return value !== '';
    } else if (type === 'checkbox') {
      return input.checked;
    } else if (type === 'email') {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    } else if (type === 'tel') {
      const numericValue = value.replace(/\D/g, '');
      return /^\d{11,11}$/.test(numericValue);
    }
    return false;
  }

});