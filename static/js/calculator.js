document.addEventListener('DOMContentLoaded', function () {
  const areaInput = document.getElementById('area');
  const areaValue = document.getElementById('area-value');
  const summaryArea = document.getElementById('summary-area');
  const costElement = document.getElementById('cost');
  let baseCost = 80000;

areaInput.addEventListener('input', function () {
  const area = areaInput.value;
  areaValue.textContent = area + ' м²';
  summaryArea.textContent = area + ' м²';
  updateCost();
});

});