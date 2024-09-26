from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import numpy as np
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Carregar o modelo treinado
modelo = joblib.load('melhor_modelo_regressao_linear.joblib')

def validate_inputs(data):
    """Valida e extrai os dados de entrada."""
    try:
        # Extrair e converter valores de entrada
        bedrooms = int(data.get('bedrooms', 0))
        bathrooms = float(data.get('bathrooms', 0))
        sqft_living = float(data.get('sqft_living', 0))
        sqft_lot = float(data.get('sqft_lot', 0))
        floors = float(data.get('floors', 0))
        waterfront = int(data.get('waterfront', 0))
        view = int(data.get('view', 0))
        condition = int(data.get('condition', 0))
        sqft_above = float(data.get('sqft_above', 0))
        sqft_basement = float(data.get('sqft_basement', 0))
        yr_built = int(data.get('yr_built', 0))
        yr_renovated = int(data.get('yr_renovated', 0))
        
        # Validar os valores
        if bedrooms < 0 or bathrooms < 0 or sqft_living < 0 or sqft_lot < 0 or floors < 0:
            raise ValueError("Os valores de entrada devem ser não negativos.")

        return [bedrooms, bathrooms, sqft_living, sqft_lot, floors, 
                waterfront, view, condition, sqft_above, sqft_basement, 
                yr_built, yr_renovated]
    
    except (ValueError, TypeError) as ve:
        raise ValueError(f"Dados de entrada inválidos: {ve}")

@app.route('/predict', methods=['POST'])
def predict_house_price():
    """Prever o preço da casa com base nas características fornecidas."""
    try:
        # Receber os dados do front-end (JSON)
        data = request.get_json()

        # Validar e extrair as características
        features = validate_inputs(data)

        # Criar um array para o modelo com as características mencionadas
        features_array = np.array([features])

        # Fazer a predição
        predicted_price = modelo.predict(features_array)

        # Converter o resultado para um tipo serializável em JSON
        predicted_price = float(predicted_price[0])

        # Retornar o valor previsto
        return jsonify({"price": round(predicted_price, 2)}), 200
    except Exception as e:
        logging.error(f"Erro: {e}")
        return jsonify({"error": "Erro ao realizar a predição"}), 500

if __name__ == '__main__':
    app.run(debug=True)