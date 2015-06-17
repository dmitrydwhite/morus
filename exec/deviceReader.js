var HID = require('node-hid');

var morusReader = {

  start: function (vendorId, productId, socket) {
    var _self = this;
    var devices = HID.devices();

    morusReader.connection = socket ? socket : null;
    morusReader.tare = '';

    devices.forEach(function (device) {
      if (device.vendorId.toString() === vendorId &&
          device.productId.toString() === productId) {
        morusReader.scale = new HID.HID(device.path);
      }
    });
    
    if (morusReader.scale) {
      morusReader.foundScale(morusReader.scale);
    } else {
      morusReader.couldntFindScale();
    }
  },

  foundScale: function (device) {
    morusReader.tell('found %s:%s', device.path,device.manufacturer);
    morusReader.listenForWeight();
  },

  listenForWeight: function () {
    morusReader.scale.on('data', function (data) {
      var scotch = JSON.stringify(data);
      if (scotch !== morusReader.tare) {
        morusReader.tare = scotch;
        morusReader.tell(scotch);
      }
    });
  },

  couldntFindScale: function () {
    morusReader.tell('Couldn\'t find anticipated scale');
    morusReader.connection.close();
  },

  tell: function (message) {
    console.log(message);
    morusReader.connection.send(message);
  },

  terminate: function () {
    morusReader.scale.off('data');
    morusReader.connection.close();
  }
};

module.exports = morusReader;
