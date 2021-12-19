import requests
import json
from tkinter import *
from turtle import Turtle, Screen

t = Turtle()
t.hideturtle()
screen = Screen()

def tela(r, g, b, mensagem):
    screen.setup(width=400, height=300)
    screen.bgcolor(#FCA311)
    screen.title('pyClima')
    screen.tracer(0)
    t.clear()
    t.goto(0, 250)
    t.color('white')
    t.clear()
    t.write('pyClima', align='center', font=('Comic Sans MS', 30, 'normal'))
    t.goto(0, -250)
    t.color('white')
    t.write(mensagem, align='center', font=('Comic Sans MS', 15, 'normal'))









screen.exitonclick()