var c = document.getElementById("ftb2maga");
var ctx = c.getContext("2d");
/*
ctx.fillStyle = "#000000";
ctx.fillRect(50,50,500,50);

ctx.strokeStyle = "#0000ff";
ctx.strokeRect(75, 75, 500, 50);


ctx.beginPath();
ctx.moveTo(0,500);
ctx.lineTo(500,500);
ctx.lineTo(500,750);
ctx.closePath();

ctx.strokeStyle = "#00ff00";
ctx.fillStyle = "#ff0000";
ctx.stroke();

ctx.beginPath();
ctx.moveTo(0,250);
ctx.lineTo(250,250);
ctx.lineTo(750,0);
ctx.closePath();
ctx.fill();

ctx.beginPath();
ctx.moveTo(400,250);
ctx.lineTo(600,250);
ctx.lineTo(600,0);
ctx.lineTo(500,350);
ctx.closePath();
ctx.stroke();
ctx.fill();
*/

ctx.beginPath();
//ctx.moveTo(100,200);
ctx.arc(200,200,100,0,-500);
//ctx.closePath();
ctx.stroke();
ctx.font = "90px arial";
ctx.fillText("texty text",300,300);
