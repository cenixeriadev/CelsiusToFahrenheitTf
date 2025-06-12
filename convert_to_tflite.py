import tensorflow as tf

model = tf.keras.models.load_model('models/celsius_to_fahrenheit_model.h5', compile=False)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open('models/celsius_to_fahrenheit_model.tflite', 'wb') as f:
    f.write(tflite_model)
