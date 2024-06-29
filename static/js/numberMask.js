const telInput = document.getElementById('customer-tel');
const maskOptions = {
  mask: '+{7} (000) 000-00-00'
};
const mask = IMask(telInput, maskOptions);

const telInputMobile = document.getElementById('customer-tel-mobile');
const maskOptionsMobile = {
  mask: '+{7} (000) 000-00-00'
};
const maskMobile = IMask(telInputMobile, maskOptionsMobile);