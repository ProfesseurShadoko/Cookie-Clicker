# Cookie-Clicker

A simple script for automating cookie-clicking on the famous
<a href="https://orteil.dashnet.org/cookieclicker/">
  website
</a>!

The code requires the following packages:

```python
import time #used for evaluating performance
import pyautogui #cookie-clicking
import keyboard #pause/unpause
import webbrowser #launch the website
import pyperclip #copy some js code
```

## How to use the tool

Simply run:

```python
CookieClicker().run()
```

The webbrowser will open up and the cookie clicker will be ready to start clicking. Here's how it
works:
  - <kbd>SPACE</kbd> : **pause/unpause the clicker**. The position of your mouse when you hit the key for the first time
  will define the position of the Clicker.
  - <kbd>SHIFT</kbd> + <kbd>SPACE</kbd> : **resets** the position of the clicker and pauses the game.
  - <kbd>CTRL</kbd> + <kbd>SPACE</kbd> : **exit** the programm
  
Of course, the script only works when the webbrowers is open, wich means, you cannot use your computer
while the clicker is running. But there is still a way to activate an automatic clicker that runs in 
background (but slower).
Open the console of the inspector of your browser and simply hit <kbd>CTRL</kbd> + <kbd>V</kbd>,
wich will paste one line of JavaScript code, that will click the Cookie and the Golden Cookies who appear at random.

```javascript
setInterval(() => document.getElementById('bigCookie').click(), 1);
setInterval(() => document.getElementById('shimmers').firstElementChild.click(), 10);
```

## Conclusion

Now enjoy, but remember, cheating is bad!
  
  
