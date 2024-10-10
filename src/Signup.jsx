import React, { useState } from "react";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    // Call API to signup user
    console.log(
      `Signing up with username: ${username} and password: ${password}`
    );
  };

  return (
    <div>
      <h2 className="login-title">Signup</h2>
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
        <label className="login-label">Confirm Password:</label>
        <input
          className="login-input"
          type="password"
          value={confirmPassword}
          onChange={(event) => setConfirmPassword(event.target.value)}
        />
        <br />
        <button className="login-submit-button" type="submit">
          Signup
        </button>
      </form>
    </div>
  );
};

export default Signup;
