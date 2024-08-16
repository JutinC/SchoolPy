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
from test3 import ChessController

#Here the Game and Player DB are mixed into one
class ChessController:

    def __init__(self, ChessController):
        
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
        #Adds a new window
        self.editWin = tk.Toplevel(self.editWin)
        
        #Title
        self.editWin.title("Edit")
        
        #Sets Geometry

        self.editWin.geometry('1500x1000')

         
        #Setting the player Frame
        self.playerFrame = tk.Frame(self.editWin, width = 700, height = 800)
        self.playerFrame.grid(row = 0, column = 0)
        
        # Set the game Frame
        self.gameFrame = tk.Frame(self.editWin, width = 700, height = 800)
        self.gameFrame.grid(row = 0, column = 1)
        
        #Setting the icon of the window
        self.ico = Image.open('/Users/imatable/SchoolPy/chess.ico')
        self.photo = ImageTk.PhotoImage(self.ico)
        self.editWin.wm_iconphoto(False, self.photo)
        
        # # #Picture
        # self.bgFrame = tk.Frame(self.editWin, width=813, height=477)

        #Player Image   
        self.chessImage = tk.PhotoImage(file='/Users/imatable/SchoolPy/bg.PNG')
        self.canvas = tk.Canvas(self.playerFrame, width=813, height=477)
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.chessImage, anchor="nw")
        
#PLAYER SECTION GNWRGNLWRNGLWRNL  
#PLAYER Labels and Entries
        self.lblId = tk.Label(self.playerFrame, text = "Record Id", bg = "azure")
        self.entryId = tk.Entry(self.playerFrame, width = 5, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblName = tk.Label(self.playerFrame, text = "Player", bg = "azure")
        self.entryName = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")

        self.lblAge = tk.Label(self.playerFrame, text = "Age", bg = "azure")
        self.entryAge = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")

        self.lblCountry = tk.Label(self.playerFrame, text = "Country", bg = "azure")
        self.entryCountry = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")

        self.lblBlitzRating = tk.Label(self.playerFrame, text = "Blitz Rating", bg = "azure")
        self.entryBlitzRating = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblBlitzRank = tk.Label(self.playerFrame, text = "Blitz Rank", bg = "azure")
        self.entryBlitzRank = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblRapidRating = tk.Label(self.playerFrame, text = "Rapid Rating", bg = "azure")
        self.entryRapidRating = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblRapidRank = tk.Label(self.playerFrame, text = "Rapid Rank", bg = "azure")
        self.entryRapidRank = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblClassicalRating = tk.Label(self.playerFrame, text = "Classical Rating", bg = "azure")
        self.entryClassicalRating = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblClassicalRank = tk.Label(self.playerFrame, text = "Classical Rank", bg = "azure")
        self.entryClassicalRank = tk.Entry(self.playerFrame, width = 30, bd = 1, relief = "sunken", state = "disabled")
        
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
        self.connectButton.place(x=50, y=20)


        #Id
        self.lblId.place(x=50, y=120)
        self.entryId.place(x=50, y=140)


        #Name
        self.lblName.place(x=400, y=120)
        self.entryName.place(x=400, y=140)


        #Age
        self.lblAge.place(x=50, y=180)
        self.entryAge.place(x=50, y=200)
        
        #Country
        self.lblCountry.place(x=400, y=180)
        self.entryCountry.place(x=400, y=200)
        
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
