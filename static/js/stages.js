document.addEventListener('DOMContentLoaded', function () {
    const finishBtns = document.getElementsByClassName('client-finish-btn');
    Array.from(finishBtns).forEach(btn => {
        btn.addEventListener('click', function () {

            const clientId = btn.dataset.clientId;
            const url = `/manager/complete_project/${clientId}/`;
            
            fetch(url, {
                method: 'GET', 
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', 
                    'X-CSRFToken': '{{ csrf_token }}' 
                },
            })
            .then(response => {
                return response.json();
            })
            .then(data => {
                console.log(data);  
                alert(data.message);  
            })
            .catch(error => {
                console.error('Error during fetch operation:', error);
                alert('Произошла ошибка при завершении проекта');
            });
        });
    });

    const notifiBtns = document.getElementsByClassName('client-notifi-btn');
    Array.from(notifiBtns).forEach(btn => {
        btn.addEventListener('click', function () {

            const clientId = btn.dataset.clientId;
            const url = `/manager/notify_next_phase/${clientId}/`;

            fetch(url, {
                method: 'GET', 
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', 
                    'X-CSRFToken': '{{ csrf_token }}' 
                },
            })
            .then(response => {
                return response.json();
            })
            .then(data => {
                console.log(data);  
                alert(data.message);  
            })
            .catch(error => {
                console.error('Error during fetch operation:', error);
                alert('Произошла ошибка при изменении этапа');
            });


        });
    });

    const newPassBtns = document.getElementsByClassName('client-new-pass-btn');
    Array.from(newPassBtns).forEach(btn => {
        btn.addEventListener('click', function () {

            const clientId = btn.dataset.clientId;
            const url = `/manager/send_new_password/${clientId}/`;

            fetch(url, {
                method: 'GET', 
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', 
                    'X-CSRFToken': '{{ csrf_token }}' 
                },
            })
            .then(response => {
                return response.json();
            })
            .then(data => {
                console.log(data);  
                alert(data.message);  
            })
            .catch(error => {
                console.error('Error during fetch operation:', error);
                alert('Произошла ошибка при смене пароля');
            });


        });
    });
});

