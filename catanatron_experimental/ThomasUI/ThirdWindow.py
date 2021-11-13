from ctypes import sizeof
import os
from pickle import FALSE, TRUE
import PySimpleGUI as sg
import subprocess
import math
from ThomasUI import visuals

from humanfriendly import text


# Simple UI for catan
def GenerateResultsScreen(numOfGames,arrayOfPlayerTypes,avgPlayerVictoryPoints,playerWins,winningPlayer,numOfPlayers):

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
    leftPad = 0
    

    
    layout = [
    [sg.Text('Results: ')],
    
    #[sg.Text("",font=("Arial",25))],[sg.Image('/Users/thomashansknecht/Documents/catanatron/catanatron_experimental/ThomasUI/visuals/crown.png',pad=((leftPad,0),0))],
    [sg.Text('Player 1 is: ' + str(playerClass[0]),font=("Arial",25),pad=((50,0),0),text_color = playerColors[0])]+[sg.Text('Player 2 is: ' + str(playerClass[1]),font=("Arial",25),text_color = playerColors[1],pad=((150,10),20))],
    
    [sg.Text("Average Victory Points: " +str(avgPlayerVictoryPoints[0]),font=("Arial",30),text_color = playerColors[0],key=("player1VicPoints"),pad=((50,580),(0,10)))]+[sg.Text("Average Victory Points: " +str(avgPlayerVictoryPoints[1]),font=("Arial",30),text_color = playerColors[1],key=("player2VicPoints"))],
    [sg.Text('Player 3 is: ' + str(playerClass[2]),font=("Arial",25),pad=((50,0),0),text_color = playerColors[2])] + [sg.Text('Player 4 is: ' + str(playerClass[3]),font=("Arial",25),text_color = playerColors[3],pad=((550,10),20))],
    
    [sg.Text("Average Victory Points: " +str(avgPlayerVictoryPoints[2]),font=("Arial",30),text_color = playerColors[2],key=("player3VicPoints"),pad=((50,590),(0,10)))]+[sg.Text("Average Victory Points: " +str(avgPlayerVictoryPoints[3]),font=("Arial",30),text_color = playerColors[3],key=("player4VicPoints"))],
    
    [sg.Text("Graph of Player Wins",pad=(675,20),font=("Arial",45))],
    [sg.Graph(canvas_size=(800, 500), graph_bottom_left=(-20,-10), graph_top_right=(105,10*numOfGames), background_color='white', pad=(500,20),key='graph')],

    [sg.Button('Done',font=("Arial",40),pad=((170,70),(0,10)))]


    #[sg.Text("Number of Games Played:",font=("Arial",25),pad=((50,0),0))] +[sg.Text("Best Player:",font=("Arial",25),pad=((510,0),20))],
    #[sg.Text("",font=("Arial",25),key=("numOfGames"))]+[sg.Text("",font=("Arial",25),key=("bestPlayer"),pad=((510,0),(0,50)))]
    ]
                
                
                

    # Create the Window
    window = sg.Window('Settlers of Catan',layout, finalize=True)

    # Create our graph properties
    graph = window['graph']
    graph.DrawLine((-8,0), (600,0))    
    graph.DrawLine((-8,0), (-8,600))    

# Draw vertical axis key

    

    for x in range(0, int(numOfPlayers), 1):    
        graph.DrawLine((x*30,-3), (x*30,0))    
         
        graph.DrawText(str(playerClass[x])+ str(x+1), (x*30,-5), color=playerColors[x],font=("Arial",15))    


# Settings need to change depending on how many games were played. We need a setting for 0-4,5-20,21-50,51-100
# Draw horizontal axis key

    if numOfGames >= 4 and numOfGames <= 20:    
        for y in range(0, int(numOfGames)*3, int(numOfGames/3)):    
            graph.DrawLine((-3*80-30,y*3), (3*80-30,y*3))    
            
            graph.DrawText( y, (-15,y*3+1), color='blue',font=("Arial",20))    

        # Draw Graph    
    
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

GenerateResultsScreen(5,["RandomPlayer:RED","AlphaBetaPlayer:BLUE","BadPlayer:YELLOW","GreenPlayer:GREEN"],[5,10,15,20],[5,10,15,5],3,4)