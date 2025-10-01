

import pgzrun
import random

HEIGHT = 300
WIDTH = 500

message = ""


pizza = Actor("pizza")
pizza.pos = (250,150)
caseoh = Actor("caseoh")
caseoh.pos = (50,50)



def draw():
    screen.fill("white")
    caseoh.draw()
    pizza.draw()
    screen.draw.text(message,(0,0),color = "brown" , fontsize = 20 )

def update():
    global message
    if keyboard.a:
        caseoh.x -=20
    if keyboard.s:
        caseoh.y +=20
    if keyboard.d:
        caseoh.x +=20
    if keyboard.w:
        caseoh.y -=20
    if caseoh.colliderect(pizza):
        message = "nom"
        auto_pos()


        


def on_mouse_down(pos):
    global message
    if pizza.collidepoint(pos):
        message = "nom"
        
        auto_pos()



def auto_pos():
    pizza.y = random.randint(1,250)
    pizza.x = random.randint(1,450)
    


pgzrun.go()
