var rectangles = []
function make_rectangle() {
    "use strict";
    var r = {}
    r.rw = 50;
    r.rh = 50;
    r.ulx = (WIDTH/2)-r.rw/2
    r.uly = (HEIGHT/2) - r.rh/2
    rectangles.push(r)

    r = {}
    r.rw = 10;
    r.rh = 10;
    r.ulx = 40;
    r.uly = 40;
    rectangles.push(r)

    r = {}
    r.rw = 10;
    r.rh = 10;
    r.ulx = 200;
    r.uly = 200;
    rectangles.push(r)

    r = {}
    r.rw = 10;
    r.rh = 10;
    r.ulx = 180;
    r.uly = 180;
    rectangles.push(r)

    r = {}
    r.rw = 10;
    r.rh = 10;
    r.ulx = 280;
    r.uly = 45;
    rectangles.push(r)

    r = {}
    r.rw = 10;
    r.rh = 10;
    r.ulx = 5;
    r.uly = 220;
    rectangles.push(r)

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
        ctx.fillRect(r.ulx,r.uly,r.rw,r.rh)
        ctx.closePath();
    }
}


