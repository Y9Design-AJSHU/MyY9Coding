from tkinter import *
from tkinter import Entry
from tkinter.ttk import Progressbar
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter import simpledialog

#Understand

#VARIABLES*****************
#Caution: You have to use lists.  Using individual variables you get access issues. 

data = []

calsGoal = 2000
rFile = open("data.txt", "r")
rFile2 = open("cals.txt", "r")
cals = float(rFile2.read())
data = rFile.read().split("\n")

for i in range(0, len(data),1):
	data[i] = float(data[i]) #casting 
		
print(data)

#FUNCTIONS ****************

#Step 1: Bind this function to an action

def weigthRunMe():

	#Step 2:  Access and then clear widget
	value = weightEntry.get()
	print(value)	
	weightEntry.delete(0, 'end')


	#Step 3: Append value to the list
	data.append(float(value))
	
	c.delete("all")


		
	#Step 4: Update display	
	chartUpdate()
	
	
def chartUpdate():
	
	#These are local variables only needed inthis function.
	#bar graph
	y_stretch = 1
	y_gap = 20
	x_stretch = 0
	x_width = 36
	x_gap = 20
	print(len(data))
	ctr = 0
	for i in range(len(data) - 1 - 10, len(data),1):
		x0 = (ctr) * x_stretch + (ctr) * x_width + x_gap
		y0 = 220 - (data[i] * y_stretch + y_gap)
		x1 = ctr * x_stretch + ctr * x_width + x_width + x_gap
		y1 = 220 - y_gap
		c.create_rectangle(x0-18, y0, x1-18, y1, fill="#ff8f00")
		c.create_text(x0-15, y0, anchor='sw', text=str(int(data[i])), font=("Purisa", 18), fill='white')
		ctr = ctr + 1
#Step 1: Bind this function to an action	

def calsRunMe():
	global cals
	#Step 2:  Access widget
	value1 = float(calsEntry.get())
	print(value1)	
	
	#Step 3: Add to Variable
	cals+=value1
	#Step 4: Update display	
	bar['value'] = float(cals)/float(calsGoal)*100
	barValue = float(cals)/float(calsGoal)*100
	label['text'] = str(int(round(barValue,0)))+'%'
	calsEntry.delete(0, 'end')


def on_closing():
	if messagebox.askokcancel("Save", "Would you like to save the data inputted?"):
		#This is where you write to the file
		wFile = open("data.txt", "w")
		for i in range(0, len(data)-1,1):
			wFile.write(str(data[i])+"\n")
		for i in range(len(data)-1, len(data),1):
			wFile.write(str(data[i]))
		wFile.close()
		wFile2 = open("cals.txt", "w")
		wFile2.write(str(cals))
		wFile2.close()
		root.destroy()

#GUI SETUP ROOT1 *****************
root = Tk()
style = ttk.Style()
style.theme_use('default')

#styling
style.configure("orange.horizontal.TEntry", foreground='#ff8f00')
style.configure("orange.TButton", background='#ff8f00', font=("Purisa", 20))
style.configure("orange.Horizontal.TProgressbar", background='#ff8f00')
style.configure("transp.TLabel", font=("Purisa", 20), foreground='black' )
#canvas
c = Canvas(root, background='#8b0000', highlightthickness=3, highlightbackground="black", width=390)
c.grid(row=3,column=1, columnspan=5, pady=3)

#progress bar
bar = Progressbar(length=390, style='orange.Horizontal.TProgressbar')
bar.grid(row=5, column=1, columnspan=3, pady=10, padx=10, sticky=E+W+N+S)
bar['value']=cals/calsGoal*100
#label on progress bar

label=Label(root, text = str(int(bar['value']))+"%", style = 'transp.TLabel')
label.grid(row=5, column=2, pady=10, padx=10, sticky=W)

chartUpdate();

#Button that submits the weight

weightButton = Button(root, text="Submit Weight", style='orange.TButton', command = weigthRunMe)
weightButton.grid(row=2, column=1)

#Type your weight here
weightEntry = Entry(root, width=15,style='orange.horizontal.TEntry',font=("Purisa", 20))
weightEntry.grid(row=1, column=1, padx = 10, pady=10)


#Button that submits the calories

calsButton = Button(root, text="Submit Calories", style='orange.TButton', command = calsRunMe)
calsButton.grid(row=2, column=3)

#Type your cals here
calsEntry = Entry(root, width=15,style='orange.horizontal.TEntry',font=("Purisa", 20))
calsEntry.grid(row=1, column=3, padx=10, pady=10);

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
