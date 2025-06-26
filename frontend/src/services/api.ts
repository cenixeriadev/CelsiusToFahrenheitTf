import axios from 'axios';

// Set the base URL for the API
const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:5000';

// Create an axios instance with default config
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Define interfaces for the API requests and responses
export interface ConversionRequest {
  celsius: number;
}

export interface ConversionResponse {
  celsius: number;
  fahrenheit: number;
  success: boolean;
}

export interface ErrorResponse {
  error: string;
}

// API functions
export const temperatureService = {
  // Convert Celsius to Fahrenheit
  convertCelsiusToFahrenheit: async (celsius: number): Promise<ConversionResponse> => {
    try {
      const response = await api.post<ConversionResponse>('/api/predict', { celsius });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        throw error.response.data as ErrorResponse;
      }
      throw { error: 'Error de conexión con el servidor' };
    }
  }
};

export default api;
