(function () {
  if (Window && WebSocket && !Window.morus) {

    Window.morus = new WebSocket('ws://localhost:3000');

    Window.morus.onmessage = function (data) {
      var dataArray = JSON.parse(data.data); 
      var realArray = new Array(dataArray);
      var scaleWeight = parseInt(realArray[4]) / 10;
      var unitByte = realArray[1];
      var units = '';

      switch (unitByte) {
        case 2: 
          units = 'err';
          break;
        case 3: 
          units = 'lbs.';
          break;
        case 4: 
          units = 'kg.';
          break;
        default: 
          units = 'NaN';
          break;
      }
    
      console.log(realArray); // This is an array of strings.  Index 4 is the weight in tenths of lbs.
    };

  } else {
    console.log('Not Available To Connect');
  }
})();
