document.getElementById('new-pass-btn').addEventListener('click', function() {
    const form = document.getElementById('new-pass-form');
    const formData = new FormData(form);
  
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
            alert('Произошла ошибка: ' + data.error);
        } else {
            alert('Произошла неизвестная ошибка');
        }
    })
    .catch(function(error) {
        alert('Произошла ошибка при выполнении запроса: ' + error.message);
    });
  });