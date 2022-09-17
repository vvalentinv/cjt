let phoneInput = document.getElementById('phone-input');
let passwordInput = document.getElementById('password-input');
let firstNameInput = document.getElementById('firstname-input');
let lastNameInput = document.getElementById('lastname-input');
let emailInput = document.getElementById('email-input');
let registrationSubmitButton = document.getElementById('register-submit-btn');
let loginErrorMessageDiv = document.getElementById('login-error-message');
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";


registrationSubmitButton.addEventListener('click', registerUser)
async function registerUser(event) {
  event.preventDefault();
  let res = await fetch(`http://${devDomain}:8080/users`, {
    credentials: 'include',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      "email": emailInput.value,
      "password": passwordInput.value,
      "first_name": firstNameInput.value,
      "last_name": lastNameInput.value,
      "phone": phoneInput.value
    })
  })

  if (res.status == 200) {
    let data = await res.json();
    localStorage.setItem("user_fname", data.first_name)
    localStorage.setItem("user_lname", data.last_name)
    localStorage.setItem("role", data.role_name)
    localStorage.setItem("id", data.user_id)
    window.location.href = "tours.html"
  } else if (res.status == 400) {
    loginErrorMessageDiv.innerHTML = ""
    let data = await res.json();
    let errorElement = document.createElement('p');
    errorElement.innerHTML = data.message;
    errorElement.style.color = 'red';
    errorElement.style.fontWeight = 'bold';
    loginErrorMessageDiv.appendChild(errorElement);
  }
};
