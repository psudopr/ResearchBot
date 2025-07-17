import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import CompanyPage from './pages/CompanyPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import PrivateRoute from './components/PrivateRoute'; // You will create this component
import { AuthProvider } from './context/AuthContext'; // You will create this context

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/" element={<PrivateRoute><HomePage /></PrivateRoute>} />
          <Route path="/company/:companyId" element={<PrivateRoute><CompanyPage /></PrivateRoute>} />
          <Route path="/profile" element={<PrivateRoute><UserPage /></PrivateRoute>} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;