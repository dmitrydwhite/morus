# Morus
![Morus Logo](https://github.com/dmitrydwhite/morus/blob/master/icons/apple-icon-180x180.png?raw=true)
---
#### version 0.0.3
by Dmitry White

### What it is
Morus is a custom-designed interface specifically to connect a USB HID scale with a browser.

---
### How to use it
v 0.0.3: 
* In the command line, run
```
    node ./exec/socketServer.js
```
* In the markup of your web-page, include this script tag in the page head:
```
    <script type="text/javascript" src="https://rawgit.com/dmitrydwhite/morus/master/client.js"></script>
```
If you don't already have the jQuery, please do include it before the Morus script tag.
* Then, in your HTML, include the following tags:
```
    <span class="morus-weight"></span> // This will be filled with the scale weight 
    <span class="morus-units"></span>  // This will be filled with the weight units
```

---
### Other cool things
* In the command line, run 
```
    node ./dev/deviceHelper.js
```
in order to get a list of all the USB HID's connected to the system.