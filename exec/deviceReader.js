var HID = require('node-hid');

var morusReader = {

  suspended: false,

  start: function (vendorId, productId, socket) {
    var _self = this;
    var devices = HID.devices();

    if (!morusReader.suspended) {
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
    } else {
      morusReader.suspended = false;
      morusReader.connection = socket ? socket : null;
      morusReader.foundScale(morusReader.scale);
    }
  },

  suspend: function () {
    if (!morusReader.suspended) {
      morusReader.suspended = true;
    }
  },

  foundScale: function (device) {
    morusReader.tell('Found Device');
    morusReader.listenForWeight();
  },

  listenForWeight: function () {
    morusReader.scale.on('data', function (data) {
      var newWeight = JSON.stringify(data);
      if (newWeight !== morusReader.tare) {
        morusReader.tare = newWeight;
        morusReader.tell(newWeight);
      }
    });
  },

  couldntFindScale: function () {
    morusReader.tell('Couldn\'t find anticipated scale');
    morusReader.connection.close();
  },

  tell: function (message) {
    console.log(message);
    if (!morusReader.suspended) morusReader.connection.send(message);
  },

  terminate: function () {
    morusReader.scale.off('data');
    morusReader.connection.close();
  }
};

module.exports = morusReader;
