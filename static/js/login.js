// Login function
function login(username, password) {
  console.log(
    `Logging in with username: ${username} and password: ${password}`
  );
  // Call API to log in the user (if necessary)
}

// Get elements from the form
const loginForm = document.querySelector(".login-form");

// Add event listener to handle form submission
loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const username = document.querySelector(".login-input[type='text']").value;
  const password = document.querySelector(
    ".login-input[type='password']"
  ).value;
  login(username, password);
});
