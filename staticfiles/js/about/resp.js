
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    //document.getElementById("header").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    //document.getElementById("header").style.marginLeft= "0";
};
function myFunction() {
    var x = document.getElementById("password-field");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function myFunction_two() {
    var x = document.getElementById("myDIV");
        x.style.display = "block";
    
}
function myFunction_three() {
    var x = document.getElementById("menu");
        x.style.display = "block";
    
}

