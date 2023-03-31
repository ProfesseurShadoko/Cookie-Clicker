import pyautogui
import keyboard
import time
import webbrowser
import pyperclip

class ExitGameExcetion(Exception):
    pass

msg ="""
WHEN THE BROWSER IS OPEN:
\t- position your MOUSE over the COOKIE
\t- hit SPACEBAR to launch/pause
\t- hit SHIFT+SPACEBAR to reset the clicking position
\t- hit CTRL+SPACEBAR to exit the programm

Hint: hit CTRL+ALT+J and then CTRL+V and ENTER in order to create a js function that will automatically click the golden cookies, and click even if the window is not open.

"""



class CookieClicker:
    
    """initializes :
    - position=0
    - paused=True
    - count=0
    - time=0
    """
    def __init__(self):
        self.position = None
        self.paused = True
        self.count = 0
        
        #we want to know the total time when the script was running
        self.time = 0
        #therefor, we need to know when the session started (when it was unpaused)
        self.session_start = None
        
        pyautogui.PAUSE = 1e-6
        #pyautogui.PAUSE = 0
        
    def run(self):
        """Runs the script :
        - shows how to use the system
        - copies js script that the user can paste in the inspector console
        - launches a new cookie clicker page
        - calls self.loop()
        - prints out statistics once the loop is over
        """
        print(msg)
        js_auto_click = "setInterval(() => document.getElementById('bigCookie').click(), 1);setInterval(() => document.getElementById('shimmers').firstElementChild.click(), 10);"
        pyperclip.copy(js_auto_click)
        
        webbrowser.open("https://orteil.dashnet.org/cookieclicker/")
        
        try:
            self.loop()
        except ExitGameExcetion:
            print("\nEXIT-GAME\n")
        except KeyboardInterrupt:
            print("^C")
    
    #CLICK
    """run a click at self.position (and updates click_count)
    """
    def click(self):
        pyautogui.click(self.position)
        self.count+=1
       
    """set's position of the click to the current position of the mouse""" 
    def set_position(self):
        self.position = pyautogui.position()
    
    """reset's the position of the clicker (so that he can be moved) and pauses the game"""
    def reset_position(self):
        print("Taking a fresh start !")
        self.position = None
        self.paused = True
        keyboard.read_event()
        time.sleep(1)
    
    #PAUSE/QUIT
    """pauses/unpauses the game & set_position if necessary"""
    def pause(self):
        if self.position == None:
            self.set_position()
        
        if (not self.paused):
            self.stop_session()
        
        self.paused = not self.paused
        keyboard.read_event() #flush event
        time.sleep(1) #avoid bar pressed too long
        
        if (not self.paused):
            self.start_session()
    
    """raise an exception caught by the run function to exit the main loop"""
    def quit(self):
        if not self.paused:
            self.pause()
        raise(ExitGameExcetion())
    
    #STATS
    """returns the frequency of the click """
    def frequency(self) -> float:
        return self.count / self.time if self.time !=0 else 0
    
    """set's time counter for starting a session"""
    def start_session(self):
        print("START")
        self.session_start = time.perf_counter()
    
    """stops time counter for interrupting a session"""
    def stop_session(self):
        stop = time.perf_counter()
        self.time += stop - self.session_start
        print(f"PAUSE after {stop-self.session_start:.2f}s - ({self.count} clicks overall - f={self.frequency():.2f} Hz)")
    
    #MAIN LOOP  
    def loop(self):
        while True:
            if keyboard.is_pressed("space"):
                if keyboard.is_pressed("ctrl"):
                    self.quit()
                if keyboard.is_pressed("shift"):
                    self.reset_position()
                    continue #don't unpause!
                self.pause()
            else:
                if not self.paused:
                    self.click()
    
            
    
