# =========================================================
# A script that allows players to automate procedures
# in Digimon Heroes (played in an emulator on PC)
# Written by: Ian Wong
# =========================================================

import pyautogui
import time
import dhbotfunctions

# FUNCTIONS
# ------------------------------
# Obtain screen info: top left corner, width, height
def getScreenInfo():
	print 'Analysing screen dimensions...'
	analysis1 = pyautogui.locateOnScreen('images/analysis_1.png')
	analysis2 = pyautogui.locateOnScreen('images/analysis_2.png')

	screen_x = analysis1[0]
	screen_y = analysis1[1]
	screen_width = analysis2[0] + analysis2[2] - analysis1[0]
	screen_height = analysis2[1] + analysis2[3] - analysis1[1]
	
	return (screen_x, screen_y, screen_width, screen_height)
	
# Displays a welcome message
def displayWelcomeMessage():
	print " =================================="
	print " DIGIMON HEROES AUTOMATION SCRIPT"
	print " =================================="
	print ""
	
# MAIN
# ------------------------------
if (__name__ == '__main__'):

	# Obtain screen info
	screen_info = getScreenInfo()
	
	# Begin user interactivity
	displayWelcomeMessage()
	while True:
		user_input = raw_input(' > ')
		print "Running function %s..." % user_input
		
		# Check for exit command
		if (user_input == 'exit'):
			print "Exiting..."
			exit()
		
		# Execute other commands
		try:
			dhbotfunctions.commands[user_input](screen_info)
		except KeyError:
			print "Error: No valid command '%s'" % user_input
