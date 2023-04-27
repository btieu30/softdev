// Team TT :: Brianna Tieu and Vivian Teo
// SoftDev pd8
// K32 -- JS Bounce
// 2023-04-27
// --------------------------------------------------

var c = document.getElementById("playground");

var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("buttonDVD");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
var requestID; //counter for time


ctx.fillStyle = "blue";stopButton.addEventListener("click", stopIt);
var clear = function(e) {
    // e.preventDefault(); //prevents
    ctx.clearRect(0,0,c.width,c.height);
}

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 120;
    var rectHeight = 60;

    var rectX = Math.random() * (c.width-rectWidth); //random coords 
    var rectY = Math.random() * (c.width-rectHeight); //random coords 

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0,0,c.width,c.height);
        ctx.drawImage(logo,rectX,rectY,rectWidth,rectHeight);

        if (rectX + rectWidth >= c.width || rectX <= 0) {
            xVel = -1 * xVel;
        }

        if (rectY + rectHeight >= c.width || rectY <= 0) {
            yVel = -1 * yVel;
        }

        rectX += xVel;
        rectY += yVel;

        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};

var radius = 0;
var growing = true;

var drawDot = (e) => {
    console.log("drawDot invoked...");
    clear(e); //wipe the canvas

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
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);