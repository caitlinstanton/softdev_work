
var c = document.getElementById("playground");
/*
	Caitlin Stanton
	SoftDev2 pd 3
	HW 2b -- Dot, Dot, Dot
	2016-02-11
*/

var c = document.getElementById("playground");
	//gets the canvas element based on its ID so that it can be manipulated
var ctx = c.getContext("2d");
	//basically activates the 2d drawing aspect of the canvas
var button = document.getElementById("clear");
	//gets the button element based on its ID so that it can be manipulated
	
/* FUNCTION TO MAKE CIRCLES AT MOUSE CLICKS AND CONNECT THESE CIRCLES */
/* ACTIVATED WHEN CANVAS IS CLICKED */
var dots = function(e) {
	var mouse = getPosition(c,e);
		//gets the values returned from getPosition()
		//can access the x and y coordinates of the mouse click
	var x = mouse.x;
	var y = mouse.y;
	ctx.strokeStyle = "blue";
	ctx.arc(x,y,5,0,2*Math.PI);
		//creates a circle of radius 5 at the coordinates of the mouse click
	ctx.lineTo(x,y);
		//draws a path from the last specified point on the path to the coordinates of the mouse click
	ctx.stroke();
		//draws a stroke over the path/circles created
};

/* FUNCTION TO GET THE COORDINATES OF THE MOUSE CLICK */
/* CALLED IN DOTS FUNCTION, WHEN CANVAS IS CLICKED */
function getPosition(canvas,event) {
	var bounds = canvas.getBoundingClientRect();
		//getBoundingClientRect() returns the size of the element and its position relative to the viewport
	return {	//both elements are returned
		x: event.clientX - bounds.left,
			//gets the x coordinate of the mouse click (event)
			//takes into account the left-horizontal relative position of the canvas in relation to the viewport
		y: event.clientY - bounds.top
			//gets the y coordinate of the mouse click (event)
			//takes into account the top-vertical relative position of the canvas in relation to the viewport	
	};
}

c.addEventListener("click",dots);
	//calls the dots() function when the mouse is clicked in the canvas

/* FUNCTION TO CLEAR CANVAS */
/* ACTIVATED WHEN BUTTON IS CLICKED */
button.addEventListener("click",function() {
	ctx.clearRect(0, 0, c.width, c.height);
		//clears the pixels specified within a given rectangle
		/* clearRect(x,y,w,h)
			- x,y: coordinates of the top-left corner of the rectangle in question
			- w: width of the rectangle in question
			- h: height of the rectangle in question
		*/
	ctx.beginPath();
		//called so that each instance of the canvas after it's cleared begins a new path of dots/lines
		//stops layers of previous shapes from resurfacing after being cleared and then the canvas is clicked again
		//essentially makes sure that the canvas is blank even after it's cleared and clicked again
}, false);