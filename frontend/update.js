let updateBtn = document.getElementById("update-Button");
let logoutBtn = document.getElementById("logout");
let touridValue = localStorage.getItem("tid");
let dayInput = document.getElementById("days");
let priceInput = document.getElementById("price");
let radioBtn = document.getElementsByClassName("inactive");
let loginErrorMessageDiv = document.getElementById('login-error-message');
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";
let act = 2;

logoutBtn.addEventListener("click", logout);
updateBtn.addEventListener("click", update);

function loginstatus() {
  console.log()
  if (localStorage.getItem("role") == "user") {
    window.location.href = "/tours.html";
  }
}

async function update() {
  loginErrorMessageDiv.innerHTML = ""
  let active = document.getElementsByName("inactive");
  for (i = 0; i < active.length; i++) {
    if (active[i].checked) {
      act = active[i].value;
      break;
    }
  }

  let res = await fetch(`http://${devDomain}:8080/tour`, {
    method: "PUT",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      tour_id: touridValue,
      day: dayInput.value,
      price: priceInput.value,
      inactive: act,
    }),
  })
  if (res.status == 200) {
    localStorage.removeItem("tid");
    alert("Tour Updated");
    window.location.href = "/mytours.html";
  } else if (res.status == 400) {
    let data = await res.json();
    let errorElement = document.createElement('p');
    errorElement.innerHTML = data.message;
    errorElement.style.color = 'red';
    errorElement.style.fontWeight = 'bold';
    loginErrorMessageDiv.appendChild(errorElement);
  }

}

async function logout() {
  try {
    let res = await fetch(`http://${devDomain}:8080/logout`, {
      'method': 'POST',
    })
    console.log(res);
    if (res.status == 200) {
      localStorage.clear();
      window.alert("Logout Successful");
      window.location.href = "/index.html";
    }
  } catch (err) {
    console.log(err.message)
  }
}
