var ROVERS = {};
var RADIUS = 5;
function draw_rovers(rover_name)
{   

    "use strict";
    var r = ROVERS[rover_name];
    var ctx = myGameArea.context;
    ctx.beginPath();
    ctx.arc(r.Xpos, r.Ypos, RADIUS, 0, 2 * Math.PI);
    ctx.fillStyle = r.Color;
    ctx.fill();
    ctx.closePath();

	
        for(var i =0 ;i<r['NUM_SENSORS'];i++) {
                ctx.beginPath()
                ctx.strokeStyle = '#000000';
                ctx.moveTo(r.Xpos,r.Ypos);
                var xxyy = r.SENSOR_DATA[i];
                ctx.lineTo(xxyy[0],xxyy[1]);
                ctx.stroke();
                ctx.closePath();
        }
} //end fo draw rover

