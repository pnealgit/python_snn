const connection = new WebSocket('ws://localhost:8088');
var name = "testbed";
connection.onopen = () => {
  console.log('connected');
};

connection.onclose = () => {
  console.error('disconnected');
};

connection.onerror = error => {
  console.error('failed to connect', error);
};

var msg_type = "";
connection.onmessage = (event) => {
	//console.log('received', event.data);
        var state = event.data.split(',');
	var msg_type = state.shift();
	var name = state.shift();

	if (msg_type == "new" ) {
		console.log("NEW: ",state);
		ROVERS[name] = {};
		ROVERS[name]['Color'] = state.shift();
		var SETUP = {};

		SETUP['name'] = name;
		SETUP['width'] = WIDTH;
		SETUP['height'] = HEIGHT;
		SETUP['rectangles'] = rectangles;

		var jsetup = "";
		jsetup = JSON.stringify(SETUP);
        	connection.send(jsetup);
	} //end of if on 'new'


	if (msg_type == "position" ) {
		//var istate = state.split(',').map(Number);
		var istate = state.map((i) => Number(i));
		ROVERS[name]['Xpos'] = istate.shift();
		ROVERS[name]['Ypos'] = istate.shift();
		ROVERS[name]['NUM_SENSORS'] = istate.shift();

		var sensor_data = [];
		for (var k=0;k<ROVERS[name]['NUM_SENSORS'];k++) {
			var sdxy = [];
		    	sdxy.push(istate.shift());
		    	sdxy.push(istate.shift());
			sensor_data.push(sdxy);
		}
		ROVERS[name]['SENSOR_DATA'] = sensor_data;

		updateGameArea();
	}
} //end of on message
