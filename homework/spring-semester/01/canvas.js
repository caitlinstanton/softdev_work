/*
Caitlin Stanton
SoftDev2 pd 3
HW 1b -- Finding Your Path Around the Canvas
2016-02-10
*/


var c = document.getElementById("ftb2maga");
	//getElementById() method returns the element that has the given ID
	//allows you to manipulate or get information from that specific element
var ctx = c.getContext("2d");
	//defines the 2d drawing context of the canvas
	//basically activates the 2d drawing aspect of the canvas
	

//draws a black filled in rectangle		
ctx.fillStyle = "black";
	//sets the color for shapes to be filled with (when the fill() or fillRect() methods are used)
	//color is set using a hexcode or the written out color itself
		//e.g. if you want black: #000000, #000, "black"
ctx.fillRect(50,50,300,50);
	//method to create a rectangle that is filled with the color set using fillStyle
	/* fillRect(x,y,w,h)
		- x,y: coordinates of the top left corner of the rectangle
		- w: width of the rectangle, rightward horizontal distance from the top right corner of the rectangle
		- h: height of the rectangle, downward vertical distance from the top right corner of the rectangle
	*/
	
	
//draws a hollow rectangle with blue sides
ctx.strokeStyle = "#0000ff";
	//sets the color for lines/strokes drawn (when the stroke() or strokeRect() methods are used)
	//color is set using a hexcode or the written out color itself
		//e.g. if you want blue: #0000ff, "blue"
ctx.strokeRect(75, 75, 400, 50);
//method to create a hollow rectangle whose lines are the color set using strokeStyle
	/* strokeRect(x,y,w,h)
		- x,y: coordinates of the top left corner of the rectangle
		- w: width of the rectangle, rightward horizontal distance from the top right corner of the rectangle
		- h: height of the rectangle, downward vertical distance from the top right corner of the rectangle
	*/

	
//draws a hollow triangle with green sides
ctx.beginPath();
	//begins a new path by resetting the program from the last path
	//prevents new paths from being connected (if you don't want them to)
ctx.moveTo(0,150);
	//moves the path created to the specific point given, without drawing a line
	/* moveTo(x,y)
		- x,y: coordinates of the point the path will be moved to
	*/
ctx.lineTo(200,200);
	//creates a path from the last specified point on the path to the given point
	/* lineTo(x,y)
		- x,y: coordinates of point to which the path will move, draws a line to this point
	*/
ctx.lineTo(300,450);
ctx.closePath();
	//creates a path from the last specified point on the path back to the starting point
ctx.stroke();
	//draws a line over the path defined using the moveTo() and lineTo() functions
	//drawn in the color last set by strokeStyle(), or reverts to default color of black


//draws a red filled in rectangle
ctx.beginPath();
ctx.moveTo(0,250);
ctx.lineTo(250,250);
ctx.lineTo(250,300);
ctx.lineTo(0,300);
ctx.closePath();
ctx.fillStyle = "#ff0000";
ctx.fill();
	//fills the shape defined by the current path
	//drawn in the color last set by fillStyle(), or reverts to default color of black

	
//draws a purple filled in triangle with orange sides	
ctx.beginPath();
ctx.moveTo(75,400);
ctx.lineTo(150,500);
ctx.lineTo(100,300);
ctx.closePath();
ctx.strokeStyle = "orange";
ctx.stroke();
ctx.fillStyle = "purple";
ctx.fill();


//draws a closed arc with orange sides
ctx.beginPath();
ctx.arc(400,400,65,0,1.5*Math.PI);
	//draws a circular arc path defined by the parameters given
	/* arc(x,y,r,start,end)
		- x,y: coordinates of the center of the circle/arc
		- r: radius of the circle/arc
		- start: starting angle from which the arc will be drawn, measured in radians
		- end: ending angle to which the arc will be drawn, measured in radians
	*/
ctx.closePath();
ctx.stroke();


//inserts text onto the canvas
ctx.font = "oblique bold 65px sans-serif";
	//sets the properties for all text on the canvas
	/* can have a combination of possible parameters:
		- font-style (stroke style, i.e. how slanty it is): normal, italic, oblique, etc.
		- font-weight (stroke weight, i.e. how bold it is): normal, bold, 200, etc.
		- font-size: measured in pixels
		- font-family (type of font)
	*/
ctx.fillStyle = "#075b89";
	//sets fillStyle to a navy color
ctx.fillText("hello world!",0,500);
	//writes the given piece of text, with the top left corner of the word at the given coordinates
	//written in the color last set by fillStyle(), or reverts to default color of black
	//written using the properties set using the font property
	/* fillText("text",x,y)
		- "text": text you want to be written, in quotes
		- x,y: coordinates of the top left corner of the text being written
	*/
ctx.font = "italic 10px verdana";
ctx.strokeStyle = "#eeff00";
	//sets strokeStyle to a yellow color
ctx.strokeText("i'm a secret SHHHHSHHHH",350,250);
	//writes the given piece of text, with the top left corner of the word at the given coordinates
	//written in the color last set by strokeStyle(), or reverts to default color of black
	//written using the properties set using the font property
	/* strokeText("text",x,y)
		- "text": text you want to be written, in quotes
		- x,y: coordinates of the top left corner of the text being written
	*/