from tkinter import *		
import tkinter.font
from gpiozero import LED as Red		    #using gpiozero module. this helps to its functions which are shorter and easier as compared to rpi.GPIO's functions. 
									    #import LED enables LED functions, like is_lit, off, on etc. 
from gpiozero import LED as Yellow
from gpiozero import LED as Green
import RPi.GPIO						   

RPi.GPIO.setmode(RPi.GPIO.BOARD)	   #using GPIO naming convention

red = Red(14)						    #setting GPIO 14 for red LED
yellow = Yellow(15)					    #setting GPIO 15 for yellow LED
green = Green(18)					    #setting GPIO 18 for green LED

win = Tk()							    #tkinter function to open a new window
win.title("Led Toggle")				    #giving a name to the window
Font = tkinter.font.Font(family = 'Calibri' , size = 12, weight = "bold")
									    #declaring a variable Font with specifications of font used throughout the GUI
def redToggle():						#defining redToggle command, used in redButton
	if red.is_lit:						#if case to find if the LED is on. Used only in case the button is pressed.
		red.off()						#once button is pressed, if the LEd is on, turn off the LED
		redButton["text"] = "Turn Red LED on"
										#and change the text visible on the button to Turn Red LED on.		
	else:
		yellow.off()					#turn yellow LED off if Red LED is off and button to turn Red LED on is pressed
		green.off()						#turn green LED off if Red LED is off and button to turn Red LED on is pressed
		red.on()						#turn red LED on if Red LED is off and button to turn Red LED on is pressed
		redButton["text"] = "Turn Red LED off"
										#change the text written on the button.


def yellowToggle():
	if yellow.is_lit:
		yellow.off()
		yellowButton["text"] = "Turn Yellow LED on"
	else:
		red.off()
		green.off()
		yellow.on()
		yellowButton["text"] = "Turn Yellow LED off"


def greenToggle():
	if green.is_lit:
		green.off()
		greenButton["text"] = "Turn Green LED on"
	else:
		red.off()
		yellow.off()
		green.on()
		greenButton["text"] = "Turn Green LED off"

def close():							#defining close command used in exit button and close button
	red.off()							#turning red LED off
	yellow.off()						#turning yellow LED off
	green.off()							#turning green LED off
	win.destroy()						#closing the GUI window

redButton = Button(win, text = 'Turn Red LED on', font  = Font, command = redToggle, bg = 'red', height = 1, width = 24) 
										#definng various paramters of a declared button
redButton.grid(row=0, column=1)
										#definig the position of the button on the GUI window

yellowButton = Button(win, text = 'Turn Yellow LED on', font  = Font, command = yellowToggle, bg = 'yellow', height = 1, width = 24)  
yellowButton.grid(row=1, column=1)

greenButton = Button(win, text = 'Turn Green LED on', font  = Font, command = greenToggle, bg = 'green', height = 1, width = 24)  
greenButton.grid(row=2, column=1)

exitButton = Button(win, text = 'Exit', font  = Font, command = close, bg = 'blue', height = 1, width = 24)  
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)	#giving close function(defined earlier) to exit button
win.mainloop()							#creating a loop for the program