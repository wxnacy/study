// node 使用 cluster 模块来创建多核服务
const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length; // 获取CPU的个数
const process = require('process');

if (cluster.isMaster) {
  console.log(`Start server master pid: ${process.pid}`);
  for (var i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', function(worker, code, signal) {
    console.log(`suicide ${worker.suicide}, code ${code}, signal ${signal}`);
    console.log('worker ' + worker.process.pid + ' died');
    // cluster.fork();
  });
} else {

  console.log(`Start server on 0.0.0.0:8000 pid: ${process.pid}`);
  http.createServer(function(req, res) {
    console.log(`Work on pid: ${process.pid}`);
    res.writeHead(200);
    res.end("hello world\n");
  }).listen(8000);
}

// > $ node index.js                                       ⬡ 10.15.0 [±master ●●]
// Start server on 0.0.0.0:8000 pid: 29564
// Start server on 0.0.0.0:8000 pid: 29563
// Start server on 0.0.0.0:8000 pid: 29567
// Start server on 0.0.0.0:8000 pid: 29565
// Start server on 0.0.0.0:8000 pid: 29566
// Start server on 0.0.0.0:8000 pid: 29568
// Start server on 0.0.0.0:8000 pid: 29569
// Start server on 0.0.0.0:8000 pid: 29570
// Work on pid: 29564
// Work on pid: 29563
// Work on pid: 29567
// Work on pid: 29565
// Work on pid: 29566
// Work on pid: 29568
// Work on pid: 29569
// Work on pid: 29570
