function updateGameArea() {
    "use strict";
    var s = "";
    var response;
    myGameArea.clear();
    myGameArea.frameNo += 1;
    draw_rectangle();

    for(var r in ROVERS) {
        draw_rovers(r);
    }
}
