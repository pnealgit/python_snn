var rectangles = []
var FOOD = 2;
var POISON = 1;

function make_rectangle() {
    "use strict";
    //1 is poison
    //2 is food

    //make big poison
    var r = {}
    r.rw = 50;
    r.rh = 50;
    r.ulx = (WIDTH/2)-r.rw/2
    r.uly = (HEIGHT/2) - r.rh/2
    r.type = POISON;
    r.eaten = 0;
    rectangles.push(r)

    //make poisons
    for(var j=0;j<10;j++) {
	r = {}
    	r.rw = 10;
    	r.rh = 10;
    	r.ulx = getRandomInt(10,WIDTH-10);
    	r.uly = getRandomInt(10,HEIGHT-10);
    	r.type = POISON;
	r.eaten = 0;
        rectangles.push(r)
    }
    //make food 
    for(var j=0;j<20;j++) {
	r = {}
    	r.rw = 10;
    	r.rh = 10;
    	r.ulx = getRandomInt(10,WIDTH-10);
    	r.uly = getRandomInt(10,HEIGHT-10);
    	r.type = FOOD;
	r.eaten = 0;
        rectangles.push(r)
    }

console.log("RECTANGLES: ",rectangles)
}


function draw_rectangle() {
    "use strict";
    var ctx = myGameArea.context
    var r = {}
    for (var i = 0;i<rectangles.length;i++) {
        r = rectangles[i];
        ctx.beginPath();
        ctx.fillStyle = "blue";
	if (r.type == 2) {
		ctx.fillStyle = "green";
	}
        ctx.fillRect(r.ulx,r.uly,r.rw,r.rh)
        ctx.closePath();
    }
}


