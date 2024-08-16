"""
School Controller
Justin Choi
15 March 2023
IDT
Period 3
"""
#External Libraries
import tkinter as tk
from tkinter import messagebox
from school import School
from schoolDatabase import SchoolDatabase
from PIL import ImageTk, Image


#Here the Game and school DB are mixed into one
class SchoolController:

    def __init__(self):
        
        #school Values
        self.currentSchool = 0
        self.school = School()
        self.midInsert = False
        self.answer = ""
        self.connection = False
        self.schoolDatabase = SchoolDatabase()
        
        #set the main window
        self.mainWin = tk.Tk()
        self.mainWin.title("Schools in GA")   
        self.mainWin.geometry('800x1000') 

        
        #File Section
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
        self.recordMenu.add_command(label = "Delete ", command = self.showConfirmAlert)
        self.menubar.add_cascade(label = "Edit", menu = self.recordMenu)

        #ADD BOTH GAMES
        #navigation menu
        self.navMenu = tk.Menu(self.menubar, tearoff = 0)
        self.navMenu.add_command(label = "School", command = lambda: [self.nav("school")])
        self.menubar.add_cascade(label = "Navigation", menu = self.navMenu)
        
        #help menu
        self.helpMenu = tk.Menu(self.menubar, tearoff = 0)
        self.helpMenu.add_command(label = "Directions", command= self.help)
        self.helpMenu.add_command(label = "About", command = self.about)
        self.menubar.add_cascade(label = "Help", menu = self.helpMenu)

        #Set Frame to hold the school stats
        self.mainWin.config(menu = self.menubar)

        #Setting the school Frame
        self.schoolFrame = tk.Frame(self.mainWin, width = 750, height = 1000)
        # #Setting the icon of the window
        # self.ico = Image.open('iconSchool.ico')
        # self.photo = ImageTk.PhotoImage(self.ico)
        # self.mainWin.wm_iconphoto(False, self.photo)



        # #school Image 
        self.imagePath = "imageSchool.jpg"
        self.image = Image.open(self.imagePath)
        self.schoolImage = ImageTk.PhotoImage(self.image)
        self.imageLabel = tk.Label(self.mainWin, image=self.schoolImage)
        self.imageLabel.image = self.schoolImage
        self.imageLabel.place(x=525,y=200)


        # self.rawImage = Image.open("imageSchool.png")
        # self.schoolImage = ImageTk.PhotoImage(self.rawImage)
        # self.canvas = tk.Canvas(self.schoolFrame, width=800, height=1000)
        # self.canvas.pack(fill="both", expand=True)
        # self.canvas.create_image(0, 0, Image=self.schoolImage, anchor="nw")

        #Connection Button
        self.btnConnection = tk.Button(self.schoolFrame, text = "Connect", width = 10, height = 2, bg = "green", fg = "black", command = lambda: [self.connectionManager("nocare")])
        
        #school Labels and Entries
        self.lblId = tk.Label(self.schoolFrame, text = "Id", bg = "azure")
        self.entryId = tk.Entry(self.schoolFrame, width = 5, bd = 1, relief = "sunken", state = "disabled")
        
        self.lblName = tk.Label(self.schoolFrame, text = "school", bg = "azure")
        self.entryName = tk.Entry(self.schoolFrame, width = 20, bd = 1, relief = "sunken")

        self.lblDistrict = tk.Label(self.schoolFrame, text = "District", bg = "azure")
        self.entryDistrict = tk.Entry(self.schoolFrame, width = 5, bd = 1, relief = "sunken")

        self.lblCounty = tk.Label(self.schoolFrame, text = "County", bg = "azure")
        self.entryCounty = tk.Entry(self.schoolFrame, width = 5, bd = 1, relief = "sunken")

        self.lblSchoolRank = tk.Label(self.schoolFrame, text = "SchoolRank", bg = "azure")
        self.entrySchoolRank = tk.Entry(self.schoolFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblSports = tk.Label(self.schoolFrame, text = "Sports", bg = "azure")
        self.entrySports = tk.Entry(self.schoolFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblArts = tk.Label(self.schoolFrame, text = "Arts", bg = "azure")
        self.entryArts = tk.Entry(self.schoolFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblScience = tk.Label(self.schoolFrame, text = "Science", bg = "azure")
        self.entryScience = tk.Entry(self.schoolFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblMisc = tk.Label(self.schoolFrame, text = "Misc", bg = "azure")
        self.entryMisc = tk.Entry(self.schoolFrame, width = 10, bd = 1, relief = "sunken")
        
        self.lblTeacher = tk.Label(self.schoolFrame, text = "Teacher", bg = "azure")
        self.entryTeacher = tk.Entry(self.schoolFrame, width = 10, bd = 1, relief = "sunken")
        
        #school Navigation buttons
        self.btnFirst = tk.Button(self.schoolFrame, text = "|<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.clear(), self.displaySchool(0)])
        self.btnFastBack = tk.Button(self.schoolFrame, text = "<<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(-5)])
        self.btnBack = tk.Button(self.schoolFrame, text = "<", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(-1)])
        self.btnForward = tk.Button(self.schoolFrame, text = ">", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(1)])
        self.btnFastForward = tk.Button(self.schoolFrame, text = ">>", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(5)])
        self.btnLast = tk.Button(self.schoolFrame, text = ">|", width = 5, height = 2, bg = "gray", fg = "black", command = lambda: [self.jumpRec(len(self.schoolDatabase.records) - 1)])

        #school FeedBack Label
        self.lblFeedback = tk.Label(self.schoolFrame, text="Press Connect to Begin...", bg="gray")

        #school CRUD buttons
        self.btnNew = tk.Button(self.schoolFrame, text="New school", width=12, height=2, bg="gray", fg="black", command= self.addSchool)
        self.btnSave = tk.Button(self.schoolFrame, text="Save school", width=12, height=2, bg="gray", fg="black", command= self.updateSchool)
        self.btnDelete = tk.Button(self.schoolFrame, text="Delete school", width=12, height=2, bg="gray", fg="black", command= self.showConfirmAlert)
        
        #school place the following:
        #Connection Button
        
        self.btnConnection.place(x=25, y=40)
        #Id
        self.lblId.place(x=625, y=20)
        self.entryId.place(x=625, y=40)

        #Name
        self.lblName.place(x=50, y=110)
        self.entryName.place(x=50, y=130)

        #District
        self.lblDistrict.place(x=375, y=110)
        self.entryDistrict.place(x=375, y=130)
        
        #County
        self.lblCounty.place(x=525, y=110)
        self.entryCounty.place(x=525, y=130)
        
        #Ratings
        self.lblSchoolRank.place(x=150, y=240)
        self.entrySchoolRank.place(x=150, y=260)

        self.lblSports.place(x=450, y=240)
        self.entrySports.place(x=450, y=260)
        
        self.lblArts.place(x=150, y=300)
        self.entryArts.place(x=150, y=320)
        
        self.lblScience.place(x=450, y=300)
        self.entryScience.place(x=450, y=320)
        
        self.lblMisc.place(x=150, y=360)
        self.entryMisc.place(x=150, y=380)
        
        self.lblTeacher.place(x=450, y=360)
        self.entryTeacher.place(x=450, y=380)
        
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

        self.schoolFrame.grid(row = 1, column = 0)
        #Runs the loop
        self.mainWin.mainloop()

    #Connection to do both DBs CAN BE ACCESSED THROUGH FILES
    #Creating new everything
    def add(self):
        self.addSchool()
    
    #Deleteing everything
    def update(self):
        self.updateSchool()
    
    #Connection ManDistrictr
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
                answer = self.schoolDatabase.connect()
                self.btnConnection.config(activebackground="blue", bg="light green", fg="black", text="Disconnect")
                self.connection=True
                self.lblFeedback.config(text=answer)
                self.displaySchool(0)
            else:
                answer = self.schoolDatabase.disconnect()
                self.btnConnection.config(activebackground="gray", bg="pale violet red", fg="black", text="Connect")
                self.connection=False
                self.currentSchool = 0
                self.lblFeedback.config(text=answer)


    #school Navigation Section
    def jumpRec(self, jump):
        self.currentSchool = self.currentSchool + jump
        self.size = len(self.schoolDatabase.records)
        
        if(self.currentSchool >= self.size):
            self.currentSchool = self.size - 1 
        if(self.currentSchool < 0):
            self.currentSchool = 0

        self.displaySchool(self.currentSchool) 
    
    #messagebox for help
    def help(self): 
        messagebox.showinfo("Help", "Press Connect then edit everything else. For the see game function, you want your move list to be the coordinate the piece is from to the coordinate the piece goes Ex. e2e4 moves pawn to e4.")
        tk.mainloop()
    
    #messagebox for about us
    def about(self): 
        messagebox.showinfo("About us", "We have created this chess statistic database to ensure our user has the greatest experience analyzing gamegs along with ratings and SchoolRank. This will allow for enhanced gameplay usDistrict, as well as a greater knowledge of chess.")
        tk.mainloop()
    
    #confirm exit function
    def confirm_exit(self):
        confirm = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
        if confirm:
            self.mainWin.destroy()
    
    #school CRUD Section
    #CREATE
    def addSchool(self):
        if(not self.midInsert):
            self.clear()
            self.btnNew.config(text = "Commit Insertion")
            self.midInsert = True
        else:
            #pgets the school data
            print("else happened")
            self.getSchool() 
            print("SChool happened???")
            #calls insert function
            answer = self.schoolDatabase.create_school() 
            self.lblFeedback.config(text = answer)
            self.btnNew.config(text = "New school")
            self.midInsert = False
    
    def getSchool(self):
        #function to get each entry
        self.school.id = self.entryId.get()
        self.school.name = self.entryName.get()
        self.school.district = self.entryDistrict.get()
        self.school.county = self.entryCounty.get()
        self.school.schoolRank = self.entrySchoolRank.get()
        self.school.sports = self.entrySports.get()
        self.school.arts = self.entryArts.get()
        self.school.science = self.entryScience.get()
        self.school.misc = self.entryMisc.get()
        self.school.teacher = self.entryTeacher.get()
        self.schoolDatabase.school = self.school
    
    #READ
    def displaySchool(self, schoolNum):
        #Unpack to display it
        (self.school.id, self.school.name, self.school.District, self.school.County, self.school.SchoolRank, self.school.Sports, self.school.Arts, self.school.Science, self.school.Misc, self.school.Teacher) = self.schoolDatabase.records[schoolNum]

        #clears Everything
        self.clear()
        #Edit id to change it
        self.entryId.config(state = "normal")
        self.entryId.insert(0, self.school.id)
        self.entryId.config(state = "disabled")
        self.entryName.insert(0, self.school.name)
        self.entryDistrict.insert(0, self.school.District)
        self.entryCounty.insert(0, self.school.County)
        self.entrySchoolRank.insert(0, self.school.SchoolRank)
        self.entrySports.insert(0, self.school.Sports)
        self.entryArts.insert(0, self.school.Arts)
        self.entryScience.insert(0, self.school.Science)
        self.entryMisc.insert(0, self.school.Misc)
        self.entryTeacher.insert(0, self.school.Teacher)
        
        self.lblFeedback.config(text = "Record ID: " + str(self.school.id)) 
        
    #UPDATE 
    def updateSchool(self):
        #Gets the entry values to the update them to the actual record
        self.getSchool()
        self.schoolDatabase.school = self.school
        answer = self.schoolDatabase.update()
        self.lblFeedback.config(text = answer) 
    
    #DELETE
    def deleteSchool(self, id):
        answer = self.result = self.schoolDatabase.delete(id)
        self.lblFeedback.config(text = answer)
        self.currentSchool = self.currentSchool - 1
        self.displaySchool(self.currentSchool)

    
    #Confirmation on how to delete the record for school
    def showConfirmAlert(self):
        s = "Press OK to delete the school: " + self.entryName.get()
        if(tk.messagebox.askokcancel(title = "Confirm Delete", message = s)):
            answer = self.schoolDatabase.delete(self.school.id)
            self.lblFeedback.config(text = answer)
        else:
            self.lblFeedback.config(text = "Deletion Cancelled.")
    
    
    #Makes all the fields empty
    def clear(self):
        self.entryId.config(state = "normal")
        self.entryId.delete(0, tk.END)
        self.entryId.config(state = "disabled")
        self.entryId.delete(0, tk.END)
        self.entryName.delete(0, tk.END)
        self.entryDistrict.delete(0, tk.END)
        self.entryCounty.delete(0, tk.END)
        self.entrySchoolRank.delete(0, tk.END)
        self.entrySports.delete(0, tk.END)
        self.entryArts.delete(0, tk.END)
        self.entryScience.delete(0, tk.END)
        self.entryMisc.delete(0, tk.END)
        self.entryTeacher.delete(0, tk.END)

    def nav(self, db):
        #Creates new window from main window
        self.navWin = tk.Toplevel(self.mainWin)
        #Title
        self.navWin.title("Navigation")
        #Geometry
        self.navWin.geometry('200x200')
        #Label
        self.lblNav = tk.Label(self.navWin, text = "Enter the record Id")
        #Entry to get id value
        self.entryNav = tk.Entry(self.navWin)
        #Gets id from the entry
        navId = self.entryNav.get()
        print(navId)
        self.idNum = 0
        #Button to do the command
        self.btnNav = tk.Button(self.navWin, text = "Find", width = 10, height = 2, bg = "green", fg = "black", command = lambda: [self.moveId(self.idNum,db), self.navWin.destroy()])
        #Packs everything
        self.lblNav.pack()
        self.entryNav.pack()
        self.btnNav.pack()
    
    def moveId(self, idNum, db):
        #Find out if it is a school or a game navigation then displays the id
        if(db == "school"):
         self.displaySchool(idNum)