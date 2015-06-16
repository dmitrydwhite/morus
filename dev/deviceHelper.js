var HID = require('node-hid');
var devices = HID.devices();
devices.forEach(function (device) {
  console.log(device);
});