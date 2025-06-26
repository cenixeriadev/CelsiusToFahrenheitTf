from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure CORS
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5173')


CORS(app, origins=[FRONTEND_URL] ,allow_headers=['Content-Type'], methods=['GET', 'POST'])

def load_tflite_model():
    model_path = os.path.join("models", "celsius_to_fahrenheit_model.tflite")
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter


def predict_temperature(interpreter, celsius_value):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Crear entrada en el formato correcto
    input_data = np.array([[celsius_value]], dtype=np.float32)

    # Ejecutar la inferencia
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Obtener resultado
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return float(output_data[0][0])

# Carga global del modelo
print("Cargando modelo TFLite...")
tflite_interpreter = load_tflite_model()



if tflite_interpreter is None:
    print("Error: No se pudo cargar el interprete del modelo TFLite.")


@app.route('/api/predict', methods=['POST'])
def predict():
    global tflite_interpreter
    try:
        celsius = float(request.json.get('celsius', 0))

        if tflite_interpreter is None:
            raise Exception("Modelo TFLite no disponible")

        fahrenheit = predict_temperature(tflite_interpreter, celsius)

        return jsonify({
            'celsius': celsius,
            'fahrenheit': round(fahrenheit, 2),
            'success': True
        })

    except ValueError:
        return jsonify({'error': "Por favor ingresa un número válido para la temperatura"}), 400
    except Exception as e:
        return jsonify({'error': f"Error en la predicción: {str(e)}"}), 500

if __name__ == '__main__':
    debug_mode = FLASK_ENV == 'development'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
