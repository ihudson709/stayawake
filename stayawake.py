# Keep MS Windows Active. Prevent Screensaver from activating. Prevent Monitor from going to sleep.
# Developed by Ian Hudson 4/25/2022

import ctypes
import os
import pyautogui
import keyboard
import logging
import time

LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename = 'StayAwake.log', level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

# Display App Name, Credits, Eula and Copyrights
logger.info(' StayAwake - v2.0')
logger.info(' See readme.txt for more details, see EULA.txt for legal info.')
logger.info(' Icons made by www.freepik.com from www.flaticon.com.')
logger.info(' Developed by Ian Hudson (C)2022 All Rights Reserved.')

time.sleep(5)

pyautogui.FAILSAFE = False

def exitproc():
	ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
	ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )
	logger.debug('StayAwake has been deactivated.')
	os._exit(0)

# Create hotkey and it's funtion for exit processes 
keyboard.add_hotkey("ctrl+alt+x", lambda: exitproc()) # Disable the app by pressing: cntrl+alt+x
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
logger.debug('StayAwake is active.')

while(True):
	ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
	