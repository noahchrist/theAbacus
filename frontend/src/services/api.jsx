import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchMarkets = async () => {
  const response = await api.get('/markets');
  return response.data;
};

export const calculateEdge = async (data) => {
  const response = await api.post('/calculate-edge', data);
  return response.data;
};

export default api;