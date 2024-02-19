# © Copyright 2024 CrazyH
# This file was originally made by CrazyH
# Do not rebrand if you are distributing it
# © Copyright 2024 CrazyH

# Setup Package Importing
import subprocess, sys, time, os


# Import Packages
try:
  from pynput import mouse, keyboard
  from pynput.mouse import Button, Controller
except ImportError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'pynput'])
finally:
  from pynput import mouse, keyboard
  from pynput.mouse import Button, Controller

try:
  from colorama import Fore, Back, Style
except ImportError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
finally:
  from colorama import Fore, Back, Style


# Define variables
mEnabled = True
mListen = ""
mControl = ""
curr_inpts = {}


# Define Quit Variables
COMBINATIONS = [
  {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char=':')},
]
TOGGLE_COMBINATIONS = [
  {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode(char='/')},
]
current = set()


# Define Functions
cls = lambda: print("\033c\033[3J", end='')

def banner():
  print(f"""{Fore.LIGHTRED_EX}
  ·▄▄▄▄        ▄• ▄▌▄▄▄▄· ▄▄▌  ▄▄▄ .     ▄▄▄·▄▄▄  ▄▄▄ ..▄▄ · .▄▄ · 
  ██▪ ██ ▪     █▪██▌▐█ ▀█▪██•  ▀▄.▀·    ▐█ ▄█▀▄ █·▀▄.▀·▐█ ▀. ▐█ ▀. 
{Fore.RED}  ▐█· ▐█▌ ▄█▀▄ █▌▐█▌▐█▀▀█▄██▪  ▐▀▀▪▄     ██▀·▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄
  ██. ██ ▐█▌.▐▌▐█▄█▌██▄▪▐█▐█▌▐▌▐█▄▄▌    ▐█▪·•▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█
  ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀ ·▀▀▀▀ .▀▀▀  ▀▀▀     .▀   .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀▀ 

{Fore.RED}{Style.BRIGHT}  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

  MADE BY CRAZYH ON GITHUB

  PRESS 'CTRL + SHIFT + SLASH' TO TOGGLE.
  PRESS 'CTRL + SHIFT + SEMICOLON' TO QUIT THIS PROGRAM.
{Style.RESET_ALL}""")

def getInputs():
  mouseButton = input(f"""    {Fore.RED}Enter the mouse button to cheat using (left or right):
      {Fore.LIGHTRED_EX}{Style.BRIGHT}[>] """);
  clicksPerPress = int(input(f"""    {Fore.RED}Enter the amount of clicks per mouse press:
      {Fore.LIGHTRED_EX}{Style.BRIGHT}[>] """));
  timeBetween = float(input(f"""    {Fore.RED}Enter time between each mouse press (0.010 Recommended):
      {Fore.LIGHTRED_EX}{Style.BRIGHT}[>] """));
  return { "mouseButton": mouseButton, "clicksPerPress": clicksPerPress, "timeBetween": timeBetween }

def logClick(inputs):
  clicksPerPress = inputs["clicksPerPress"]
  print(f"""    {Fore.RED}{Style.BRIGHT}[+] {time.ctime()}  {Style.RESET_ALL}{Fore.LIGHTRED_EX} {str(clicksPerPress)} Mouse Presses Simulated""")

def on_press(key):
  if any([key in COMBO for COMBO in COMBINATIONS]):
    current.add(key)
    if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
      # Cleanup
      cls()
      print(f"""{Fore.LIGHTRED_EX}
  ·▄▄▄▄        ▄• ▄▌▄▄▄▄· ▄▄▌  ▄▄▄ .     ▄▄▄·▄▄▄  ▄▄▄ ..▄▄ · .▄▄ · 
  ██▪ ██ ▪     █▪██▌▐█ ▀█▪██•  ▀▄.▀·    ▐█ ▄█▀▄ █·▀▄.▀·▐█ ▀. ▐█ ▀. 
{Fore.RED}  ▐█· ▐█▌ ▄█▀▄ █▌▐█▌▐█▀▀█▄██▪  ▐▀▀▪▄     ██▀·▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄
  ██. ██ ▐█▌.▐▌▐█▄█▌██▄▪▐█▐█▌▐▌▐█▄▄▌    ▐█▪·•▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█
  ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀ ·▀▀▀▀ .▀▀▀  ▀▀▀     .▀   .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀▀ 

{Fore.RED}{Style.BRIGHT}  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

    {Fore.RED}{Style.BRIGHT}[+] {Style.RESET_ALL}{Fore.LIGHTRED_EX}EXITED PROGRAM
{Style.RESET_ALL}""")

      # Stop listener
      if(mListen != ""):
        mListen.stop()

      # Exit
      os._exit(0)

  elif any([key in COMBO for COMBO in TOGGLE_COMBINATIONS]):
    current.add(key)
    if any(all(k in current for k in COMBO) for COMBO in TOGGLE_COMBINATIONS):
      if(mListen != ""):
        # Log Toggle
        print(f"""    {Fore.RED}{Style.BRIGHT}[+] {time.ctime()}  {Style.RESET_ALL}{Fore.LIGHTRED_EX} Program Toggled""")

        # Stop/Start listener
        global mEnabled
        if(mEnabled == True):
          mEnabled = False
          #mListen.stop()
          #while mEnabled == False:
          #  waitingStatement = 0
        else:
          mEnabled = True
          #startMouseListener()
        

def on_release(key):
  if any([key in COMBO for COMBO in COMBINATIONS]):
    current.remove(key)

def on_click(x, y, button, pressed):
  mouseButton = curr_inpts["mouseButton"]
  if mEnabled == True and button == mouse.Button[mouseButton]:
    mListen.stop()
    clicksPerPress = curr_inpts["clicksPerPress"]
    timeBetween = curr_inpts["timeBetween"]

    # Simulate Clicks
    global mControl
    for i in range(clicksPerPress):
      mControl.press(Button[mouseButton])
      time.sleep(0.005)
      mControl.release(Button[mouseButton])
      time.sleep(timeBetween)

    # Log Simulated Clicks
    logClick(curr_inpts)

    # Start Again
    startClicks(curr_inpts)

def startMouseListener():
  with mouse.Listener(on_click=on_click) as listener:
    global mListen
    mListen = listener
    listener.join()

def startClicks(inputs):
  # Setup
  clicksPerPress = inputs["clicksPerPress"]
  global curr_inpts
  curr_inpts = inputs

  # Setup Controller
  global mControl
  mControl = Controller()
  
  # Start Listener
  startMouseListener()

def startKeyListener():
  listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
  listener.start()


# Main code
def main():
  # Setup Quit Listener
  startKeyListener()

  # Get Inputs
  cls()
  banner()
  inputs = getInputs()

  # Log clicks
  cls()
  banner()
  startClicks(inputs)
  


# Check how it's being run
if __name__ == '__main__':
    main()