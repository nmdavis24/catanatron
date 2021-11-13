import os
import PySimpleGUI as sg
import subprocess

# Simple UI for catan

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Game using default settings')],
            [sg.Text('Please specify the type of player for players 1,2,3, and 4')],
            [sg.Text('Options:')],
            [sg.Text('1. AlphaBeta - Oracle player AI')],
            [sg.Text('2. Human - Human Player ')],
            [sg.Text('3. BaseLine - A Base Line AI that picks moves randomly ')],
            [sg.Text('4. Custom1 - The first AI we made')],
            [sg.Text('5. Custom2 - The second custom AI we made')],
            [sg.Text('6. None - This player will not exist. At least 2 players must exist')],
            [sg.Text('Player 1:          '), sg.InputText()],
            [sg.Text('Player 2:          '), sg.InputText()],
            [sg.Text('Player 3:          '), sg.InputText("None")],
            [sg.Text('Player 4:          '), sg.InputText("None")],
            [sg.Text('Give Number of Games as 1,2,3,4,...n')],
            [sg.Text('Num of Games:'), sg.InputText("1")],
            
            [sg.Button('Start Game'), sg.Button('Cancel')] ]

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
                #Custom2 -- Not created yet

                
                
                
        print('You entered:', '\nPlayer1:', values[0], '\nPlayer2:', values[1], '\nPlayer3:', values[2], '\nPlayer4:', values[3])
    

        
        #rc = subprocess.call("catanatron-play --players=R,W,F,AB:2 --num=2")
        # This is the path on a Mac for Thomas
        os.system('/Users/thomashansknecht/opt/anaconda3/bin/catanatron-play --players=' + str(values[0]) +','+ str(values[1])+ ','+ str(values[2])+ ',' + str(values[3]) + ' --num=' + str(values[4])) 
        break

window.close()