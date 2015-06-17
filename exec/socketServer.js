var WebSocketServer = require('ws').Server;
var reader = require('./deviceReader');
var wss = new WebSocketServer({host:'localhost', port:3000});

wss.on('connection', function(client) {
  console.log('here');
  reader.start('2338', '32775', client);
});