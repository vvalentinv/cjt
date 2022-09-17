const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo');
let logoutBtn = document.getElementById("logout");
let loginBtn = document.getElementById("login");
let registerBtn = document.getElementById("register");
let addButton = document.getElementById("addtours");
let myTourBtn = document.getElementById("mytours")
let allTourBtn = document.getElementById("alltours")
let devDomain = "127.0.0.1";
let testDomain = "ec2-34-222-20-217.us-west-2.compute.amazonaws.com";

logoutBtn.addEventListener('click', logout)

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

// Show active menu when scrolling
const highlightMenu = () => {
  const elem = document.querySelector('.highlight');
  const servicesMenu = document.querySelector('#services-page');
  let scrollPos = window.scrollY;

  //adds 'highlight' class to my menu items



  if ((elem && window.innerWIdth < 960 && scrollPos < 600) || elem) {
    elem.classList.remove('highlight');
  }
};
