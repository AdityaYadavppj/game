import turtle
import tkinter as tk
from tkinter import messagebox as msg
from turtle import TurtleScreen,RawTurtle

win = tk.Tk()
win.geometry ("800x600")
win.resizable(width = False , height = False )
win.title("______TURTLE RACE _____")
win["bg"] = "green"
canvas = tk.Canvas(win,width = 750 , height = 455)
canvas.place(x = 20 ,y = 10)
title = tk.Label(canvas , text = "___TURTLE RACE___" , width = 20 ,height =1,font = ("Agency FB" , 40))
title.place(x = 200 , y = 10)
title2 = tk.Label(canvas , text = "Made by Aditya_Raj_Yadav" , width = 50 , height = 1 , font = ("Agency FB" , 30)).place(x =0, y =400)

chance = ""
def start():
    s1 = TurtleScreen(canvas)
    s1.bgcolor("white")

    p1 = RawTurtle(s1)

    p1.color("red")
    p1.shape("turtle")
    p1.up()
    p1.goto(-200,100)
    


    p2 = p1.clone()
    p2.color("black")
    p2.shape("turtle")
    p2.up()
    p2.goto(-200,-100)

    p1.goto(300 , 60)
    p1.down()
    p1.circle(40)
    p1.up()
    p1.goto(-200,100)
    

    p2.goto(300 , -140)
    p2.down()
    p2.circle(40)
    p2.up()
    p2.goto(-200,-100)


    import random

    die = [1,2,3,4,5,6]

    def play():
        for i in range (20):
            global chance
            if chance != "A":
                chance = "A"
                if p1.pos()>=(300,50):
                    print("_PLAYER_ONE_WINS_")
                    win.destroy()
                    win2 = tk.Tk()

                    win2.title("CONGRATULATIONS")
                    win2.geometry("400x100")
                    win2["bg"] = "yellow"
                    tk.Label(win2 , text = "_PLAYER_ONE_WIN_THIS_GAME_" , font = ("Agency FB" , 30) , bg = "white" , fg = "red").place(x = 10 , y = 30)

                    break
                else:

                    die_outcome = random.choice(die)
                    p1.fd(20*die_outcome)
                    #print("")

            else:
                   msg.showwarning("ALERT","IT NOT YOUR CHANCE")
            break
    def play2():
        for i in range (20):
            global chance
            if chance != "B":
                chance = "B"
                if p2.pos()>=(300,-50):
                    print("_PLAYER_TWO_WINS_")
                    win.destroy()
                    win2 = tk.Tk()

                    win2.title("CONGRATULATIONS")
                    win2.geometry("400x200")
                    win2["bg"] = "yellow"
                    tk.Label(win2 , text = "_PLAYER_TWO_WIN_THIS_GAME_" , font = ("Agency FB" , 30) , bg = "white" , fg = "red").place(x = 10 , y = 30)

                    break
                else:

                    die_outcome = random.choice(die)
                    p2.fd(20*die_outcome)
                    #print("")

            else:
                   msg.showwarning("ALERT","IT NOT YOUR CHANCE")
            break
    player1 = tk.Button(canvas,text = "Player 1", bg = "green" , fg = "white" , activeforeground = "yellow" ,
                         font = ("Agency FB" , 18),relief = "ridge" , width = 8 , height = 1 ,command = play)
    player1.place(x = 120 , y = 420)
    player2 = tk.Button(canvas,text = "Player 2", bg = "green" , fg = "white" , activeforeground = "yellow" ,
                         font = ("Agency FB" , 18),relief = "ridge" , width = 8 , height = 1 ,command = play2)
    player2.place(x = 550 , y = 420)

start = tk.Button(canvas,text = "START", bg = "green" , fg = "white" , activeforeground = "yellow" ,
                         font = ("Agency FB" , 18),relief = "ridge" , width = 8 , height = 1 ,command = start)
stop = tk.Button(canvas,text = "STOP", bg = "green" , fg = "white" , activeforeground = "yellow" ,
                         font = ("Agency FB" , 18),relief = "ridge" , width = 8 , height = 1 ,command =win.destroy)
start.place(x = 118 , y = 20)
stop.place (x = 606 , y = 20)

    



    
    
