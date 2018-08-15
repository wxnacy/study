const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:4200/test');

ws.on('open', function open() {
  ws.send('wxnacy');
});

ws.on('message', function incoming(data) {
  console.log(data);
});
