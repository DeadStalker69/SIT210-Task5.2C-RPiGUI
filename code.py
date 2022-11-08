from tkinter import *		
import tkinter.font
from gpiozero import LED as Red		    #using gpiozero module. this helps to its functions which are shorter and easier as compared to rpi.GPIO's functions. 
									    #import LED enables LED functions, like is_lit, off, on etc. 
from gpiozero import LED as Blue
from gpiozero import LED as Green
import RPi.GPIO						   

RPi.GPIO.setmode(RPi.GPIO.BOARD)	   #using GPIO naming convention

red = Red(14)						    #setting GPIO 14 for red LED
blue = Blue(15)					    #setting GPIO 15 for blue LED
green = Green(18)					    #setting GPIO 18 for green LED

win = Tk()							    #tkinter function to open a new window
win.title("Led Toggle")				    #giving a name to the window
win.configure(background='#e9f5e6')
win.geometry("450x390")
win.minsize(450,390)
Font = tkinter.font.Font(family = 'Calibri' , size = 12, weight = "bold")
									    #declaring a variable Font with specifications of font used throughout the GUI
def redToggle():						#defining redToggle command, used in redButton
	if red.is_lit:						#if case to find if the LED is on. Used only in case the button is pressed.
		red.off()						#once button is pressed, if the LEd is on, turn off the LED
		colour.configure(background = 'white')
		redButton["text"] = "Turn Red LED on"
										#and change the text visible on the button to Turn Red LED on.		
	else:
		blue.off()					#turn blue LED off if Red LED is off and button to turn Red LED on is pressed
		green.off()						#turn green LED off if Red LED is off and button to turn Red LED on is pressed
		red.on()						#turn red LED on if Red LED is off and button to turn Red LED on is pressed
		colour.configure(background = 'red')
		redButton["text"] = "Turn Red LED off"
										#change the text written on the button.


def blueToggle():
	if blue.is_lit:
		blue.off()
		colour.configure(background = 'white')
		blueButton["text"] = "Turn blue LED on"
	else:
		red.off()
		green.off()
		blue.on()
		colour.configure(background = 'blue')
		blueButton["text"] = "Turn blue LED off"


def greenToggle():
	if green.is_lit:
		green.off()
		colour.configure(background = 'white')
		greenButton["text"] = "Turn Green LED on"
	else:
		red.off()
		blue.off()
		green.on()
		colour.configure(background = 'green')
		greenButton["text"] = "Turn Green LED off"

def close():							#defining close command used in exit button and close button
	red.off()							#turning red LED off
	blue.off()						    #turning blue LED off
	green.off()							#turning green LED off
	win.destroy()						#closing the GUI window

redButton = Radiobutton(win, text = 'Turn Red LED on', font  = Font, command = redToggle, height=3, width = 24, indicatoron=0) 
										#definng various paramters of a declared button
redButton.place(x=30, y=30, in_=win)
										#definig the position of the button on the GUI window

blueButton = Radiobutton(win, text = 'Turn blue LED on', font  = Font, command = blueToggle, height=3, width = 24, indicatoron=0)  
blueButton.place(x=30, y=120, in_=win)

greenButton = Radiobutton(win, text = 'Turn Green LED on', bg = 'bisque2', font  = Font, command = greenToggle, height=3, width = 24, indicatoron=0)  
greenButton.place(x=30, y=210, in_=win) 

exitButton = Radiobutton(win, text = 'Exit', font  = Font, command = close, height=3, width = 24, indicatoron=0)  
exitButton.place(x=30, y=300, in_=win)

label = Button(win, text = 'The ON LED', height=1, width=7)
label.place(x=340, y=120, in_=win)

colour = Button(win,bg = 'white', height=3, width = 4)
colour.place(x=350, y=160, in_=win)

win.protocol("WM_DELETE_WINDOW", close)	#giving close function(defined earlier) to exit button
win.mainloop()							#creating a loop for the program
