let emailLogin = document.getElementById("email-login-input");
let passwordLogin = document.getElementById("password-login-input");
let loginButton = document.getElementById("login");
var enterButton = document.getElementById("email-login-input");
var enterButton1 = document.getElementById("password-login-input");
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";

loginButton.addEventListener('click', loginNow)


document.addEventListener("DOMContentLoaded", loginstatus);




enterButton.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("login").click();
  }
});
enterButton1.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("login").click();
  }
});


document.addEventListener("DOMContentLoaded", loginstatus);


function loginstatus() {
  console.log()
  if (localStorage.getItem("role") == "user") {
    window.location.href = "/tours.html";
  } else if (localStorage.getItem("role") == "guide") {
    window.location.href = "/mytours.html";
  }
}
async function loginNow() {



  if (emailLogin.value != "" && passwordLogin != "") {

    try {
      let res = await fetch(`http://${devDomain}:8080/login`, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "email": emailLogin.value,
          "password": passwordLogin.value
        }),
      })

      let data = await res.json();


      if (res.status == 200) {
        if (data.role_name == "guide") {

          localStorage.setItem("user_fname", data.first_name)
          localStorage.setItem("user_lname", data.last_name)
          localStorage.setItem("role", data.role_name)
          localStorage.setItem("id", data.user_id)
          console.log(localStorage.getItem("role"))
          window.location.href = '/mytours.html'
        }
        if (data.role_name == "user") {
          localStorage.setItem("user_fname", data.first_name)
          localStorage.setItem("user_lname", data.last_name)
          localStorage.setItem("role", data.role_name)

          localStorage.setItem("id", data.user_id)
          window.location.href = '/tours.html'

        }
      }
      if (res.status == 400) {
        alert(data.message)
      }
    }
    catch (err) {
      alert(err);
    }
  }
  else {
    alert("Please enter Username/Password")


  }
}
