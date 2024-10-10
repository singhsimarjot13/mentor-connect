import React, { useState } from "react";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    // Call API to login user
    console.log(
      `Logging in with username: ${username} and password: ${password}`
    );
  };

  return (
    <div>
      <h2 className="login-title">Login</h2>
      <form className="login-form" onSubmit={handleSubmit}>
        <label className="login-label">Username:</label>
        <input
          className="login-input"
          type="text"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
        />
        <br />
        <label className="login-label">Password:</label>
        <input
          className="login-input"
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
        <br />
        <button className="login-submit-button" type="submit">
          Login
        </button>
      </form>
      <p className="signup-message">
        Don't have an account? <a href="/Signup">Sign up</a>
      </p>
    </div>
  );
};

export default Login;
