var WebSocketServer = require('ws').Server;
var reader = require('./deviceReader');
var wss = new WebSocketServer({host:'localhost', port:3000});


// use like this:
wss.on('connection', function(client) {
  console.log('here');
  reader.start('1452', '781', client);
});