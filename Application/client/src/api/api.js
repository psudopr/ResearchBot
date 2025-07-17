import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // The address of the backend API
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add a request interceptor to include the auth token in requests
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth
export const login = (credentials) => {
  return apiClient.post('/auth/login', credentials);
};

export const logout = () => {
  // You might want to call a backend endpoint to invalidate the token
  localStorage.removeItem('token');
};

// User
export const getUser = () => {
  return apiClient.get('/users/me');
};

export const updateUser = (userData) => {
  return apiClient.put('/users/me', userData);
};

export const changePassword = (passwordData) => {
  return apiClient.put('/users/me/password', passwordData);
};

// Companies
export const getCompanies = () => {
  return apiClient.get('/companies');
};

export const getCompany = (companyId) => {
  return apiClient.get(`/companies/${companyId}`);
};

// Articles
export const getArticles = (companyId) => {
  return apiClient.get(`/articles?company_id=${companyId}`);
};

export const markArticleAsRead = (articleId) => {
  return apiClient.put(`/articles/${articleId}/read`);
};
