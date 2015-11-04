# Morus
![Morus Logo](https://github.com/dmitrydwhite/morus/blob/master/icons/apple-icon-180x180.png?raw=true)
---
#### version 0.1.1
by Dmitry White

### What it is
Morus is a custom-designed interface specifically to connect a USB HID scale with a browser on a Windows system.

---
### How to use it
v 0.1.1: 
* Download this repo.
* Create a desktop shortcut to `/dist/morus.exe`
* In the markup of your web-page, include this script tag in the page head:
```
    <script type="text/javascript" src="https://rawgit.com/dmitrydwhite/morus/master/client_min.js"></script>
```
* In your markup, add a class named `"morus-weight"` to the element that you want to display the scale weight, usually an `<input>` element.
* If you want your page to display alternate units, add a class named `"morus-units"` to the element where you want the units displayed.
* Plug the scale in to a USB port on your computer and make sure the scale is turned on.
* Run `/dist/morus.exe`, probably by double-clicking the desktop shortcut you created.  A console window should open with some introductory information.  Hello!
* Load your web-page.
* Morus should start right away.  In the dedicated console window, you should start seeing some data, and your markup should be displaying the correct information from the scale.
* Enjoy!

---
