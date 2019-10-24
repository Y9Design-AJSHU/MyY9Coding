from tkinter import Tk, Canvas, Frame, BOTH
root = Tk()	
canvas = Canvas()
points = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
canvas.create_polygon(points, outline='black', fill='white', width=3)
canvas.pack()
root.geometry()
root.mainloop()

