// //Team Ringbearers :: Brianna Tieu, Shinji Kusakabe
// SoftDev pd08
// K31 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ADD8E6";

var requestID; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0, 0,c.width,c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    //clear the slate or playground
    clear();
    //check if the circle is meant to grow AND diameter is larger than canvas
    if (growing === true && radius >= c.width / 2) {
        growing = false;
    } else if (growing === false && radius <= 0){
        growing = true;
    }
    //check if the circle is meant to grow and adjust radius accordingly
    if (growing === true) {
        radius = radius + 2;
    } else {
        radius = radius - 2;
    }

    ctx.beginPath();
    ctx.arc(250, 250,radius,0,2*Math.PI,false);
    ctx.fill();
    ctx.closePath();

    //cancel must go before request, otherwise the button must be clicked
    //each time to grow the circle (but porque?)
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);