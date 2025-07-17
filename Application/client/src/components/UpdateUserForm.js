import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { updateUser } from '../api/api';

function UpdateUserForm() {
  const { user } = useAuth();
  const [fullName, setFullName] = useState(user.full_name || '');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateUser({ full_name: fullName });
      setMessage('Profile updated successfully!');
    } catch (error) {
      setMessage('Failed to update profile.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={fullName} 
        onChange={(e) => setFullName(e.target.value)} 
      />
      <button type="submit">Update Profile</button>
      {message && <p>{message}</p>}
    </form>
  );
}

export default UpdateUserForm;
