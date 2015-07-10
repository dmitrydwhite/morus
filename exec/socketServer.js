var WebSocketServer = require('ws').Server;
var reader = require('./deviceReader');
var wss = new WebSocketServer({host:'localhost', port:3000});

console.log('M.O.R.U.S');

wss.on('connection', function(client) {
  console.log('Connecting...');
  client.on('close', function () {
    reader.suspend();
    console.log('Handshake failed');
  });
  // reader.start('2338', '32775', client);  // This is for the actual scale
  reader.start('1452', '781', client);  // This is finding the usb mouse for testing purposes
});