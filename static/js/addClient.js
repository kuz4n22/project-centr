document.getElementById('submitButton').addEventListener('click', function(event) {
    event.preventDefault();
    
    const form = document.getElementById('form-send');
    const formData = new FormData(form);
    
    let phoneNumber = formData.get('phone_number'); 
    phoneNumber = phoneNumber.replace(/[\s()-]/g, '');
    formData.set('phone_number', phoneNumber);
    
    fetch(form.action, {
        method: form.method,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', 
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.json(); 
        } else {
            return response.json().then(errorData => {
                throw new Error(errorData.error || 'Произошла ошибка при отправке запроса');
            });
        }
    })
    .then(data => {
        alert("Пользователь успешно создан");
        window.location.href = '/manager/'; 
    })
    .catch(error => {
        alert('Ошибка: ' + error.message);
    });
});