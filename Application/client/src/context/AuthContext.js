import React, { createContext, useContext, useState, useEffect } from 'react';
import { login as apiLogin, logout as apiLogout, getUser } from '../api/api';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      getUser()
        .then(response => {
          setUser(response.data);
        })
        .catch(() => {
          // Token is invalid or expired
          localStorage.removeItem('token');
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (credentials) => {
    const response = await apiLogin(credentials);
    localStorage.setItem('token', response.data.access_token);
    const userResponse = await getUser();
    setUser(userResponse.data);
  };

  const logout = () => {
    apiLogout();
    setUser(null);
  };

  const authContextValue = { user, login, logout, isAuthenticated: !!user };

  return (
    <AuthContext.Provider value={authContextValue}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};