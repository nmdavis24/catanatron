from ctypes import sizeof
import os
from pickle import FALSE, TRUE
import PySimpleGUI as sg
import subprocess
from ThomasUI import visuals

from humanfriendly import text
from PIL import Image, ImageFont, ImageDraw # we a re putting text over the image so we need this



# Simple UI for catan
def GenerateEndScreen(GameNum,playerVictoryPoints,arrayOfPlayerTypes):

    playerColors = ['','','','']
    playerClass = ['','','','']
    print (arrayOfPlayerTypes)
    
    for i in range(0,len(arrayOfPlayerTypes)):
        if (arrayOfPlayerTypes[i] != ''):
            currentline = arrayOfPlayerTypes[i].split(":")
            playerClass[i] = currentline[0]
            playerColors[i] = currentline[1]

            # The colors can sometimes includ a bunch of additional info so we need to trim that off
            badSymbol = "("
            if badSymbol in playerColors[i]:
                fullLine = playerColors[i].split("(")
                playerColors[i] = fullLine[0] 
        else:
            # We can not change a color to nothing so we need to catch any non existent players and give them a color
            playerColors[i] = "white"
            playerClass[i] = "Nothing"
        
    print("Player Classes: " + str(playerClass))
    print("Player Colors: " + str(playerColors).lower())

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
    [sg.Text('Game: ' + str(GameNum),font=("Arial",50),pad=(400,10))],
    [sg.Text("",font=("Arial",25))],
    [sg.Text('Player 1 is: ' + str(playerClass[0]),font=("Arial",25),text_color = playerColors[0])]+[sg.Button('Done',font=("Arial",40),pad=((140,20),(0,10)))]+[sg.Text('Player 2 is: ' + str(playerClass[1]),font=("Arial",25),text_color = playerColors[1],pad=((130,10),20))],
    
    [sg.Text(str(playerVictoryPoints[0]),font=("Arial",40),text_color = playerColors[0],key=("player1VicPoints"),pad=((65,690),(0,10)))]+[sg.Text(str(playerVictoryPoints[1]),font=("Arial",40),text_color = playerColors[1],key=("player2VicPoints"))],
    
    [sg.Image('/Users/thomashansknecht/Documents/catanatron/catanatron_experimental/ThomasUI/visuals/CatanBoard.png')],    
    [sg.Text('Player 3 is: ' + str(playerClass[2]),font=("Arial",25),text_color = playerColors[2])] + [sg.Text('Player 4 is: ' + str(playerClass[3]),font=("Arial",25),text_color = playerColors[3],pad=((400,10),20))],
    
    [sg.Text(str(playerVictoryPoints[2]),font=("Arial",40),text_color = playerColors[2],key=("player3VicPoints"),pad=((65,690),(0,10)))]+[sg.Text(str(playerVictoryPoints[3]),font=("Arial",40),text_color = playerColors[3],key=("player4VicPoints"))],
    
    [sg.Text("Number of Games Played:",font=("Arial",25))] +[sg.Text("Best Player:",font=("Arial",25),pad=((370,0),20))],
    [sg.Text("",font=("Arial",25),key=("numOfGames"))]+[sg.Text("",font=("Arial",25),key=("bestPlayer"),pad=((0,0),(0,50)))]
    ]
                
                
                

    # Create the Window
    window = sg.Window('Settlers of Catan',layout)


    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Done': # if user closes window or clicks cancel
            break
        
        #if event == 'Start Game':
            
                    
                    
            #print('You entered:', '\nPlayer1:', values[2], '\nPlayer2:', values[3], '\nPlayer3:', values[4], '\nPlayer4:', values[5])
        

            
            #rc = subprocess.call("catanatron-play --players=R,W,F,AB:2 --num=2")
            # This is the path on a Mac for Thomas
            #break

    window.close()

