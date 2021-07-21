var WIDTH = 320
var HEIGHT = 240
var ROVER = {};

var NUM_SENSORS = 3 
var Time_to_live = 1000;
var TRY = 0;


function make_table() {
    results = "<tr><td>FITNESS</td></tr>";
    for(i=0;i<ROVERS.length;i++) {
        results = results + "<tr><td>" + ROVERS[i].Fitness + "</td></tr>";
    }
    document.getElementById('fitness_table').innerHTML = results;
}

function startGame() {
        make_rectangle()
        make_table();
        myGameArea.start();
}

myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = WIDTH;
        this.canvas.height = HEIGHT;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.frameNo = 0;
        //this.interval = setInterval(updateGameArea, 5);
	updateGameArea();
        },
    clear : function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
} 
