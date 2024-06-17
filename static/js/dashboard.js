// change view
document.addEventListener('DOMContentLoaded', () => {
  const addClient = document.getElementById('add-client');
  const activeClients = document.getElementById('active-clients');
  const finishedClients = document.getElementById('finished-clients');
  const activeContainer = document.getElementById('active-container');
  const finishedContainer = document.getElementById('finished-container');
  const addContainer = document.getElementById('add-container');

  addClient.addEventListener('click', () => {
    addClient.style.background = '#222220';
    activeClients.style.background = '#FFF';
    finishedClients.style.background = '#FFF';
    addClient.style.color = '#FFF';
    activeClients.style.color = '#222220';
    finishedClients.style.color = '#222220';
    activeContainer.style.display = 'none';
    finishedContainer.style.display = 'none';
    addContainer.style.display = 'block';
  });
  activeClients.addEventListener('click', () => {
    addClient.style.background = '#FFF';
    activeClients.style.background = '#222220';
    finishedClients.style.background = '#FFF';
    addClient.style.color = '#222220';
    activeClients.style.color = '#FFF';
    finishedClients.style.color = '#222220';
    activeContainer.style.display = 'block';
    finishedContainer.style.display = 'none';
    addContainer.style.display = 'none';
  });
  finishedClients.addEventListener('click', () => {
    addClient.style.background = '#FFF';
    activeClients.style.background = '#FFF';
    finishedClients.style.background = '#222220';
    addClient.style.color = '#222220';
    activeClients.style.color = '#222220';
    finishedClients.style.color = '#FFF';
    activeContainer.style.display = 'none';
    finishedContainer.style.display = 'block';
    addContainer.style.display = 'none';
  });
});

// send 
