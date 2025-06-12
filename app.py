from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os

app = Flask(__name__)
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


@app.route('/' , methods=['GET' , 'POST'])
def index():

    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    global tflite_interpreter

    result = None
    error = None
    
    if request.method == 'POST':
        try:
            celsius = float(request.form.get('celsius', 0))

            if tflite_interpreter is None:
                raise Exception("Modelo TFLite no disponible")
            
            fahrenheit = predict_temperature(tflite_interpreter, celsius)

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
