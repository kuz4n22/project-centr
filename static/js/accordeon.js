document.querySelectorAll('.question').forEach((el) => {
  el.addEventListener('click', () => {
    let content = el.nextElementSibling;
    let img = el.querySelector('img');

    if(content.style.maxHeight) {
      content.style.maxHeight = null;
      content.style.marginTop = null;
    } else {
      content.style.maxHeight = content.scrollHeight + 'px';
      content.style.marginTop = '20px';
    }

    if (img.style.transform === 'rotate(180deg)') {
      img.style.transform = 'rotate(0deg)';
    } else {
      img.style.transform = 'rotate(180deg)';
    }
        
  })
})
