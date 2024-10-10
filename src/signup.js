// Signup function
function signup(username, password, confirmPassword) {
  console.log(
    `Signing up with username: ${username} and password: ${password}`
  );
  // Call API to sign up the user (if necessary)
}

// Get elements from the form
const signupForm = document.querySelector(".signup-form");

// Add event listener to handle form submission
signupForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const username = document.querySelector(".login-input[type='text']").value;
  const password = document.querySelector(
    ".login-input[type='password']"
  ).value;
  const confirmPassword = document.querySelector(
    ".login-input.confirm-password"
  ).value;
  signup(username, password, confirmPassword);
});
