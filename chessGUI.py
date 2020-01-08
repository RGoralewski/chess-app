from tkinter import *

#Window
mainWindow = Tk()
mainWindow.title("Chess App")
mainWindow.geometry('640x480')

#Description for textbox
description = Label(mainWindow, text="Player name: ", font=("Calibri", 10))
description.grid(column=0, row=0)

#Textbox to type player name
txt = Entry(mainWindow, width=10)
txt.grid(column=1, row=0)
txt.focus()

#List of players
players = []

#List of players' labels - to see already added players
pLabels = []

#Add player button - adds a player with a name from the
#textbox to the players list
def addPlayerClicked():
    players.append(txt.get())
    pLabels.append(Label(mainWindow, text=players[-1], font=("Calibri", 10)))
    pLabels[-1].grid(column=1, row=len(players))
addPlayerButton = Button(mainWindow, text="Add player", command=addPlayerClicked)
addPlayerButton.grid(column=2, row=0)

#Delete player button
def deletePlayerClicked():
    if players:
        players.pop()
    if pLabels:
        pLabels[-1].destroy()
        pLabels.pop()
deletePlayerButton = Button(mainWindow, text="Delete", command=deletePlayerClicked)
deletePlayerButton.grid(column=2, row=1)

#Mainloop
mainWindow.mainloop()
