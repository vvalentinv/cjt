let getBtn = document.getElementById("get");
let updateBtn = document.getElementsByName("update");
let tourElement = document.getElementById("tours");
let logoutBtn = document.getElementById("logout");
let addButton = document.getElementById("addtour");
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";

window.addEventListener('popstate', addTours);
document.addEventListener("DOMContentLoaded", addTours);
logoutBtn.addEventListener("click", logout);
document.addEventListener("DOMContentLoaded", loginstatus);

function loginstatus() {
  if (localStorage.getItem("role") == "user") {
    window.location.href = "/tours.html";
    if (localStorage.getItem("role") != "guide") {
      window.location.href = "/tours.html";
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('guide')) {
    loginBtn.remove();
    registerBtn.remove();
  } else {
    logoutBtn.remove();
    addButton.remove();
    myTourBtn.remove();
    allTourBtn.remove();
  }

})

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

async function addTours() {
  try {
    let id = localStorage.getItem("id");
    let res = await fetch(`http://${devDomain}:8080/tours/${id}`, {
      credentials: 'include'
    });
    if (res.status == 200) {
      let data = await res.json();
      addToursToTable(data);
    }
  } catch (err) {
    console.log(err.message);
  }
}

function update_tour(event) {
  let tid = event.target.value;
  localStorage.setItem("tid", tid);
  console.log(tid);
  window.location.href = "/update.html";
}

async function delete_tour(event) {
  try {
    let tid = event.target.value;
    //console.log(tid)
    let res = await fetch(`http://${devDomain}:8080/tour/${tid}`, {
      method: "DELETE",
    });
    if (res.status == 200) {
      window.location.href = "/mytours.html";
    }
  } catch (err) {
    console.log(err.message)
  }
}

function addToursToTable(data) {
  for (const tour of data.tours) {
    let route_name = tour[0];
    let route_id = tour[1];
    let guide_id = tour[2];
    let day = tour[3];
    let price = tour[4];
    let tid = tour[5];

    let row = document.createElement("tr");
    let idCell = document.createElement("td");
    let routeCell = document.createElement("td");
    let guideCell = document.createElement("td");
    let dayCell = document.createElement("td");
    let priceCell = document.createElement("td");
    let updateButton = document.createElement("button");
    let buttonCell = document.createElement("td");

    updateButton.name = "update";
    updateButton.innerHTML = "Update";
    updateButton.value = tid;
    updateButton.id = tid;
    updateButton.className = "button";
    updateButton.style = "margin-bottom: 10px";
    updateButton.onclick = update_tour;

    let deleteButton = document.createElement("button");
    deleteButton.id = "delete";
    deleteButton.innerHTML = "Delete";
    deleteButton.value = tid;
    deleteButton.className = "button";

    deleteButton.onclick = delete_tour;

    localStorage.setItem(route_id, tour);
    buttonCell.appendChild(updateButton);
    buttonCell.appendChild(deleteButton);
    idCell.innerHTML = route_name;
    priceCell.innerHTML = "$" + parseFloat(price / 100).toFixed(2);
    routeCell.innerHTML = route_id;
    guideCell.innerHTML = guide_id;
    if (day == 1) {
      dayCell.innerHTML = "Monday";
    }
    if (day == 2) {
      dayCell.innerHTML = "Tuesday";
    }
    if (day == 3) {
      dayCell.innerHTML = "Wednesday";
    }
    if (day == 4) {
      dayCell.innerHTML = "Thursday";
    }
    if (day == 5) {
      dayCell.innerHTML = "Friday";
    }
    if (day == 6) {
      dayCell.innerHTML = "Saturday";
    }
    if (day == 7) {
      dayCell.innerHTML = "Sunday";
    }
    row.appendChild(idCell);
    row.appendChild(routeCell);
    row.appendChild(dayCell);
    row.appendChild(priceCell);
    row.appendChild(buttonCell);
    tourElement.appendChild(row);
  }
}
