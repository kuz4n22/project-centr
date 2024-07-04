document.getElementById('customCheckbox').addEventListener('change', function() {
  const submitButton = document.getElementById('submitButton');
  submitButton.disabled = !this.checked;
});