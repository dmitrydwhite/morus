(function () {
  if (Window && WebSocket && !Window.morus) {

    Window.morus = new WebSocket('ws://localhost:3000');

    Window.morus.onmessage = function (data) {
      var dataArray = data ? JSON.parse(data.data) : []; 
      var realArray = new Array(dataArray);
      var scaleWeight = parseInt(realArray[4]) / 10;
      var unitByte = realArray[1];
      var units = '';
      var Mweight = document.getElementsByClassName('morus-weight')[0]
      var Munits = document.getElementsByClassName('morus-units')[0]

      if (unitByte === 3) {
        units = 'lbs.';
      } else if (unitByte === 4) {
        units = 'kg.';        
      } else {
        units = 'NA'
      }

      if (scaleWeight == NaN) {
        scaleWeight = 'ØØ'
      }
      
      // $('.morus-weight').text(scaleWeight);
      // $('.morus-units').text(units);
      if (Mweight) {
        Mweight.value = scaleWeight
      }

      if (Munits) {
        Munits.value = units
      }

      console.log(realArray); // This is an array of strings.  Index 4 is the weight in tenths of lbs.
    };

  } else {
    console.log('Not Available To Connect');
  }
})();
