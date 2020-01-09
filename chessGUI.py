from tkinter import *
import chessSetter

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
    txt.delete(0, END)
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

#Set matches button
def setMachesClicked():
    if len(players) > 1:
        #Create a new window for set matches
        matchesWindow = Tk()
        matchesWindow.title("Matches")
        matchesWindow.geometry('800x600')
        #Set matches
        matches = chessSetter.setMatches(players)
        #Display matches
        rowNum = 0
        for m in matches:
            lbl = Label(matchesWindow, text=str(rowNum + 1) + ". ")
            lbl.grid(column=0, row=rowNum)
            lbl = Label(matchesWindow, text=m[0])
            lbl.grid(column=1, row=rowNum)
            lbl = Label(matchesWindow, text=" - ")
            lbl.grid(column=2, row=rowNum)
            lbl = Label(matchesWindow, text=m[1])
            lbl.grid(column=3, row=rowNum)
            rowNum += 1

setMatchesButton = Button(mainWindow, text="Set matches!", command=setMachesClicked, bg="orange")
setMatchesButton.grid(column=3, row=0)

#Mainloop
mainWindow.mainloop()
