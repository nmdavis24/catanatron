import PySimpleGUI as sg
import numpy as np
from ctypes import sizeof
import os
from pickle import FALSE, TRUE
from humanfriendly import text


"""
    Embedding the Matplotlib toolbar into your application

"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
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
def GenerateResultsScreen(numOfGames,arrayOfPlayerTypes,avgPlayerVictoryPoints,totalVictoryPoints,playerWins,numOfPlayers):

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
            avgPlayerVictoryPoints[i] = (0)
        
    # Calculate best player based on avg Victory points + number of Games won (The index of that player will be defined from here)
    winnerIndex = 0
    maxPoints = 0
    p = 0
    for p in range(0,numOfPlayers):
        if int(playerWins[p]) + int(totalVictoryPoints[p]) > maxPoints:
            winnerIndex = p
            maxPoints = int(playerWins[p]) + int(totalVictoryPoints[p])

    # Now we need to check for more players with the same score
    print("Winner is Player: " + str(winnerIndex+1)+ " which is" + str(playerClass[winnerIndex]) )

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    leftPad = 0
    

    
    layout = [
    #[sg.Text("",font=("Arial",25))],[sg.Image('/Users/thomashansknecht/Documents/catanatron/catanatron_experimental/ThomasUI/visuals/crown.png',pad=((leftPad,0),0))],
    [sg.Text('Player 1 is: ' + str(playerClass[0]),font=("Arial",25),pad=((50,0),0),text_color = playerColors[0])]+[sg.Text('Player 2 is: ' + str(playerClass[1]),font=("Arial",25),text_color = playerColors[1],pad=((170,10),0))],
    
    [sg.Text("Average Victory Points: " +str(float(round(avgPlayerVictoryPoints[0],4))),font=("Arial",30),text_color = playerColors[0],key=("player1VicPoints"),pad=((50,100),(0,10)))]+[sg.Text("Average Victory Points: " +str(float(round(avgPlayerVictoryPoints[1],4))),font=("Arial",30),text_color = playerColors[1],key=("player2VicPoints"))],
    [sg.Text('Player 3 is: ' + str(playerClass[2]),font=("Arial",25),pad=((50,0),0),text_color = playerColors[2])] + [sg.Text('Player 4 is: ' + str(playerClass[3]),font=("Arial",25),text_color = playerColors[3],pad=((170,10),0))],
    
    [sg.Text("Average Victory Points: " +str(float(round(avgPlayerVictoryPoints[2],4))),font=("Arial",30),text_color = playerColors[2],key=("player3VicPoints"),pad=((50,100),(0,10)))]+[sg.Text("Average Victory Points: " +str(float(round(avgPlayerVictoryPoints[3],4))),font=("Arial",30),text_color = playerColors[3],key=("player4VicPoints"))],
    
    [sg.Button('Done',font=("Arial",40),pad=((430,0),(20,20)))]+[sg.Button('Graph Results',font=("Arial",40),pad=((10,0),(0,0)),key='result_But')],
    
    [sg.Text("",pad=((265,0),20),font=("Arial",45),key='graph_Header')],
    [sg.Canvas(key='controls_cv',pad=((305,0),0))],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(400 * 2, 400)
                       )]
        ],
        pad=((150,0), 0))],
    
       
    

    [sg.Text("",font=("Arial",25),pad=((200,0),0),key='plotPlayers1',text_color = playerColors[0])]+[sg.Text("",font=("Arial",25),pad=((55,0),0),key='plotPlayers2',text_color= playerColors[1])]+[sg.Text("",font=("Arial",25),pad=((60,0),0),key='plotPlayers3',text_color= playerColors[2])]+[sg.Text("",font=("Arial",25),pad=((60,0),0),key='plotPlayers4',text_color= playerColors[3])],
    [sg.Text("",font=("Arial",25),pad=((200,0),0),key='plotPlayerWins1',text_color = playerColors[0])]+[sg.Text("",font=("Arial",25),pad=((60,0),0),key='plotPlayerWins2',text_color= playerColors[1])]+[sg.Text("",font=("Arial",25),pad=((65,0),0),key='plotPlayerWins3',text_color= playerColors[2])]+[sg.Text("",font=("Arial",25),pad=((65,0),0),key='plotPlayerWins4',text_color= playerColors[3])],
    [sg.Text("Number of Games Played: "+str(numOfGames),font=("Arial",25),pad=((50,0),(30,30)))],
    [sg.Text("Best Overall Player was Player "+str(winnerIndex+1)+ " who is "+ str(playerClass[winnerIndex]) + " with " + str(totalVictoryPoints[winnerIndex])+ " total Victory Points",font=("Arial",25),pad=((50,0),20))],
    [sg.Text("and " + str(playerWins[winnerIndex]) + " total wins",font=("Arial",25),pad=((50,0),0))],
    [sg.Text("",font=("Arial",25),key=("numOfGames"))]+[sg.Text("",font=("Arial",25),key=("bestPlayer"),pad=((210,0),(0,50)))]
    ]
                
                
                
    # Create the Window
    window = sg.Window('Results for Settlers of Catan Simulation',layout, finalize=True)
   

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit') or event == "Done":  # always,  always give a way out!
            break
        
        
        # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        print ("Player Wins is " + str(playerWins))
        print ("Player Classes"+str(playerClass))

        j = 0
        # Make sure we have an int and not null character
        for j in range(0,len(playerWins)):
            if playerWins[j] == '':
                playerWins[j] = 0 
        # using list comprehension to
        # perform conversion
        test_list = [int(i) for i in playerWins]
        
        ax.bar([0,1,2,3],test_list,color=playerColors)
        ax.set_facecolor('lightGreen')
        #plt.grid()

        
        
            

        # ------------------------------- Instead of plt.show()
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        window['graph_Header'].Update("Graph of Player Wins")
        window['plotPlayers1'].Update("Player 1")
        window['plotPlayerWins1'].Update("(" + str(playerWins[0]) + " wins)")
        window['plotPlayers2'].Update("Player 2")
        window['plotPlayerWins2'].Update("(" + str(playerWins[1]) + " wins)")
        window['plotPlayers3'].Update("Player 3")
        window['plotPlayerWins3'].Update("(" + str(playerWins[2]) + " wins)")
        window['plotPlayers4'].Update("Player 4")
        window['plotPlayerWins4'].Update("(" + str(playerWins[3]) + " wins)")
        window['result_But'].Update("",visible=False)


#GenerateResultsScreen(5,["RandomPlayer:RED","AlphaBetaPlayer:BLUE","BadPlayer:YELLOW",""],[5.325353532325,4.3245357678,3.7896856554,''],[25,8,15,''],[1,2,6,4],3)