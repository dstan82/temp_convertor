from tkinter import *

#define functions

#convert fahrenheit to celsius and kelvin
def convert_fahr():

	words = fbtext.get()
	ftemp = float(words)
	celbox.delete(0, END)
	celbox.insert(0, "%.2f" % (ftoc(ftemp)))
	kelbox.delete(0, END)
	kelbox.insert(0, "%.2f" % (ctok(ftoc(ftemp))))
	return

#convert celsius to fahrenheit

def convert_cel():

	words = cbtext.get()
	ctemp = float(words)
	fahrbox.delete(0, END)
	fahrbox.insert(0, "%.2f" % (ctof(ctemp)))
	kelbox.delete(0, END)
	kelbox.insert(0, "%.2f" % (ctok(ctemp)))

#convert kelvin to C and F
def convert_kel():

	words = kbtext.get()
	ktemp = float(words)
	fahrbox.delete(0, END)
	fahrbox.insert(0, "%.2f" % (ctof(ktoc(ktemp))))
	celbox.delete(0, END)
	celbox.insert(0, "%.2f" % (ktoc(ktemp)))

def ftoc(fahr):
	return (fahr-32) * 5 / 9

def ctof(cel):
	return cel * 9 / 5 + 32

def ktoc(kel):
	return kel - 273.15

def ctok (cel):
	return cel + 273.15

w=Tk() #Starting the tk interpreter from tkinter
w.title("Temperature Converter")

#Labels
fahrlabel = Label(w, text = "Fahrenheit")
fahrlabel.grid(row = 0, column = 0, padx = 25, pady = 25)

cellabel = Label(w, text = "Celsius")
cellabel.grid(row = 1, column = 0, padx = 25, pady = 25)

kellabel = Label(w, text = "Kelvin")
kellabel.grid(row = 2, column = 0, padx = 25, pady = 25)

exitbutton = Button(w, text = "Exit", command = quit)
exitbutton.grid(row = 3, column = 0, padx = 25, pady = 25, columnspan = 3)

#Entry Boxes

fbtext = StringVar()
fbtext.set("")
fahrbox=Entry(w,textvariable=fbtext)
fahrbox.grid(row=0, column=1, padx=25, pady=25)

cbtext = StringVar()
cbtext.set("")
celbox=Entry(w,textvariable=cbtext)
celbox.grid(row=1, column=1, padx=25, pady=25)

kbtext = StringVar()
kbtext.set("")
kelbox=Entry(w,textvariable=kbtext)
kelbox.grid(row=2, column=1, padx=25, pady=25)

fgobutton = Button(w, text = "Go", command = convert_fahr)
fgobutton.grid(row = 0 , column = 2, padx=25, pady =25)

fgobutton = Button(w, text = "Go", command = convert_cel)
fgobutton.grid(row = 1 , column = 2, padx=25, pady =25)

fgobutton = Button(w, text = "Go", command = convert_kel)
fgobutton.grid(row = 2 , column = 2, padx=25, pady =25)

w.mainloop()
