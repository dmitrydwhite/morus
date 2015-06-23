# Morus
![Morus Logo](https://github.com/dmitrydwhite/morus/blob/master/icons/apple-icon-180x180.png?raw=true)
---
#### version 0.0.2
by Dmitry White

### What it is
Morus is a custom-designed interface specifically to connect a USB HID scale with a browser.

---
### How to use it
v 0.0.2: 
* In the command line, run
```
    node ./exec/socketServer.js
```
* In a web-page running locally, include this script tag in the page head:
```
    <script type="text/javascript" src="./client.js"></script>
```
* Then, in your HTML, include the following tags:
```
    <span class="morus-weight"></span> // Will be filled with the scale weight 
    <span class="morus-units"></span>  // Will be filled with the weight units
```

---
### Other cool things
* In the command line, run 
```
    node ./dev/deviceHelper.js
```
in order to get a list of all the USB HID's connected to the system.