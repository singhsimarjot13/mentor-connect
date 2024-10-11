document.addEventListener("DOMContentLoaded", () => {
  // Render login and signup HTML
  const root = document.getElementById("root");
  root.innerHTML = `
    <div>
      <div id="login-container"></div>
      <div id="signup-container"></div>
    </div>
  `;

  // Get elements
  const loginBtn = document.getElementById("login-btn");
  const signupBtn = document.getElementById("signup-btn");
  const loginContainer = document.getElementById("login-container");
  const signupContainer = document.getElementById("signup-container");

  // Load login form by default
  function loadLogin() {
    loginContainer.innerHTML = "";
    const loginScript = document.createElement("script");
    loginScript.src = "./login.js";

    loginScript.onload = function () {
      console.log("Login script loaded");
    };
    loginContainer.appendChild(loginScript);
    signupContainer.innerHTML = "";
  }

  // Load signup form when signup is clicked
  function loadSignup() {
    signupContainer.innerHTML = "";
    const signupScript = document.createElement("script");
    signupScript.src = "./signup.js";

    signupScript.onload = function () {
      console.log("Signup script loaded");
    };
    signupContainer.appendChild(signupScript);
    loginContainer.innerHTML = "";
  }

  // Load login by default when the page loads
  loadLogin();

  // Add event listeners for buttons
  loginBtn.addEventListener("click", () => {
    loadLogin();
  });

  signupBtn.addEventListener("click", () => {
    loadSignup();
  });
});
