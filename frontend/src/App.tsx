import { useState} from 'react'
import type {FormEvent} from 'react';
import type{ temperatureService, ConversionResponse, ErrorResponse } from './services/api';

function App() {
  const [celsius, setCelsius] = useState<string>('');
  const [result, setResult] = useState<ConversionResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(null);
    setResult(null);
    setLoading(true);

    try {
      // Convert string to number
      const celsiusValue = parseFloat(celsius);
      
      // Validate input
      if (isNaN(celsiusValue)) {
        throw { error: "Por favor ingresa un número válido para la temperatura" };
      }

      // Call API
      const response = await temperatureService.convertCelsiusToFahrenheit(celsiusValue);
      setResult(response);
    } catch (err) {
      // Handle errors
      const errorResponse = err as ErrorResponse;
      setError(errorResponse.error || 'Error desconocido');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>🌡️ Convertidor de Temperatura</h1>
        <p>Celsius a Fahrenheit usando DeepLearning</p>
      </div>

      {error && (
        <div className="alert alert-error">
          <strong>❌ Error:</strong> {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className={loading ? 'loading' : ''}>
        <div className="form-group">
          <label className="form-label" htmlFor="celsius">
            🌡️ Temperatura en Celsius (°C):
          </label>
          <input
            type="number"
            step="0.01"
            className="form-input"
            id="celsius"
            placeholder="Ejemplo: 25.5"
            value={celsius}
            onChange={(e) => setCelsius(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="btn" disabled={loading}>
          {loading ? '⏳ Convirtiendo...' : '🔥 Convertir a Fahrenheit'}
        </button>
      </form>

      {result && (
        <div className="result">
          <h3>✅ Resultado de la Conversión</h3>
          
          <div className="result-display">
            <div className="temp-input">
              <div className="temp-value">{result.celsius}°</div>
              <div className="temp-label">Celsius</div>
            </div>
            
            <div className="arrow">➡️</div>
            
            <div className="temp-output">
              <div className="temp-value">{result.fahrenheit}°</div>
              <div className="temp-label">Fahrenheit</div>
            </div>
          </div>

          <div className="model-info">
            <small>🤖 Predicción realizada por modelo de TensorFlow</small>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
