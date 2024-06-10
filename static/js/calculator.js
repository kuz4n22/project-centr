// area animation
const rangeSlider = document.getElementById('rangeSlider');
const rangeValue = document.getElementById('rangeValue');

rangeSlider.addEventListener('input', () => {
  const value = rangeSlider.value;
  rangeValue.textContent = `${value} м²`;

  const percentage = ((value - 40) / (200 - 40)) * 100;
  rangeSlider.style.background = `linear-gradient(to right, #FFF ${percentage}%, rgba(255, 255, 255, 0.4) ${percentage}%)`;
});
