document.addEventListener("DOMContentLoaded", () => {
  const textInput = document.getElementById('customer-name');
  const emailInput = document.getElementById('customer-email');
  const telInput = document.getElementById('customer-tel');
  const textMessage = document.getElementById('textMessage');
  const emailMessage = document.getElementById('emailMessage');
  const telMessage = document.getElementById('telMessage');

  // mask
  const maskOptions = {
    mask: '+{7} (000) 000-00-00'
  };
  const mask = IMask(telInput, maskOptions);


  textInput.addEventListener('input', () => validateInput(textInput, textMessage));
  emailInput.addEventListener('input', () => validateInput(emailInput, emailMessage));
  telInput.addEventListener('input', () => validateInput(telInput, telMessage));
});

function validateInput(input, messageElement) {
  if (valid(input)) {
      input.classList.remove('invalid');
      input.classList.add('valid');
      messageElement.style.display = 'none';
      messageElement.style.color = 'green';
  } else {
      input.classList.remove('valid');
      input.classList.add('invalid');
      messageElement.style.display = 'block';
      messageElement.style.color = 'red';
  }
}

function valid(input) {
  const value = input.value.trim();
  const type = input.type;

  if (type === 'text') {
      return value !== '';
  } else if (type === 'email') {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  } else if (type === 'tel') {
      // Remove all non-digit characters before validation
      const numericValue = value.replace(/\D/g, '');
      // Check if the numeric value has between 10 and 12 digits
      return /^\d{11,11}$/.test(numericValue);
  }

  return false;
}