"""
Chess database
Justin Choi and Alex Lou
15 March 2023
IDT
Period 3
"""

#External Libraries
import sqlite3
from masterProject.player import Player


#Container class
#Justin Choi will be doing this whole container class
class PlayerDab:
    
    def __init__(self):
        
        #Connection Flag
        self.connected = False
        
        #Makes a list for each player 
        self.records = []
        
        #Object hold the class as self.player
        self.player = Player()
        
#Connections section
#Connection must have try except for backup
    def connect(self):
        try:
            #Connecting to a certain time in the sql
            self.conn = sqlite3.connect("player.sqlite")
            
            #Create cursor
            self.cursor = self.conn.cursor()
            
            #Returns to show in terminal that it works
            return  "Connected"
        
        except sqlite3.Error as error:
            return "Error Connecting", error
    
    def disconnect(self):
        
        if(self.conn):
            self.cursor.close()
            self.conn.close()
            
            return "Disconnected"
        else:
            return "There was not a connection to disconnect"    


#CRUD Section
#Queries must have try except for backup
#JUSTIN CHOI is doing the C and R of crud 

#############################################################################
        
    #This is CREATE of crud adding in the players to the database
    #There is autoincrement in the sql so no need for the ID
    
    def create_player(self):
        try:
            query = "INSERT INTO players (name, age, country, blitzRating, blitzRank, rapidRating, rapidRank, classicalRating, classicalRank) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
            
            values = (self.player.name, self.player.age, self.player.country, self.player.blitzRating, self.player.blitzRank, self.player.rapidRating, self.player.rapidRank, self.player.classicalRating, self.player.classicalRank)
            
            self.cursor.execute(query, values)
            
            self.conn.commit()
            return f"{self.mycursor.rowcount} record inserted."
        
        
        except sqlite3.Error as error:
            return "Error Connecting", error

    def read_players(self):
        
        try:
            query = "Select * FROM players;"
            self.cursor.execute(query)
            
            #Retrieve all records into our lsit as a list of TUPLES
            res = self.cursor.fetchall()
            
            for row in res:            #print(self.gamers) #Daemon print for debug
                print(row)                    #return ""
                
        except sqlite3.Error as error:
            return "Error Connecting", error
            
            


#Alex Lou is doing the update and delete for the crud

    #This is the UPDATE part which updates the values in the database
    def update(self):
        try: 
            query = "UPDATE player SET " + \
                    "name = '" + self.name + "', " + \
                    "age = '" + self.name + "', " + \
                    "country = '" + self.name + "', " + \
                    "blitzRating = '" + self.name + "', " + \
                    "blitzRank = '" + self.name + "', " + \
                    "rapidRating = '" + self.name + "', " + \
                    "rapidRank = '" + self.name + "', " + \
                    "classicalRating = '" + self.name + "', " + \
                    "classicalRank = '" + self.name + "';"
                    
            self.cursor.execute(query)
            self.conn.commit()
            return "Updated"
        
        except sqlite3.Error as error:
            return "Error Connecting", error
    
    #This is the DELETE part which deletes the player
    def delete(self, row):
        try:
            query = "DELETE FROM players WHERE id = " + str(row) + ";"
            self.cursor.execute(query)
            self.conn.commit()
           
            return "Record Deleted."
        
        except sqlite3.Error as error:
            return "Error Connecting", error