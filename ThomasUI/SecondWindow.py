import os
import PySimpleGUI as sg
import subprocess
import visuals

from humanfriendly import text
from PIL import Image, ImageFont, ImageDraw # we a re putting text over the image so we need this



# Simple UI for catan

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
[sg.Text('Results',font=("Arial",50),pad=(400,10))],
[sg.Text("",font=("Arial",25))],
[sg.Text(" Player 1: Victory Points:",font=("Arial",25))]+[sg.Button('Done',font=("Arial",40),pad=((140,20),(0,10)))]+[sg.Text("Player 2: Victory Points:",font=("Arial",25),pad=((130,10),20))],
[sg.Text("",font=("Arial",25),key=("player1VicPoints"))]+[sg.Text("",font=("Arial",25),key=("player2VicPoints"))],
[sg.Image('/Users/thomashansknecht/Documents/catanatron/ThomasUI/visuals/CatanBoard.png')],
[sg.Text("Player 3: Victory Points:",font=("Arial",25))] + [sg.Text("Player 4: Victory Points:",font=("Arial",25),pad=((400,10),20))],
[sg.Text("",font=("Arial",25),key=("player3VicPoints"))]+[sg.Text("",font=("Arial",25),key=("player4VicPoints"))],
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