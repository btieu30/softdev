// Team TT :: Donald Bi and Vivian Teo
// SoftDev pd8
// K31 -- JS Paint, Paint, Paint...
// 2023-04-26
// --------------------------------------------------

var c = document.getElementById("playground");

var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID; //counter for time

var clear = () => {
    ctx.clearRect(0,0,c.width,c.height);
}

var radius = 0;
var growing = true;

var drawDot = () => {
    console.log("drawDot invoked...");
    clear(); //wipe the canvas

    // if reach bounds, stop growing/shrinking
    if (radius===(c.height/2)) {
        growing = false;
    }
    if (radius<=0) {
        growing = true;
    }

    // change radius (growing/shrinking)
    if (growing) {
        radius++
    }
    else {radius--}

    drawCircle(); //draw circle

    window.cancelAnimationFrame(requestID); //prevents exponential growth
    requestID = window.requestAnimationFrame(drawDot); 
}

var stopIt = () => {
    console.log("stopIt invoked...")

    window.cancelAnimationFrame(requestID);
    console.log("requestID cancelled");
}


var drawCircle = function() {
    centerX = c.width/2;
    centerY = c.width/2;
    ctx.beginPath();
    ctx.arc(centerX,centerY,radius,0,2*Math.PI,false);
    ctx.fill();
    ctx.stroke();    
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);