// 导入WebSocket模块:
const WebSocket = require('ws');

// 引用Server类:
const WebSocketServer = WebSocket.Server;

// 实例化:
const wss = new WebSocketServer({
    port: 4200
});

wss.on('connection', function connection(ws) {
  console.log("server connection");
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    ws.send(`hello ${message}`)
  });

});
