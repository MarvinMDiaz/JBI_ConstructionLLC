var nav = document.getElementById("nav");
var close = document.getElementById("close");
var list = document.getElementById("list");
var logo = document.getElementById("logo");

var box2 = document.getElementById("box2");

var box1 = document.getElementById("box1");
var bars = document.getElementById("bars");
var header = document.getElementById("header");

function reloadPage() {
    window.location.reload(true);

}

function closeNav() {
    if (i.matches) { // If media query matches
        hideMenu()

    } else {
        nav.style.display = "flex"
    }
    // reloadPage()
}
var i = window.matchMedia("(max-width: 1014px)")
closeNav(i) // Call listener function at run time
i.addListener(closeNav) // Attach listener function on state changes



function showMenu() {
    nav.style.display = "flex";
    close.style.display = "block"
    list.style.display = "none"
    close.style.marginRight = "-22px"
    logo.style.width = "100%"
    box1.style.marginLeft = "8%"
    bars.style.marginRight = "8%"
    logo.style.backgroundColor = "rgb(41, 41, 41)"
    logo.style.opacity = ".8"



}

function hideMenu() {
    // box2.style.display = "flex"
    box1.style.marginLeft = "0%"
    bars.style.marginRight = "0%"
    logo.style.width = "84%"
    logo.style.backgroundColor = "transparent"
    nav.style.display = "none";
    list.style.display = "block"
    close.style.display = "none"
    // bars.style.width = "45%"


}



function myFunction(x) {
    if (x.matches) { // If media query matches
        nav.style.display = "flex"
        logo.style.backgroundColor = "transparent"
    } else {
        nav.style.display = "none"
    }
}

var x = window.matchMedia("(min-width: 1015px)")
myFunction(x) // Call listener function at run time
x.addListener(myFunction) // Attach listener function on state changes



function myFunction2(y) {
    if (y.matches) { // If media query matches

        logo.style.width = "63%"
    } else {
        logo.style.width = "84%"

    }
}

var y = window.matchMedia("(min-width: 1445px)")
myFunction2(y) // Call listener function at run time
y.addListener(myFunction2) // Attach listener function on state changes




// document.getElementById('confetti').addEventListener('click', party)