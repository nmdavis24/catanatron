import os
from pickle import FALSE, TRUE
import PySimpleGUI as sg
import subprocess
import ThomasUI
from ThomasUI.SecondWindow import GenerateEndScreen

from humanfriendly import text

# Simple UI for catan

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Define Game Rules',font=("Arial",25))],[sg.Radio('Default     ', "RADIO1", default=True, size=(10,1)), sg.Radio('Custom', "RADIO1")],
            [sg.Text('Please specify the type of player for players 1,2,3, and 4',font=("Arial",15))],
            [sg.Text('Options:',font=("Arial",15))],
            [sg.Text('1. AlphaBeta - Oracle player AI',font=("Arial",15))],
            [sg.Text('2. Human - Human Player ',font=("Arial",15))],
            [sg.Text('3. BaseLine - A Base Line AI that picks moves randomly ',font=("Arial",15))],
            [sg.Text('4. Custom1 - The first AI we made',font=("Arial",15))],
            [sg.Text('5. Custom2 - The second custom AI we made',font=("Arial",15))],
            [sg.Text('6. None - This player will not exist. At least 2 players must exist',font=("Arial",15))],
            
            [sg.Text('Player 1:     ',font=("Arial",15)), sg.InputCombo(('AlphaBeta', 'Human', 'BaseLine','Custom1','Custom2'), default_value = 'AlphaBeta',size=(20, 5))],
            [sg.Text('Player 2:     ',font=("Arial",15)), sg.InputCombo(('AlphaBeta', 'Human', 'BaseLine','Custom1','Custom2'), default_value = 'BaseLine',size=(20, 5))],
            [sg.Text('Player 3:     ',font=("Arial",15)), sg.InputCombo(('None','AlphaBeta', 'Human', 'BaseLine','Custom1','Custom2'),default_value = 'None', size=(20, 5))],
            [sg.Text('Player 4:     ',font=("Arial",15)), sg.InputCombo(('None','AlphaBeta', 'Human', 'BaseLine','Custom1','Custom2'),default_value = 'None', size=(20, 5))],
            [sg.Text('Give Number of Games as 1,2,3,4,...100',font=("Arial",15))],
            [sg.Text('Num of Games:',font=("Arial",15)), sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=1)],
            [sg.Text('',font=("Arial",15))],
            [sg.Button('Start Game',font=("Arial",15)), sg.Button('Cancel',font=("Arial",15))] ]

# Create the Window
window = sg.Window('Settlers of Catan', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if event == 'Start Game':
        options = ["AlphaBeta", "Human", "BaseLine", "Custom1", "Custom2"]
        index = 0
        i = 0
        j = 0
        for i in range (0, len(values)):
            for option in options:
            
                if (values[i] == options[0]): #Alphabeta player
                    values[i] = "AB"
                elif (values[i] == options[1]): #Human player
                    values[i] = "H" 
                elif (values[i] == options[2]): #Base Line player -- Random Player
                    values[i] = "R"
                elif (values[i] == options[3]): #Custom1 -- Custom AI
                    values[i] = "Y"
                elif (values[i] == options[4]): #Custom2 -- Not created yet
                    values[i] = "None"
                

                
                
                
        print('You entered:', '\nPlayer1:', values[2], '\nPlayer2:', values[3], '\nPlayer3:', values[4], '\nPlayer4:', values[5])
    

        
        #rc = subprocess.call("catanatron-play --players=R,W,F,AB:2 --num=2")
        # This is the path on a Mac for Thomas
        window.close()
        window.close()
        window.close()
        os.system('/Users/thomashansknecht/opt/anaconda3/bin/catanatron-play --players=' + str(values[2]) +','+ str(values[3])+ ','+ str(values[4])+ ',' + str(values[5]) + ' --num=' + str((int(values[6])))) 

        break

window.close()