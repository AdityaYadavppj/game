import turtle 
import tkinter as tk
from tkinter import messagebox as msg
#from tkinter import *
#from turtle import *     #TurtleScreen,RawTurtle


root = tk.Tk()
root.resizable(height = False , width = False)
root.geometry("1000x600")
root["bg"] = "green"
canvas = tk.Canvas(master = root , width = 1400, height = 1000)
canvas.pack()
title =tk.Label(canvas , text = "Turtle Race" , width = 20 , height = 1 , font = ("Agency FB" , 40)).place(x = 0 , y = 10)

chance = ""

def start():
# for player 1
	
	p1 = turtle.RawTurtle(canvas)
	
	p1.color("red")
	p1.shape("turtle")
	p1.up()
	p1.goto(-400,200)
	p1.goto(400,200)
	p1.down()
	p1.circle(40)
	p1.up()
	p1.goto(-400,210)
	
# for player 2
	
	p2 = p1.clone()
	
	p2.color("black")
	p2.shape("turtle")
	p2.up()
	p2.goto(-400,0)
	p2.goto(400,0)
	p2.down()
	p2.circle(40)
	p2.up()
	p2.goto(-400,10)
	
	
	import random
	
	die = [1,2,3,4,5,6]
	def play():
		for i in range(20):
			global chance
			if chance != "A":
				chance = "A"
				if p1.pos()>=(400,200):
					print("Player 1 is win ")
					root.destroy()
					root2 = tk.Tk()
					
					root2.title("Congratulation")
					root2.geometry("400x100")
					root2["bg"] = "yellow"
					tk.Label(root2,text ="Player 2 win this game",font =  ("Agency FB" , 20) , bg = "green" , fg = "red").place(x = 500 , y = 500)
					break
				else:			
					dei2 = random.choice(die)
					p1.fd(20*dei2)
					break
				
		"""		else:
					msg.showwarming("Alert" , "It's not your chance")
					break"""
				
	           

	def play2():
	 	for i in range (20):
	 		global chance
	 		if chance != "B":
	 			chance = "B"
	 			
	 			if p2.pos()>= (400,0):
	 				print("player 2 win this game ")
	 				root.destroy()
	 				root2 = tk.Tk()
	 				root2.title("congralations")
	 				root2.geometry("400x200")
	 				root2["bg"] = "yellow"
	 				tk.Label(root2,text ="Player 2 win this game",font =  ("Agency FB" , 20) , bg = "green" , fg = "red").place(x = 500 , y = 500)
	 				break
	 			else:
	 				dei2 = random.choice(die)
	 				p2.fd(20*dei2)
	 		"""	else:
	 				msg.showwarming("Alert" , "It's not your chance")
	 				break"""
	player1 = tk.Button(canvas , text = "Player 1" , bg = "green" , fg = "white" , command = play2).place(x = 220 , y = 800)
	player2 = tk.Button(canvas , text = "Player 2" , bg = "green" , fg = "white" , command = play).place(x = 500 , y = 800)	
	 				
	 			
	 			
	 		
	 	
start()


tk.mainloop()



