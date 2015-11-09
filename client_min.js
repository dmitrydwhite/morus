(function () {
  if (Window && WebSocket && !Window.morus) {

    Window.morus = new WebSocket('ws://localhost:3000/');

    Window.morus.onmessage = function (data) {
      var realArray = data ? JSON.parse(data.data) : [];
      var twentyFives = parseInt(realArray[5]);
      var scaleWeight = (parseInt(realArray[4]) / 10) + (twentyFives * 25.6);
      var unitByte = realArray[2];
      var units = '';
      var Mweight = document.getElementsByClassName('morus-weight')[0];
      var Munits = document.getElementsByClassName('morus-units')[0];

      if (unitByte === 12) {
        units = 'lbs.';
      } else if (unitByte === 3) {
        units = 'kg.';        
      } else {
        units = 'NA';
      }

      if (scaleWeight === NaN) {
        scaleWeight = 'Ee';
      }

      if (Mweight) {
        Mweight.value = scaleWeight;
        Mweight.innerHTML = scaleWeight;
      }

      if (Munits) {
        Munits.value = units;
        Munits.innerHTML = units;
      }
    };

  }
})();
