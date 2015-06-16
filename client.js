// Example client script

newsock.onmessage = function (data) {
  var dataObj = data.data; 
  var scurry = JSON.parse(dataObj); 
  console.log(scurry.data);
};