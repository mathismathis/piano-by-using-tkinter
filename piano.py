from Tkinter import *
import pygame
pygame.init()

def buttonA():
  sound = pygame.mixer.Sound("sound/A.wav")
  sound.play()
def buttonB():
  sound = pygame.mixer.Sound("sound/B.wav")
  sound.play()
def buttonC():
  sound = pygame.mixer.Sound("sound/C.wav")
  sound.play()
def buttonD():
  sound = pygame.mixer.Sound("sound/D.wav")
  sound.play()
def buttonE():
  sound = pygame.mixer.Sound("sound/E.wav")
  sound.play()
def buttonF():
  sound = pygame.mixer.Sound("sound/F.wav")
  sound.play()
def buttonG():
  sound = pygame.mixer.Sound("sound/G.wav")
  sound.play()
def buttonH():
  sound = pygame.mixer.Sound("sound/H.wav")
  sound.play()
def buttonI():
  sound = pygame.mixer.Sound("sound/I.wav")
  sound.play()
def buttonJ():
  sound = pygame.mixer.Sound("sound/J.wav")
  sound.play()
def buttonK():
  sound = pygame.mixer.Sound("sound/K.wav")
  sound.play()
def buttonL():
  sound = pygame.mixer.Sound("sound/L.wav")
  sound.play()
def buttonM():
  sound = pygame.mixer.Sound("sound/M.wav")
  sound.play()
def buttonN():
  sound = pygame.mixer.Sound("sound/N.wav")
  sound.play()


root = Tk()
root.title("PIANO")
root.geometry("1050x700")

button= Button(root, bg="black", fg="red",text="A",command=buttonA,height=15 ,width=10)
button.grid(row=1,column=2)

button= Button(root, bg="black", fg="red",text="B",command=buttonB,height=15 ,width=10)
button.grid(row=1,column=3)

button= Button(root, bg="black", fg="red",text="C",command=buttonC,height=15,width=10)
button.grid(row=1,column=4)

button= Button(root, bg="black", fg="red",text="D",command=buttonD,height=15 ,width=10)
button.grid(row=1,column=5)

button= Button(root, bg="black", fg="red",text="E",command=buttonE,height=15 ,width=10)
button.grid(row=1,column=6)

button= Button(root, bg="black", fg="red",text="F",command=buttonF,height=15 ,width=10)
button.grid(row=1,column=7)

button= Button(root, bg="black", fg="red",text="G",command=buttonG,height=15 ,width=10)
button.grid(row=1,column=8)

button= Button(root, bg="black", fg="red",text="H",command=buttonH,height=20 ,width=15)
button.grid(row=5,column=2)

button= Button(root, bg="black", fg="red",text="I",command=buttonI,height=20 ,width=15)
button.grid(row=5,column=3)

button= Button(root, bg="black", fg="red",text="J",command=buttonJ,height=20 ,width=15)
button.grid(row=5,column=4)

button= Button(root, bg="black", fg="red",text="K",command=buttonK,height=20 ,width=15)
button.grid(row=5,column=5)

button= Button(root, bg="black", fg="red",text="L",command=buttonL,height=20 ,width=15)
button.grid(row=5,column=6)

button= Button(root, bg="black", fg="red",text="M",command=buttonM,height=20 ,width=15)
button.grid(row=5,column=7)

button= Button(root, bg="black", fg="red",text="N",command=buttonN,height=20 ,width=15)
button.grid(row=5,column=8)


root.mainloop()      


