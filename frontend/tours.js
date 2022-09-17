let getBtn = document.getElementById("get");
let tourElement = document.getElementById("tours");
let logoutBtn = document.getElementById("logout");
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";
let loginBtn = document.getElementById("login");
let registerBtn = document.getElementById("register");
let addButton = document.getElementById("addtours");
let myTourBtn = document.getElementById("mytours")
let allTourBtn = document.getElementById("alltours")

logoutBtn.addEventListener('click', logout);
document.addEventListener('DOMContentLoaded', addTours);
window.addEventListener('popstate', addTours);

document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('role')) {
    loginBtn.remove();
    registerBtn.remove();
    if (localStorage.getItem("role") == "user") {
      addButton.remove();
      myTourBtn.remove();

    }
  } else {
    logoutBtn.remove();
    addButton.remove();
    myTourBtn.remove();
    allTourBtn.remove();
  }

})

async function addTours() {
  try {
    let res = await fetch(`http://${devDomain}:8080/tours`, {
      credentials: 'include'
    });

    if (res.status == 200) {
      let data = await res.json();
      addToursToTable(data)
    }
  } catch (err) {
    console.log(err.message);
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

function addToursToTable(data) {
  for (const tour of data.tours) {
    let route_name = tour[0]
    let route_id = tour[1]
    let guide_id = tour[2]
    let day = tour[3]
    let price = tour[4]
    let inactive = tour[5]

    let row = document.createElement("tr");
    let idCell = document.createElement("td");
    let routeCell = document.createElement("td");
    let guideCell = document.createElement("td");
    let dayCell = document.createElement("td");
    let priceCell = document.createElement("td");

    idCell.innerHTML = route_name;
    priceCell.innerHTML = "$" + parseFloat(price / 100).toFixed(2);
    routeCell.innerHTML = route_id;
    guideCell.innerHTML = guide_id;

    if (day == 1) { dayCell.innerHTML = "Monday"; }
    if (day == 2) { dayCell.innerHTML = "Tuesday"; }
    if (day == 3) { dayCell.innerHTML = "Wednesday"; }
    if (day == 4) { dayCell.innerHTML = "Thursday"; }
    if (day == 5) { dayCell.innerHTML = "Friday"; }
    if (day == 6) { dayCell.innerHTML = "Saturday"; }
    if (day == 7) { dayCell.innerHTML = "Sunday"; }

    row.appendChild(routeCell);
    row.appendChild(guideCell);

    row.appendChild(idCell);
    row.appendChild(dayCell);
    row.appendChild(priceCell);

    tourElement.appendChild(row);
  }
}
