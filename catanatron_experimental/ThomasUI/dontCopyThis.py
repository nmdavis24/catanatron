import PySimpleGUI as sg
import numpy as np
from ctypes import sizeof
import os
from pickle import FALSE, TRUE
import subprocess
import math
from humanfriendly import text


"""
    Embedding the Matplotlib toolbar into your application

"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


# ------------------------------- PySimpleGUI CODE



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
    
    [sg.Text("",pad=(675,20),font=("Arial",45),key='graph_Header')],
    
    [sg.Button('Done',font=("Arial",40),pad=((370,70),(0,10)))],
    [sg.Button('Show Results',font=("Arial",40),pad=((370,70),(0,10)))],
    [sg.Canvas(key='controls_cv',pad=(600,0))],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(400 * 2, 400)
                       )]
        ],
        pad=(500, 50)
    )],


    #[sg.Text("Number of Games Played:",font=("Arial",25),pad=((50,0),0))] +[sg.Text("Best Player:",font=("Arial",25),pad=((510,0),20))],
    #[sg.Text("",font=("Arial",25),key=("numOfGames"))]+[sg.Text("",font=("Arial",25),key=("bestPlayer"),pad=((510,0),(0,50)))]
    ]
                
                
                
    # Create the Window
    window = sg.Window('Settlers of Catan',layout, finalize=True)
   

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit') or event == "Done":  # always,  always give a way out!
            break
        
        
        # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(playerClass,playerWins,color=playerColors)
        plt.grid()
            

        # ------------------------------- Instead of plt.show()
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        window['graph_Header'].Update("Graph of Player Wins")


#GenerateResultsScreen(5,["RandomPlayer:RED","AlphaBetaPlayer:BLUE","BadPlayer:YELLOW","GreenPlayer:GREEN"],[5,10,15,20],[5,10,15,5],3,4)