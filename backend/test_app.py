import pytest
import json
from .app import app  # Importação relativa

# Configurar o pytest para testar o Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_house_price_scenario_1(client):
    # Cenário 1: Previsão com entrada de dados de uma casa comum
    data = {
        "bedrooms": 3,
        "bathrooms": 2,
        "sqft_living": 2000,
        "sqft_lot": 5000,
        "floors": 1,
        "waterfront": 0,
        "view": 0,
        "condition": 3,
        "sqft_above": 1500,
        "sqft_basement": 500,
        "yr_built": 1990,
        "yr_renovated": 0
    }

    # Valor esperado (modifique para corresponder ao valor que seu modelo retorna para essa entrada)
    expected_price = 439697.61

    # Enviar uma requisição POST com dados simulados
    response = client.post('/predict', data=json.dumps(data), content_type='application/json')
    
    # Verificar se a resposta foi 200 OK
    assert response.status_code == 200
    
    # Verificar se a resposta tem um campo 'price'
    json_data = response.get_json()
    assert 'price' in json_data
    assert isinstance(json_data['price'], float)
    
    # Verificar se o preço previsto está dentro de uma tolerância aceitável
    assert pytest.approx(json_data['price'], 0.01) == expected_price

def test_predict_house_price_scenario_2(client):
    # Cenário 2: Previsão de uma casa de luxo à beira-mar
    data = {
        "bedrooms": 5,
        "bathrooms": 4,
        "sqft_living": 5000,
        "sqft_lot": 10000,
        "floors": 2,
        "waterfront": 1,
        "view": 1,
        "condition": 5,
        "sqft_above": 4000,
        "sqft_basement": 1000,
        "yr_built": 2015,
        "yr_renovated": 0
    }

    # Valor esperado para essa casa de luxo
    expected_price = 1787732.7

    # Enviar uma requisição POST com dados simulados
    response = client.post('/predict', data=json.dumps(data), content_type='application/json')
    
    # Verificar se a resposta foi 200 OK
    assert response.status_code == 200
    
    # Verificar se a resposta tem um campo 'price'
    json_data = response.get_json()
    assert 'price' in json_data
    assert isinstance(json_data['price'], float)
    
    # Verificar se o preço previsto está dentro de uma tolerância aceitável
    assert pytest.approx(json_data['price'], 0.01) == expected_price

def test_predict_house_price_scenario_3(client):
    # Cenário 3: Previsão de uma casa antiga com pouca metragem
    data = {
        "bedrooms": 2,
        "bathrooms": 1,
        "sqft_living": 800,
        "sqft_lot": 1000,
        "floors": 1,
        "waterfront": 0,
        "view": 0,
        "condition": 2,
        "sqft_above": 800,
        "sqft_basement": 0,
        "yr_built": 1940,
        "yr_renovated": 0
    }

    # Valor esperado para essa casa antiga e pequena
    expected_price = 224912.45

    # Enviar uma requisição POST com dados simulados
    response = client.post('/predict', data=json.dumps(data), content_type='application/json')
    
    # Verificar se a resposta foi 200 OK
    assert response.status_code == 200
    
    # Verificar se a resposta tem um campo 'price'
    json_data = response.get_json()
    assert 'price' in json_data
    assert isinstance(json_data['price'], float)
    
    # Verificar se o preço previsto está dentro de uma tolerância aceitável
    assert pytest.approx(json_data['price'], 0.01) == expected_price

def test_predict_house_price_invalid_data(client):
    # Cenário 4: Previsão com dados inválidos
    data = {
        "bedrooms": "three",  # Dados inválidos (string em vez de int)
        "bathrooms": -1,      # Dados inválidos (número negativo)
        "sqft_living": "NaN"  # Dados inválidos (string não numérica)
    }

    # Enviar uma requisição POST com dados inválidos
    response = client.post('/predict', data=json.dumps(data), content_type='application/json')
    
    # Verificar se a resposta foi 500 Internal Server Error (ou outro código de erro adequado)
    assert response.status_code == 500
    
    # Verificar se a resposta tem uma mensagem de erro apropriada
    json_data = response.get_json()
    assert 'error' in json_data
