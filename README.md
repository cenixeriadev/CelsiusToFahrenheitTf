# 🌡️ Conversor Celsius-Fahrenheit con TensorFlow

Proyecto de DeepLearning que convierte temperaturas usando un modelo neuronal entrenado con datos de Hugging Face. Ahora con frontend React + TypeScript y una API REST con Flask.

Proyecto de DeepLearning que convierte temperaturas usando un modelo neuronal entrenado con datos de Hugging Face.
![image](https://github.com/user-attachments/assets/d5483deb-eafd-4fa7-aacb-ac0774765a27)

![image](https://github.com/user-attachments/assets/8c21ec4a-8ed2-4ba0-ab99-d4f3f83307ad)



## 🔗 Dataset Original
Dataset usado: [prabinpanta0/celsius-to-fahrenheit](https://huggingface.co/datasets/prabinpanta0/celsius-to-fahrenheit) en Hugging Face

## 🛠️ Configuración Requerida
- **Python**: 3.9-3.12 (No compatible con 3.13+)
- **Node.js**: 14+ y npm
- **Jupyter Notebooks**: Si es posible armar el setup en VisualStudioCode debido a que alli lo desarrolle.

## 🏹 Como correr el proyecto
- **Instalacion de paquetes**:
  - Primero clonamos el repositorio:
    ```bash
    git clone https://github.com/cenixeriadev/CelsiusToFahrenheitTf.git
    cd CelsiusToFahrenheitTf
    ``` 
  - Segundo levantamos un entorno virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\Activate.ps1    # Windows
    ```
  - Instalamos los Paquetes necesarios para la aplicación:
    ```bash
    pip install -r requirements.txt
    ```
- **Ejecucion de la aplicación**
  - Corremos el backend con flask:
    ```bash
    flask --app app run
    ```
  - En otra terminal, instalamos y ejecutamos el frontend:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
  - Abrimos nuestro navegador y accedemos a:
    ```txt
    http://localhost:5173/
    ```
Listo! tienes para probar el modelo con una interfaz de usuario amigable desarrollada con React + TypeScript, que consume la API REST de Flask.

## 📄Licencia
Este proyecto está licenciado bajo la licencia MIT: consulte el archivo [LICENSE](LICENSE) para obtener más detalles.


## 👀Contacto
Si tiene alguna pregunta o necesita más ayuda, no dude en ponerse en contacto conmigo en [codeartprogrammer@gmail.com].
  
