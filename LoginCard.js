import React from 'react';

const LoginCard = ({ title, placeholder1, placeholder2, footer }) => {
  return (
    <div className="card">
      <h2>{title}</h2>
      <input type="text" placeholder={placeholder1} />
      <input type="password" placeholder={placeholder2} />
      <button>Login</button>
      <div className="footer">{footer}</div>
    </div>
  );
};

export default LoginCard;
