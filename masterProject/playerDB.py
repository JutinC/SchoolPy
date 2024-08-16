
"""
Chess database
Justin Choi and Alex Lou
15 March 2023
IDT
Period 3
"""

#External Libraries
import mysql.connector
from player import Player
# from gameDB import GameDB


#Container class
#Justin Choi this container class
class PlayerDB:
    
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
            #Connecting to a certain instance in the sql
            self.conn = mysql.connector.connect(host = '192.168.0.153', database = 'chess',  user = 'ariel', password = 'jchs')
            
            #Create cursor
            self.cursor = self.conn.cursor()
            #Reads the players
            self.read_players()
            
            #Returns to show in terminal that it works
            return  "Connected"
        
        except mysql.connector.Error as error:
            return f"Error connecting: {error}"
    
    def disconnect(self):
        
        if(self.conn):
            #Closes the conneciton instance
            self.cursor.close()
            self.conn.close()
            
            return "Disconnected"
        else:
            return "There was not a connection to disconnect"    


#CRUD Section
#Queries must have try except for backup
#JUSTIN CHOI is doing the C and R of crud 
     
    
    #CREATE
    def create_player(self):
        try:
            #makes a query to run
            query = "INSERT INTO player (name, age, country, blitzRating, blitzRank, rapidRating, rapidRank, classicalRating, classicalRank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            #Sets values from controller
            values = [self.player.name, self.player.age, self.player.country, self.player.blitzRating, self.player.blitzRank, self.player.rapidRating, self.player.rapidRank, self.player.classicalRating, self.player.classicalRank]   
            
            #Executes function
            self.cursor.execute(query, values)
            self.read_players()
            
            self.conn.commit()
            
            #Finds the id and returns that
            return f"record {self.cursor.rowcount} inserted."
           
        except mysql.connector.Error as error:
            return f"Error in insertion:  {error}"

    #READ
    def read_players(self):
        
        try:
            #Query to select everything
            query = "Select * FROM player"
            self.cursor.execute(query)
            
            #Retrieve all records
            self.records = self.cursor.fetchall()
                    
        except mysql.connector.Error as error:
                return f"Error connecting: {error}" 
            
            


#ALEX LOU is doing the update and delete for the crud

    
    #UPDATE
    def update(self):
        try: 
            #Query to change the values of the player
            query = "UPDATE player SET " + \
                    "name = %s, " + \
                    "age = %s, " + \
                    "country = %s, " + \
                    "blitzRating = %s, " + \
                    "blitzRank = %s, " + \
                    "rapidRating = %s, " + \
                    "rapidRank = %s, " + \
                    "classicalRating = %s, " + \
                    "classicalRank = %s" + \
                    "WHERE id = %s"
            #finds values from controller 
            values = (self.player.name, self.player.age, self.player.country, self.player.blitzRating, self.player.blitzRank, self.player.rapidRating, self.player.rapidRank, self.player.classicalRating, self.player.classicalRank, self.player.id)
                    
            self.cursor.execute(query, values)
            self.conn.commit()
            self.read_players()
            
            return "Updated"
        
        except mysql.connector.Error as error:
            return f"Error in updating record: {error}"
    
    #DELETE
    def delete(self, id):
        try:
            print(id)
            query = "DELETE FROM player WHERE id = %s;"
            self.cursor.execute(query, (id,))
            self.conn.commit()
            self.read_players()
            
            return "Record Deleted."
            
        except mysql.connector.Error as error:
            return f"Error deleting player: {error}"