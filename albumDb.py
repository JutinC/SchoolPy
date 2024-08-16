"""
Example Tkinter Database Program
Justin Choi
27 January 2023
IDT
Period 3
"""

#Preprocessors
import tkinter as tk
import sqlite3
from album import Album

class AlbumDb:
    
    def __init__(self):
        
        #Here is where we define fields of the python code
        #This class will be the "Container" class in our controller class
        
        #Connection Flag
        self.connected = False
        
        #List for containing records from the database
        self.records = []
        
        #Album object to hold trnsitory to/from records
        self.album = Album()
    
    #Connection Methods Section
    
    #Connecting
    def connect(self):
        #All database connection and queries MUST be try/excepted
        try:
            #connection object to local instance of an sqlite3 database
            self.sqlConnection = sqlite3.connect("album.sqlite")
        
            #Creating a cursor object for this database
            self.cursor = self.sqlConnection.cursor()
            
            return "Connected Property"
        except sqlite3.Error as error:
            return "Error Connecting", error
      
    #Disconnecting  
    def disconnect(self):
        if(self.sqlConnection):
            self.sqlConnection.close()
            return "Connection closed"
    
    #CREATE, READ, UPDATE, DELETE Section (CRUD)
    # (We will build the load routine first which is READ)
    
    #Querying database for all records and loading them into our list (self.)
    #This container is where the UI will access the table records
    
    def load(self):
        try:
            #Query everything SORTED (ORDER BY) Artist
            query = "SELECT * FROM albums ORDER BY artist;"
            self.cursor.execute(query)
            
            #Retrieve all records into our lsit as a list of TUPLES
            self.records = self.cursor.fetchall()
            print(self.records) #Daemon print for debug
            return ""
        except sqlite3.Error as error:
            return "Error Loading ", error
        
    #Inserting a record into the databse table.
    #WE will NOT push an id value because we have autoincrement for the PK for albums table
    def insert(self):
        try:
            query = "INSERT INTO albums (artist, title, genre, rating) VALUES (?,?,?,?)"
            self.cursor.execute(query, [self.album.artist, self.album.title, self.album.genre, self.album.rating])
            self.sqlConnection.commit()
            
            #Since we are keeping a database we will just do a reload here rather than pull the new id into memory
            self.load()
            return "Insertion Complete."
        
        except sqlite3.Error as error:
            return "Error Inserting Record: ", error

    #Updating  an existing record
    # (UPDATE)
    def update(self):
        try:
            #Be VERY CAREFUL buidling this query. Note SINGLE apostrophes for fields that need to be inside query strings vs numerical values
            query   =     "'UPDATE albums SET artist = '" + self.album.artist
            query = query + "', title = " + self.album.title
            query = query + "', rating = '" + str(self.album.rating) #Numerical value...
            query = query + "', WHERE id = '" + str(self.album.id) + ";"
            
            print(query) #daemon print for debugging
            self.cursor.execute(query)
            self.sqlConnection.commit()
            self.load()
            return "Record updated successfully."
        except sqlite3.Error as error:
            return "Error Updating Record: ", error
    
    #Deleting a record from the database
    #(DELETE)
    def delete(self, row):
        try:
            query = "DELETE FROM albums WHERE id = " + str(row) + ";"
            self.cursor.execute(query)
            self.sqlConnection.commit()
            self.load() #We are updating the memory list to no longer contain the dr...
            return "Record Deleted."
        except sqlite3.Error as error:
            return "Error Deleting Record: ", error
        
    
    
            
            
            