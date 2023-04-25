var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ADD8E6";

var requestID = myReq; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0, 0,c.width,c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear(e);
    ctx.beginPath();
    window.requestAnimationFrame(myReq);
    while (growing === true) {
        radius = radius + 2;
        ctx.arc(100, 100,radius,0,2*Math.PI,false);
        //if stopit clicked then growing = false
        // and set growing to false once the radius reaches the bounds of canvas
    }
}

var stopIt = () => {
    
}