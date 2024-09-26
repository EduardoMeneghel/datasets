document.getElementById('houseForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Coletando os dados do formulário
    const data = {
        bedrooms: document.getElementById('bedrooms').value,
        bathrooms: document.getElementById('bathrooms').value,
        sqft_living: document.getElementById('sqft_living').value,
        sqft_lot: document.getElementById('sqft_lot').value,
        floors: document.getElementById('floors').value,
        waterfront: document.getElementById('waterfront').value,
        view: document.getElementById('view').value,
        condition: document.getElementById('condition').value,
        sqft_above: document.getElementById('sqft_above').value,
        sqft_basement: document.getElementById('sqft_basement').value,
        yr_built: document.getElementById('yr_built').value,
        yr_renovated: document.getElementById('yr_renovated').value
    };

    // Enviando os dados ao servidor Flask
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        // Exibindo o valor previsto da casa
        document.getElementById('housePrice').textContent = `O valor previsto da casa é: R$${result.price}`;
        document.getElementById('formSection').style.display = 'none';
        document.getElementById('resultSection').style.display = 'block';
    })
    .catch(error => {
        console.error('Erro:', error);
        document.getElementById('housePrice').textContent = 'Erro ao calcular o valor da casa.';
    });
});

// Função para reiniciar o formulário
function resetForm() {
    document.getElementById('formSection').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('houseForm').reset();
}
