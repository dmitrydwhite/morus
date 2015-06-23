var WebSocketServer = require('ws').Server;
var reader = require('./deviceReader');
var wss = new WebSocketServer({host:'localhost', port:3000});

console.log('M.O.R.U.S');

wss.on('connection', function(client) {
  console.log('Connecting...');
  // reader.start('2338', '32775', client);
  reader.start('1452', '781', client);
});