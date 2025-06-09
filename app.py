from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import os

app = Flask(__name__)
def load_model():
    
    model_path = os.path.join("models", "celsius_to_fahrenheit_model.keras")


    if os.path.exists(model_path):
        try:
            model = tf.keras.models.load_model(model_path)
            print(f"Modelo cargado exitosamente desde: {model_path}")
            return model
        except Exception as e:
            print(f"Error cargando el modelo: {e}")
            return None
    else:
        print("Modelo no encontrado!")
        return None

print("Cargando modelo de conversión de temperatura...")
temperature_model = load_model()
if temperature_model is None:
    print("Error: No se pudo cargar ni crear el modelo")


@app.route('/' , methods=['GET' , 'POST'])
def index():

    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    global temperature_model

    result = None
    error = None
    
    if request.method == 'POST':
        try:
            # Obtener los valores del formulario
            celsius = float(request.form.get('celsius', 0))
            
            if temperature_model is None:
                raise Exception("Modelo no disponible")
            
            # Hacer predicción con el modelo
            celsius_input = np.array([celsius], dtype=float)
            fahrenheit_prediction = temperature_model.predict(celsius_input, verbose=0)
            fahrenheit = float(fahrenheit_prediction[0][0])
            
            # Preparar resultado
            result = {
                'celsius': celsius,
                'fahrenheit': round(fahrenheit, 2),
                'success': True
            }
            
        except ValueError:
            error = "Por favor ingresa un número válido para la temperatura"
        except Exception as e:
            error = f"Error en la predicción: {str(e)}"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)