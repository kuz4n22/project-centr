document.getElementById('customCheckbox').addEventListener('change', function() {
  const submitButton = document.getElementById('submitButton');
  submitButton.disabled = !this.checked;
});

document.getElementById('customCheckboxMobile').addEventListener('change', function() {
  const submitButtonMobile = document.getElementById('submitButtonMobile');
  submitButtonMobile.disabled = !this.checked;
});
