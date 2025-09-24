import pgzrun
import random

HEIGHT = 300
WIDTH = 500

pizza = Actor("pizza")
pizza.pos = (250,150)
caseoh = Actor("caseoh")
caseoh.pos = (0,0)

def draw():
    screen.fill("white")
    caseoh.draw()
    pizza.draw()

pgzrun.go()