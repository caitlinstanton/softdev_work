var c = document.getElementById("playground");
var ctx = c.getContext("2d");

ctx.beginPath();
var dots = function() {
	x = event.clientX + document.body.scrollLeft;
	y = event.clientY + document.body.scrollTop;
	ctx.lineTo(x,y);
	console.log("YES");
};

var clear = function() {
	console.log("clear");
};

c.addEventListener("click",dots);

var button = document.getElementById("clear");
button.addEventListener("click",clear);