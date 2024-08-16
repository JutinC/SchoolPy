"""
Example Tkinter Database Program
Justin Choi
27 January 2023
IDT
Period 3
"""

#This is the application controller module: This is effectively the GUI

#Imports Section
#aka Preprocessor directives
import tkinter as tk
from albumDb import AlbumDb
from album import Album
from PIL import Image

class AlbumController():
        
    #Contructor(This is a LARGE section as we setup ALL of the UI devices)
    def __init__(self):
        #Initializing variable
        self.currentAlbum = 0
        self.album = Album()
        self.midInsert = False
        self.answer = ""
        
        #Instantiating the containee database class into an object here.
        #This makes the controller a container class
        self.AlbumDb = AlbumDb()
        
        #Initialize TKinter and set title/version for this App
        self.mainWin = tk.Tk()
        self.mainWin.title("Album Tracking Db 1.0")
        
        #Setting up main menu
        #File Menu
        self.menubar = tk.Menu(self.mainWin)
        
        self.connectMenu = tk.Menu(self.menubar, tearoff = 0)
        self.connectMenu.add_command(label = "Connect", command = self.connectionManager)
        self.connectMenu.add_command(label = "Disconnect", command = self.connectionManager)
        self.connectMenu.add_command(label = "Exit", command = self.mainWin.destroy)
        self.menubar.add_cascade(label = "File", menu = self.connectMenu)

        self.recordMenu = tk.Menu(self.menubar, tearoff = 0)
        self.recordMenu.add_command(label = "New Album", command = self.insertAlbum)
        self.recordMenu.add_command(label = "Save Changes", command = self.saveAlbum)
        self.recordMenu.add_command(label = "Delete Current Album", command = self.showConfirmAlert)
        self.menubar.add_cascade(label = "Albums", menu = self.recordMenu)
        
        self.navMenu = tk.Menu(self.menubar, tearoff = 0)
        self.navMenu.add_command(label = "First Album", command = lambda: [self.setToZero(), self.jumpRec(0)])
        self.navMenu.add_command(label = "Previous Album", command = lambda: [self.jumpRec(-1)])
        self.navMenu.add_command(label = "Next Album", command = lambda: [self.jumpRec(1)])
        self.navMenu.add_command(label = "Last Album", command = lambda: [self.jumpRec(len(self.AlbumDb.records) - 1)])
        self.menubar.add_cascade(label = "Navigation", menu = self.navMenu)
        
        self.helpMenu = tk.Menu(self.menubar, tearoff = 0)
        self.helpMenu.add_command(label = "About", command = self.showAboutAlert)
        self.menubar.add_cascade(label = "Help", menu = self.helpMenu)
        
        #Mount the main menu to the main window
        self.mainWin.config(menu = self.menubar)
        
        #Set Frame for the UI
        self.frame = tk.Frame(self.mainWin, width = 1000, height = 800)
        
        #Use a Canvas object to hold and display the background image
        self.eagleImage = tk.PhotoImage(file = "/Users/imatable/SchoolPy/bg.PNG")
        self.canvas = tk.Canvas(self.frame, width = 1000, height = 800)
        self.canvas.pack(fill = "both", expand = True)
        self.canvas.create_image(0, 0, image = self.eagleImage, anchor = "nw")
        
        #Placing widgets on the screen - Pattern we will use is: Build then place
        
        #Connection Button
        self.connectButton = tk.Button(self.frame, text = "Connect", width = 10, height = 2, bg = "pale violet red", fg = "black", command = self.connectionManager)
        
        #Labels and Entries
        self.lblId = tk.Label(self.frame, text = "Record Id", bg = "azure")
        self.entryId = tk.Entry(self.frame, width = 5, bd = 1, relief = "sunken", state = "disabled" )
        
        self.lblArtist = tk.Label(self.frame, text = "Artist(s)", bg = "azure")
        self.entryArtist = tk.Entry(self.frame, width = 30, bd = 1, relief = "sunken")

        self.lblTitle = tk.Label(self.frame, text = "Title", bg = "azure")
        self.entryTitle = tk.Entry(self.frame, width = 30, bd = 1, relief = "sunken")

        self.lblGenre = tk.Label(self.frame, text = "Genre", bg = "azure")
        self.entryGenre = tk.Entry(self.frame, width = 30, bd = 1, relief = "sunken")

        self.lblRating = tk.Label(self.frame, text = "Rating", bg = "azure")
        self.entryRating = tk.Entry(self.frame, width = 30, bd = 1, relief = "sunken")
        
        #Play Head Buttons
        self.btnFirst       = tk.Button(self.frame, text = "|<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.setToZero(), self.displayAlbum(0)])
        self.btnFastBack    = tk.Button(self.frame, text = "<<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(-5)])
        self.btnBack        = tk.Button(self.frame, text = "<",  width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(-1)])
        self.btnForward     = tk.Button(self.frame, text = ">",  width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(1)])
        self.btnFastForward = tk.Button(self.frame, text = ">>", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(5)])
        self.btnLast        = tk.Button(self.frame, text = ">|", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.len(self.albumDb.records) - 1])

        #Feedback Label
        self.lblFeedback = tk.Label(self.frame, text="Press Connect to Begin...", bg="gray")


        #Command Buttons
        self.btnNew = tk.Button(self.frame, text="New Album", width=12, height=2, bg="gray", fg="black", command=lambda: [self.insertAlbum()])
        self.btnSave = tk.Button(self.frame, text="Save Album", width=12, height=2, bg="gray", fg="black", command=lambda: [self.saveAlbum()])
        self.btnDelete = tk.Button(self.frame, text="Delete Album", width=12, height=2, bg="gray", fg="black", command=lambda: [self.showConfirmAlert()])


        #Placing Widgets on the screen
        self.connectButton.place(x=50, y=20)


        #Id
        self.lblId.place(x=50, y=120)
        self.entryId.place(x=50, y=140)


        #Artist
        self.lblArtist.place(x=50, y=180)
        self.entryArtist.place(x=50, y=200)


        #Title
        self.lblTitle.place(x=50, y=240)
        self.entryTitle.place(x=50, y=260)
        
        #Genre
        self.lblGenre.place(x=50, y=300)
        self.entryGenre.place(x=50, y=320)
        
        #Rating
        self.lblRating.place(x=50, y=360)
        self.entryRating.place(x=50, y=380)
        
        #Playback Buttons
        self.btnFirst.place(x=60, y=500)
        self.btnFastBack.place(x=160, y=500)
        self.btnBack.place(x=260, y=500)
        self.btnForward.place(x=360, y=500)
        self.btnFastForward.place(x=460, y=500)
        self.btnLast.place(x=560, y=500)


        #Feedback Label
        self.lblFeedback.place(x=100, y=760)


        #Command Buttons
        self.btnNew.place(x=100, y=600)
        self.btnSave.place(x=300, y=600)
        self.btnDelete.place(x=500, y=600)

        #Frame placement in the application main window grid
        self.frame.grid(row=1, column=0)

        #Run the Tk Loop!
        self.mainWin.mainloop()


    #Connection Manager
    def connectionManager(self):
        if(not self.albumDb.connected):
            answer = self.albumDb.connect()
            self.connectButton.config(activebackground="blue", bg="light green", fg="black", text="Disconnect")
            self.albumDb.connected=True
            self.albumDb.load()
            print(len(self.albumDb.records)) #Daemon print for testing only
            self.displayAlbum(0)
            self.lblfeedBack.config(text=answer)
        else:
            answer = self.albumDb.disconnect()
            self.connectButton.config(activebackground="gray", bg="pale violet red", fg="black", text="Connect")
            self.albumDb.connected=False
            self.currentAlbum = 0
            self.lblfeedBack.config(text=answer)

    #CRUD Section

    #CREATE
    def insertAlbum(self):
        if(not self.midInsert):
            self.setBlanks()
            self.btnNew.config(text = "Commit Insertion")
            self.midInsert = True
        else:
            self.retrieveAlbum()                    #Helper Function to pull data from the edits
            answer = self.albumDb.insert()          #Calling the insert function from albumDb
            self.lblFeedback.config(text = answer)
            self.btnNew.config(text = "New Album")
            self.midInsert = False

    def retrieveAlbum(self):
        self.album.id        = self.entryId.get()
        [[self.album.artist]]    = self.entryArtist.get()
        self.album.title     = self.entrTitle.get()
        self.album.genre     = self.entryGenre.get()
        self.album.rating    = self.entryRating.get()
        
        self.albumDb.album = self.album
        
    #READ
    #Pulling an album from the results list and pushing it to the screen (UI)
    def displayAlbum(self, albumNum):
        #Unpack the tuple from records (our list) into our album class object for display
        (self.album.id, self.album.artist, self.album.title, self.album.genre, self.album.rating) = self.album.Db.records[albumNum]
        
        #Clear the entries
        self.setBlanks()
        print(self.album.id) #Daemon print to show me I am on the correct record (Debugging)
        self.entryId.config(state = "normal")
        self.entryId.delete(0, tk.END)
        self.entryId.insert(0, self.album.id)
        self.entryId.config(state = "disabled")
        
        self.entryArtist.insert(0, self.album.artist)
        self.entryTitle.insert(0, self.album.title)
        self.entryGenre.insert(0, self.album.genre)
        self.entryRating.insert(0, self.album.rating)
        
        self.lblFeedback.config(text = "Record ID: " + str(self.album.id))
    
    #UPDATE  
    def saveAlbum(self):
        self.retrieveAlbum()
        self.albumDb.album = self.album
        answer = self.albumDb.update()
        self.lblFeedback.config(text = answer)
        
    #DELETE
    def deleteAlbum(self, id):
        #Piped Dialogbox-to-delete-flow
        answer = self.result = self.albumDb.delete(id)
        self.lblFeedback.config(text = answer)
        
        #Protecting from an edge case out-of-bounds error for upper edge case
        self.currentAlbum = self.currentAlbum - 1
        self.displayAlbum(self.currentAlbum)

    #Navigation Section
    def jumpRec(self, jump):
        self.currentAlbum = self.currentAlbum + jump
        
        size = len(self.albumDb.records)
        
        if(self.currentAlbum >= size):
            self.currentAlbum = size - 1
            
        if(self.currentAlbum < 0):
            self.currentAlbum = 0

        self.displayAlbum(self.currentAlbum)
        
    def setToZero(self):
        self.currentAlbum = 0

    #Utility methods
    #This dialog box is extremely helpful while writing my code
    def showDialogAlert(self):
        tk.messagebox.showwarning(title = "Button Clicked", message = "This button click has not yet been handled.")

    #Help about dialog box
    def showAboutAlert(self):
        tk.messagebox.showwarning(title = "About Albums", message = "Example Database Program for IDT Period 3.")
        
    #Confirmation dialog box for deleting a record
    #How we make sure the user really wants to delete a given Album
    def showConfirmAlert(self):
        s = "Press OK to delete the Album: \n" + self.entryTitle.get()
        
        if(tk.messagebox.askyesnocancel(title = "Confirm Delete", message = s)):
            answer = self.deleteAlbum(self.album.id)
            self.lblFeedback.config(text = answer)
        else:
            self.lblFeedback.config(text = "Deletion Cancelled.")
        
    #Here is where we blank out all the entry widgets
    def setBlanks(self):
        self.entryId.config(state = "normal")
        self.entryId.delete(0, tk.END)
        self.entryId.config(state = "disabled")
        self.entryArtist.delete(0, tk.END)
        self.entryTitle.delete(0, tk.END)
        self.entryGenre.delete(0, tk.END)
        self.entryRating.delete(0, tk.END)
        
    #Nice to have while building
    def doNothing(self):
        pass

