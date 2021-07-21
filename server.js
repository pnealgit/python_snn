//import WebSocket, { WebSocketServer } from 'ws';
const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8088 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(data, isBinary) {
	  console.log(data);
    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(data, { binary: isBinary });
      }
    });
  });
});

