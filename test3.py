"""
Chess database
Justin Choi and Alex Lou
15 March 2023
IDT
Period 3
"""
#External Libraries
import tkinter as tk
from tkinter import messagebox
from masterProject.player import Player
from masterProject.playerDB import PlayerDB
from masterProject.game import Game
from masterProject.gameDB import GameDB
from PIL import ImageTk, Image

#Creating the Chess board
from masterProject.chessGame import ChessGame
from masterProject.chessGUI import ChessGUI


#Here the Game and Player DB are mixed into one
class ChessController:

    def __init__(self):
        
#Player Values
        self.currentPlayer = 0
        self.player = Player()
        self.midInsert = False
        self.answer = ""
        self.connection = False
        self.playerDB = PlayerDB()
        
#Game values
        self.gameDB = GameDB(self.playerDB)
        self.game = Game()
        self.currentGame = 0
        self.midInsert2 = 0
        #set the main window
        self.mainWin = tk.Tk()
        self.mainWin.geometry('1500x1000')
        self.mainWin.title("Chess Statistics")
        
        # create main frame
        # self.mainFrame = tk.Frame(self.mainWin, width = 800, height = 800)
        # self.mainFrame.grid(row = 0, columnspan = 2)
         
        #Setting the player Frame
        self.playerFrame = tk.Frame(self.mainWin, width = 700, height = 1000)
        self.playerFrame.grid(row = 0, column = 0)
        
        # Set the game Frame
        self.gameFrame = tk.Frame(self.mainWin, width = 700, height = 800)
        self.gameFrame.grid(row = 0, column = 1)
        
        #Setting the icon of the window
        self.ico = Image.open('/Users/imatable/SchoolPy/chess.ico')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.mainWin.wm_iconphoto(False, self.photo)
        
        #Game Image
        # self.gameImage = tk.PhotoImage(file = 'asd')
        # self.canvas = tk.Canvas(self.playerFrame, width = 800, height= 800)
        # self.canvas.place(x=800, y = 0)
        # self.canvas.create_image(800, 0, image = self.gameImage, anchor = "nw")
        
        #Player Image   
        self.chessImage = tk.PhotoImage(file='/Users/imatable/Downloads/bg.png')
        self.canvas = tk.Canvas(self.playerFrame, width=1500, height=1000)
        self.canvas.place(x= 0,y=  0)
        self.canvas.create_image(0, 0, image=self.chessImage, anchor="nw")
        
        
        
#File Section
        #Setting the menu bar at the top left 
        
        #File, About, etc.
        self.menubar = tk.Menu(self.mainWin)
        
        # File menu
        self.connectMenu = tk.Menu(self.menubar, tearoff = 0)
        self.connectMenu.add_command(label = "Connect", command = lambda: [self.connectionManager("connect")])
        self.connectMenu.add_command(label = "Disconnect", command = lambda: [self.connectionManager("noconnect")]) 
        
        # Separates the exit with a line
        self.connectMenu.add_separator()

        # file and exit
        self.connectMenu.add_command(label = "Exit", command = self.confirm_exit)
        self.menubar.add_cascade(label = "File", menu = self.connectMenu)

        #record menu
        self.recordMenu = tk.Menu(self.menubar, tearoff = 0)
        self.recordMenu.add_command(label = "New", command = self.add)
        self.recordMenu.add_command(label = "Save Changes", command = self.update)
        
        self.recordMenu.add_separator()
        
        self.recordMenu.add_command(label = "Delete All", command = self.showConfirmAlert3)
        self.menubar.add_cascade(label = "Edit", menu = self.recordMenu)

#ADDD BOTH GAMES
        #navigation menu
        self.navMenu = tk.Menu(self.menubar, tearoff = 0)
        self.navMenu.add_command(label = "Player", command = lambda: [self.nav("player")])
        self.navMenu.add_command(label = "Game", command = lambda: [self.nav("game")])
        self.menubar.add_cascade(label = "Navigation", menu = self.navMenu)
        

        #help menu
        self.helpMenu = tk.Menu(self.menubar, tearoff = 0)
        self.helpMenu.add_command(label = "Directions", command= self.help)
        self.helpMenu.add_command(label = "About", command = self.about)
        self.menubar.add_cascade(label = "Help", menu = self.helpMenu)

        #Set Frame to hold the player stats
        
        self.mainWin.config(menu = self.menubar)
        
        
        # #Connection Button
        self.btnConnection = tk.Button(self.playerFrame, text = "Connect", width = 10, height = 2, bg = "green", fg = "black", command = lambda: [self.connectionManager("nocare")])
      
#PLAYER SECTION GNWRGNLWRNGLWRNL  
#PLAYER Labels and Entries
        self.lblId = tk.Label(self.playerFrame, text = "Id", bg = "azure")
        self.entryId = tk.Entry(self.playerFrame, width = 5, bd = 1, relief = "sunken")
        
        self.lblName = tk.Label(self.playerFrame, text = "Player", bg = "azure")
        self.entryName = tk.Entry(self.playerFrame, width = 20, bd = 1, relief = "sunken")

        self.lblAge = tk.Label(self.playerFrame, text = "Age", bg = "azure")
        self.entryAge = tk.Entry(self.playerFrame, width = 5, bd = 1, relief = "sunken")

        self.lblCountry = tk.Label(self.playerFrame, text = "Country", bg = "azure")
        self.entryCountry = tk.Entry(self.playerFrame, width = 5, bd = 1, relief = "sunken")

        self.lblBlitzRating = tk.Label(self.playerFrame, text = "Blitz Rating", bg = "azure")
        self.entryBlitzRating = tk.Entry(self.playerFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblBlitzRank = tk.Label(self.playerFrame, text = "Blitz Rank", bg = "azure")
        self.entryBlitzRank = tk.Entry(self.playerFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblRapidRating = tk.Label(self.playerFrame, text = "Rapid Rating", bg = "azure")
        self.entryRapidRating = tk.Entry(self.playerFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblRapidRank = tk.Label(self.playerFrame, text = "Rapid Rank", bg = "azure")
        self.entryRapidRank = tk.Entry(self.playerFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblClassicalRating = tk.Label(self.playerFrame, text = "Classical Rating", bg = "azure")
        self.entryClassicalRating = tk.Entry(self.playerFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblClassicalRank = tk.Label(self.playerFrame, text = "Classical Rank", bg = "azure")
        self.entryClassicalRank = tk.Entry(self.playerFrame, width = 10, bd = 1, relief = "sunken")
        
#PLAYER Navigation buttons
        self.btnFirst       = tk.Button(self.playerFrame, text = "|<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.clear(), self.displayPlayer(0)])
        self.btnFastBack    = tk.Button(self.playerFrame, text = "<<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(-5)])
        self.btnBack        = tk.Button(self.playerFrame, text = "<",  width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(-1)])
        self.btnForward     = tk.Button(self.playerFrame, text = ">",  width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(1)])
        self.btnFastForward = tk.Button(self.playerFrame, text = ">>", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(5)])
        self.btnLast        = tk.Button(self.playerFrame, text = ">|", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(len(self.playerDB.records) - 1)])

        #PLAYER FeedBack Label
        self.lblFeedback = tk.Label(self.playerFrame, text="Press Connect to Begin...", bg="gray")


        #PLAYER CRUD buttons
        self.btnNew = tk.Button(self.playerFrame, text="New Player", width=12, height=2, bg="gray", fg="black", command= self.addPlayer)
        self.btnSave = tk.Button(self.playerFrame, text="Save Player", width=12, height=2, bg="gray", fg="black", command= self.updatePlayer)
        self.btnDelete = tk.Button(self.playerFrame, text="Delete Player", width=12, height=2, bg="gray", fg="black", command= self.showConfirmAlert)
#PLAYER These place the following:

        #Connection Button
        self.btnConnection.place(x=25, y=40)


        #Id
        self.lblId.place(x=625, y=20)
        self.entryId.place(x=625, y=40)


        #Name
        self.lblName.place(x=50, y=110)
        self.entryName.place(x=50, y=130)


        #Age
        self.lblAge.place(x=325, y=110)
        self.entryAge.place(x=325, y=130)
        
        #Country
        self.lblCountry.place(x=425, y=110)
        self.entryCountry.place(x=425, y=130)
        
        #Ratings
        self.lblBlitzRating.place(x=50, y=240)
        self.entryBlitzRating.place(x=50, y=260)

        self.lblBlitzRank.place(x=400, y=240)
        self.entryBlitzRank.place(x=400, y=260)
   
        self.lblRapidRating.place(x=50, y=300)
        self.entryRapidRating.place(x=50, y=320)
     
        self.lblRapidRank.place(x=400, y=300)
        self.entryRapidRank.place(x=400, y=320)
        
        self.lblClassicalRating.place(x=50, y=360)
        self.entryClassicalRating.place(x=50, y=380)
     
        self.lblClassicalRank.place(x=400, y=360)
        self.entryClassicalRank.place(x=400, y=380)
        
        #Navigation buttons
        self.btnFirst.place(x=60, y=500)
        self.btnFastBack.place(x=160, y=500)
        self.btnBack.place(x=260, y=500)
        self.btnForward.place(x=360, y=500)
        self.btnFastForward.place(x=460, y=500)
        self.btnLast.place(x=560, y=500)


        #FeedBack Label
        self.lblFeedback.place(x=25, y=750)


        #CRUD buttons
        self.btnNew.place(x=100, y=600)
        self.btnSave.place(x=300, y=600)
        self.btnDelete.place(x=500, y=600)


#GAME SECTION NR JENGKBRENKJGBJKRBRBGLJ
#GAME Labels and Entries
        self.lblId2 = tk.Label(self.gameFrame, text = "Id", bg = "azure")
        self.entryId2 = tk.Entry(self.gameFrame, width = 5, bd = 1, relief = "sunken")
        
        self.lblPlayer = tk.Label(self.gameFrame, text = "Player", bg = "azure")
        self.entryPlayer = tk.Entry(self.gameFrame, width = 30, bd = 1, relief = "sunken")

        self.lblmoveList = tk.Label(self.gameFrame, text = "moveList", bg = "azure")
        self.entrymoveList = tk.Entry(self.gameFrame, width = 30, bd = 1, relief = "sunken")

        self.lblGameType = tk.Label(self.gameFrame, text = "GameType", bg = "azure")
        self.entryGameType = tk.Entry(self.gameFrame, width = 30, bd = 1, relief = "sunken")

        self.lblResult = tk.Label(self.gameFrame, text = "Result", bg = "azure")
        self.entryResult = tk.Entry(self.gameFrame, width = 30, bd = 1, relief = "sunken")
        
        self.lblComments = tk.Label(self.gameFrame, text = "Comments", bg = "azure")
        self.entryComments = tk.Entry(self.gameFrame, width = 30, bd = 1, relief = "sunken")
        
#GAME Navigation buttons
        self.btnFirst2       = tk.Button(self.gameFrame, text = "|<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.clear2(), self.displayGame(0)])
        self.btnFastBack2    = tk.Button(self.gameFrame, text = "<<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec2(-5)])
        self.btnBack2        = tk.Button(self.gameFrame, text = "<",  width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec2(-1)])
        self.btnForward2     = tk.Button(self.gameFrame, text = ">",  width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec2(1)])
        self.btnFastForward2 = tk.Button(self.gameFrame, text = ">>", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec2(5)])
        self.btnLast2        = tk.Button(self.gameFrame, text = ">|", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec2(len(self.gameDB.records) - 1)])

        #GAMEFeedBack Label
        self.lblFeedback2 = tk.Label(self.gameFrame, text="Waiting...", bg="gray")


        #CRUD buttons
        self.btnNew2 = tk.Button(self.gameFrame, text="New Game", width=12, height=2, bg="gray", fg="black", command= self.addGame)
        self.btnSave2 = tk.Button(self.gameFrame, text="Save Game", width=12, height=2, bg="gray", fg="black", command= self.updateGame)
        self.btnDelete2 = tk.Button(self.gameFrame, text="Delete Game", width=12, height=2, bg="gray", fg="black", command= self.showConfirmAlert2)

        #Game button
        self.btnGame = tk.Button(self.gameFrame, text="See Game", width=12, height=2, bg="gray", fg="black", command= self.runGame)
#GAME These place the following:

        #Id
        self.lblId2.place(x=50, y = 120)
        self.entryId2.place(x=50, y=140)


        #Player
        self.lblPlayer.place(x=400, y=120)
        self.entryPlayer.place(x=400, y=140)


        #Game button
        self.btnGame.place(x=50, y=300)
        #moveList
        self.lblmoveList.place(x=50, y=180)
        self.entrymoveList.place(x=50, y=200)
        
        #GameType
        self.lblGameType.place(x=400, y=180)
        self.entryGameType.place(x=400, y=200)
        
        #Ratings
        self.lblResult.place(x=50, y=240)
        self.entryResult.place(x=50, y=260)

        self.lblComments.place(x=400, y=240)
        self.entryComments.place(x=400, y=260)
        
        #Navigation buttons
        self.btnFirst2.place(x=60, y=500)
        self.btnFastBack2.place(x=160, y=500)
        self.btnBack2.place(x=260, y=500)
        self.btnForward2.place(x=360, y=500)
        self.btnFastForward2.place(x=460, y=500)
        self.btnLast2.place(x=560, y=500)


        #FeedBack Label
        self.lblFeedback2.place(x=50, y=750)


        #CRUD buttons
        self.btnNew2.place(x=100, y=600)
        self.btnSave2.place(x=300, y=600)
        self.btnDelete2.place(x=500, y=600)

        #Runs the loop
        self.mainWin.mainloop()

  
#Connection to do both DBs
    #Creating new everything
    def add(self):
        self.addPlayer()
        self.addGame()
        
    #Deleteing everything
    def update(self):
        self.updatePlayer()
        self.updateGame()
    
    
    
    #Connection Manager
    def connectionManager(self, connect):
        
        #Test to run command
        skip = 1
        #If already connected will not allow connect from menu
        if(connect == "connect"):
            if(self.connection):
                self.lblFeedback.config(text = "Already connected")
                skip = 2
        #If already disconnected will not allow disconnect from menu
        if(connect == "noconnect"):
            if(not self.connection):
                self.lblFeedback.config(text = "Already disconnected")
                skip = 2
        #Runs commands to connect/disconnect the database to the 
        if(skip == 1):
            if(not self.connection):
                answer = self.playerDB.connect()
                self.btnConnection.config(activebackground="blue", bg="light green", fg="black", text="Disconnect")
                self.connection=True
                self.gameDB.read_games()
                self.lblFeedback.config(text=answer)
            else:
                answer = self.playerDB.disconnect()
                self.btnConnection.config(activebackground="gray", bg="pale violet red", fg="black", text="Connect")
                self.connection=False
                self.currentPlayer = 0
                self.lblFeedback.config(text=answer)
#Navigation based on Id


#PLAYER Navigation Section
    def jumpRec(self, jump):
        self.currentPlayer = self.currentPlayer + jump
        
        self.size = len(self.playerDB.records)
        
        if(self.currentPlayer >= self.size):
            self.currentPlayer = self.size - 1
            
        if(self.currentPlayer < 0):
            self.currentPlayer = 0

        self.displayPlayer(self.currentPlayer)      
          
#GAME Navigation Section
    def jumpRec2(self, jump):
        self.currentGame = self.currentGame + jump
        
        self.size = len(self.gameDB.records)

        if(self.currentGame >= self.size):
            self.currentGame = self.size - 1
            
        if(self.currentGame < 0):
            self.currentGame = 0

        self.displayGame(self.currentGame) 
        
    def help(self): # messagebox for help
        messagebox.showinfo("Help", "If you press the edit changes button at the bottom left, there will be a new window opened for you to edit the player stats. On the right side, you can also edit the moves of the chess game and make comments over the game to learn and improve.")
        tk.mainloop()
        
        

    
    def about(self): # messagebox for about us
        messagebox.showinfo("About us", "We have created this chess statistic database to ensure our user has the greatest experience analyzing gamegs along with ratings and rank. This will allow for enhanced gameplay usage, as well as a greater knowledge of chess.")
        tk.mainloop()
    
    # confirm exit function
    def confirm_exit(self):
        confirm = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
        if confirm:
            self.mainWin.destroy()
            
#PLAYER CRUD Section

    #CREATE
    def addPlayer(self):
        
        if(not self.midInsert):
            self.clear()
            self.btnNew.config(text = "Commit Insertion")
            self.midInsert = True
        else:
            self.getPlayer()                    #Helper Function to pull data from the edits
            answer = self.playerDB.create_player()          #Calling the insert from playerDB 
            self.lblFeedback.config(text = answer)
            self.btnNew.config(text = "New Player")
            self.midInsert = False
            
    def getPlayer(self):
            self.player.id = self.entryId.get()
            self.player.name = self.entryName.get()
            self.player.age = self.entryAge.get()
            self.player.country = self.entryCountry.get()
            self.player.blitzRating = self.entryBlitzRating.get()
            self.player.blitzRank = self.entryBlitzRank.get()
            self.player.rapidRating = self.entryRapidRating.get()
            self.player.rapidRank = self.entryRapidRank.get()
            self.player.classicalRating = self.entryClassicalRating.get()
            self.player.classicalRank = self.entryClassicalRank.get()
            
            
            self.playerDB.player = self.player
    #READ
    
    def displayPlayer(self, playerNum):
        #Unpack to display it
        (self.player.id, self.player.name, self.player.age, self.player.country, self.player.blitzRating, self.player.blitzRank, self.player.rapidRating, self.player.rapidRank, self.player.classicalRating, self.player.classicalRank) = self.playerDB.records[playerNum]

        
        #clears Everything
        self.clear()
        self.entryId.config(state = "normal")
        self.entryId.insert(0, self.player.id)
        self.entryId.config(state = "disabled")
    
        self.entryName.insert(0, self.player.name)
        self.entryAge.insert(0, self.player.age)
        self.entryCountry.insert(0, self.player.country)
        self.entryBlitzRating.insert(0, self.player.blitzRating)
        self.entryBlitzRank.insert(0, self.player.blitzRank)
        self.entryRapidRating.insert(0, self.player.rapidRating)
        self.entryRapidRank.insert(0, self.player.rapidRank)
        self.entryClassicalRating.insert(0, self.player.classicalRating)
        self.entryClassicalRank.insert(0, self.player.classicalRank)
        
        self.lblFeedback.config(text = "Record ID: " + str(self.player.id))     
        
    #UPDATE  
    def updatePlayer(self):
        self.getPlayer()
        self.playerDB.player = self.player
        answer = self.playerDB.update()
        self.lblFeedback.config(text = answer)   
        
#DELETE
    def deletePlayer(self, id):
        #Piped Dialogbox-to-delete-flow
        answer = self.result = self.playerDB.delete(id)
        self.lblFeedback.config(text = answer)
        #Protecting from an edge case out-of-bounds error for upper edge case
        self.currentPlayer = self.currentPlayer - 1
        self.displayPlayer(self.currentPlayer)

#DELETES EVERYTHING
    def deleteAll(self):
        self.deletePlayer()
        self.deleteGame()

#GAME CRUD Section

    #CREATE
    def addGame(self):
        
        if(not self.midInsert2):
            self.clear2()
            self.btnNew2.config(text = "Commit Insertion")
            self.midInsert2 = True
        else:
            self.getGame()                    #Helper Function to pull data from the edits
            answer2 = self.gameDB.create_game()          #Calling the insert from GameDB 
            self.lblFeedback2.config(text = answer2)
            self.btnNew2.config(text = "New Game")
            self.midInsert2 = False

            
    def getGame(self):
            self.game.id = self.entryId2.get()
            self.game.player = self.entryPlayer.get()
            self.game.moveList = self.entrymoveList.get()
            self.game.gameType = self.entryGameType.get()
            self.game.result = self.entryResult.get()
            self.game.comments = self.entryComments.get()

            
            
            self.gameDB.game = self.game
    #READ
    
    def displayGame(self, GameNum):
        (self.game.id, self.game.player, self.game.moveList, self.game.gameType, self.game.result, self.game.comments) = self.gameDB.records[GameNum]

        #Clear the entries
        self.clear2()
        
        self.entryId2.config(state = "normal")
        self.entryId2.insert(0, self.game.id)
        self.entryId2.config(state = "disabled")
        
        self.entryId2.insert(0, self.game.id)
        self.entryPlayer.insert(0, self.game.player)
        self.entrymoveList.insert(0, self.game.moveList)
        self.entryGameType.insert(0, self.game.gameType)
        self.entryResult.insert(0, self.game.result)
        self.entryComments.insert(0, self.game.comments)
        
        self.lblFeedback2.config(text = "Record ID: " + str(self.game.id))     
        
    #UPDATE  
    def updateGame(self):
        self.getGame()
        self.gameDB.game = self.game
        answer2 = self.gameDB.update()
        self.lblFeedback2.config(text = answer2)   
        
#DELETE
    def deleteGame(self, id):
        #Piped Dialogbox-to-delete-flow
        answer2 = self.result = self.gameDB.delete(id)
        self.lblFeedback2.config(text = answer2)
        
        #Protecting from an edge case out-of-bounds error for upper edge case
        self.currentGame = self.currentGame - 1
        self.displayGame(self.currentGame)
        
    
#Confirmation dialog box for deleting a record
#How we make sure the user really wants to delete a given Player
    def showConfirmAlert(self):
        s = "Press OK to delete the Player: " + self.entryName.get()
        
        if(tk.messagebox.askokcancel(title = "Confirm Delete", message = s)):
            answer = self.playerDB.delete(self.player.id)
            self.lblFeedback.config(text = answer)
        else:
            self.lblFeedback.config(text = "Deletion Cancelled.")
            
    def showConfirmAlert2(self):
        s = "Press OK to delete the Game: " + self.entryPlayer.get()
        
        if(tk.messagebox.askokcancel(title = "Confirm Delete", message = s)):
            answer2 = self.gameDB.delete(self.game.id)
            self.lblFeedback2.config(text = answer2)
        else:
            self.lblFeedback2.config(text = "Deletion Cancelled.")
            
    def showConfirmAlert3(self):
        s = "Press OK to delete : " + self.entryName.get() + " and " + self.entryPlayer.get()
        
        if(tk.messagebox.askokcancel(title = "Confirm Delete", message = s)):
            answer = self.playerDB.delete(self.player.id)
            answer2 = self.gameDB.delete(self.game.id)
            self.lblFeedback2.config(text = answer2)
            self.lblFeedback.config(text = answer)
        else:
            self.lblFeedback.config(text = "Deletion Cancelled.")
            
            self.lblFeedback2.config(text = "Deletion Cancelled.")
    
#Here is where we blank out all the entry widgets
    def clear(self):
        self.entryId.config(state = "normal")
        self.entryId.delete(0, tk.END)
        self.entryId.config(state = "disabled")
        
        self.entryId.delete(0, tk.END)
        self.entryName.delete(0, tk.END)
        self.entryAge.delete(0, tk.END)
        self.entryCountry.delete(0, tk.END)
        self.entryBlitzRating.delete(0, tk.END)
        self.entryBlitzRank.delete(0, tk.END)
        self.entryRapidRating.delete(0, tk.END)
        self.entryRapidRank.delete(0, tk.END)
        self.entryClassicalRating.delete(0, tk.END)
        self.entryClassicalRank.delete(0, tk.END)


#Blank out game frame
    def clear2(self):
        self.entryId2.config(state = "normal")
        self.entryId2.delete(0, tk.END)
        self.entryId2.config(state = "disabled")
        
        self.entryId2.delete(0, tk.END)
        self.entryPlayer.delete(0, tk.END)
        self.entrymoveList.delete(0, tk.END)
        self.entryGameType.delete(0, tk.END)
        self.entryResult.delete(0, tk.END)
        self.entryComments.delete(0, tk.END)

        
    def nav(self, db):
        #Creates new window from main window
        self.navWin = tk.Toplevel(self.mainWin)
        
        #Title
        self.navWin.title("Navigation")
        
        #Geomertry
        self.navWin.geometry('200x200')
        
        #Label
        self.lblNav = tk.Label(self.navWin, text = "Enter the record Id")
        #Entry to get id value
        self.entryNav = tk.Entry(self.navWin)
        #Gets id from the entry
        try:
            self.idNum = int(self.entryNav.get())
        except:
            self.idNum = 0
        #Button to do the command
        self.btnNav = tk.Button(self.navWin, text = "Find", width = 10, height = 2, bg = "green", fg = "black", command = lambda: [self.moveId(self.idNum,db), self.navWin.destroy()])
        self.lblNav.pack()
        self.entryNav.pack()
        self.btnNav.pack()

        
        
    def moveId(self, idNum, db):
        
        #Find out if it is a player or a game navigation then displays the id
        if(db == "player"):
            self.displayPlayer(idNum)
        
        if(db == "game"):
            self.displayGame(idNum)

        
    def runGame(self):
        self.moves = self.game.moveList 
        cmoves = self.convert()
        game = ChessGame(cmoves)
        gui = ChessGUI(game, self.mainWin)
        gui.run()
        
    # convert string into list of moves
    def convert(self):
        li = list(self.moves.split(" "))
        print(li)
        return li

    
