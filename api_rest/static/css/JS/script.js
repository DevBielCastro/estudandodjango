fetch('http://localhost:8000/api/myendpoint/')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Exibir dados no front-end
    })
    .catch(error => console.error('Erro:', error));
