#import turtle
from tkinter import *
from turtle import *     #TurtleScreen,RawTurtle
tk = Tk()
t = Turtle()
ts = t.getscreen()
tk.geometry("800x600")
tk.resizable(height = False , width = False)
tk["bg"] = "green"

canvas = Canvas(tk,width = 700, height = 500).place(x = 20 , y = 10)
title =Label(canvas , text = "Turtle Race" , width = 20 , height = 1 , font = ("Agency FB" , 40)).place(x = 200 , y = 10)

'''def start():
	s1=TurtleScreen(canvas)
	#s1.bgcolor("white")
	
	p1 = RawTurtle(s1)
	
	p1.color("red")
	p1.shape("turtle")
	p1.up()
	p1.goto(-200,100)
	
start()
'''


tk.mainloop()



