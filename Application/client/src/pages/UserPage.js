import React from 'react';
import UpdateUserForm from '../components/UpdateUserForm';
import ChangePasswordForm from '../components/ChangePasswordForm';

function UserPage() {
  return (
    <div>
      <h1>User Profile</h1>
      <UpdateUserForm />
      <ChangePasswordForm />
    </div>
  );
}

export default UserPage;
