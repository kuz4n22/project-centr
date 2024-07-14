document.addEventListener("DOMContentLoaded", () => {
  const textInput = document.getElementById('customer-name');
  const telInput = document.getElementById('customer-tel');
  const checkboxInput = document.getElementById('customCheckbox');

  let nameFill = false;
  let telFill = false;
  let checkboxFill = false;

  
  textInput.addEventListener('input', () => validateInput(textInput));
  telInput.addEventListener('input', () => validateInput(telInput));
  checkboxInput.addEventListener('input', () => validateInput(checkboxInput));

  textInput.addEventListener('input', () => activateBtn());
  telInput.addEventListener('input', () => activateBtn());
  checkboxInput.addEventListener('input', () => activateBtn());

  const submitButton = document.getElementById('submitButton');
  function activateBtn() {
    if (nameFill === true && telFill === true && checkboxFill === true) {
      submitButton.disabled = false;
    } else {
      submitButton.disabled = true;
    }
  }



  function validateInput(input) {
    if (valid(input) === 'empty') {
      input.style.borderBottom= '1px solid #FF0F00';
      if (input.type === 'text') {
        nameFill = false;
      }
      if (input.type === 'tel') {
        telFill = false;
      }
    } else if (valid(input)) {
      input.style.borderBottom= '1px solid #1DBC19';
      if (input.type === 'text') {
        nameFill = true;
      }
      if (input.type === 'tel') {
        telFill = true;
      }
      if (input.type === 'checkbox') {
        checkboxFill = true;
      }
    } else {
      input.style.borderBottom= '1px solid #FF0F00';
      if (input.type === 'text') {
        nameFill = false;
      }
      if (input.type === 'tel') {
        telFill = false;
      }
      if (input.type === 'checkbox') {
        checkboxFill = false;
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
