// Team TT :: Brianna Tieu and Vivian Teo
// SoftDev pd8
// K30 -- JS Paint
// 2023-04-25
// --------------------------------------------------

//retrieve node in DOM via ID
var c = document.getElementById("slate");
var makeButton = document.getElementById("buttonToggle");
var wipeButton = document.getElementById("buttonClear");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
        makeButton.innerHTML = "Circle";
    }
    else {
        mode = "rect"
        makeButton.innerHTML = "Rectangle";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillStyle = "orange";
    ctx.fillRect(mouseX, mouseY, 50, 60)
}

var drawCircle = function(e) {
    var mouseX = e.offsetX //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    centerX = c.width/2;
    centerY = c.width/2;
    ctx.beginPath();
    ctx.arc(mouseX,mouseY,20,0,2*Math.PI,false);
    ctx.fillStyle = "orange";
    ctx.fill();
    ctx.stroke();    
}

var draw = function(e) {
    if (mode==="rect") {
        console.log("rectangling...");    
        drawRect(e);
    }
    else {
        console.log("circling...");
        drawCircle(e);
    }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    ctx.clearRect(0,0,c.width,c.height);
}    

c.addEventListener("click", draw) //passes the mouse event as parameter for the function
makeButton.addEventListener("click", toggleMode)
wipeButton.addEventListener("click", wipeCanvas) //wipe canvas clean
