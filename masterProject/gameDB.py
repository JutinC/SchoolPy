""" Alex Lou and Justin Choi
IDT Period 3
20 march 2023
games DB """

# imports
import mysql.connector
from game import Game

#Container class
#Alex Lou will be doing this container class
class GameDB:
    #We add playerDB in order to keep the connection together in the same instance 
    def __init__(self, playerDB):
        
        self.playerDB = playerDB
        #Makes a list for each game 
        self.records = []
        
        #Object hold the class as self.game
        self.game = Game()
 
         
#CRUD Section
#Queries must have try except for backup
#ALEX LOU is doing the C and R of crud 

    #CREATE    
    def create_game(self):
        try:
            #Query to insert game
            query = "INSERT INTO game (player, moveList, gameType, result, comments) VALUES (%s, %s, %s, %s, %s)"
            #Value from controller
            values = [self.game.player, self.game.moveList, self.game.gameType, self.game.result, self.game.comments]   
            
            self.playerDB.cursor.execute(query, values)
            self.read_games()
            
            self.playerDB.conn.commit()
            
            return f"{self.playerDB.cursor.rowcount} record inserted."
        
        
        except mysql.connector.Error as error:
            return f"Error in insertion:  {error}"

    def read_games(self):
        
        try:
            #Query to read the game
            query = "Select * FROM game"
            self.playerDB.cursor.execute(query)
            
            #Retrieve all records into our list
            self.records = self.playerDB.cursor.fetchall()
            
        except mysql.connector.Error as error:
                return f"Error connecting: {error}" 
            
            


#JUSTIN CHOI is doing the update and delete for the crud

    #UPDATE
    def update(self):
        try: 
            #Query to update the values
            query = "UPDATE game SET " + \
                    "player = %s, " + \
                    "moveList = %s, " + \
                    "gameType = %s, " + \
                    "result = %s, " + \
                    "comments = %s " + \
                    "WHERE id = %s"
            #gets from controller
            values = [self.game.player, self.game.moveList, self.game.gameType, self.game.result, self.game.comments, self.game.id]
            self.playerDB.cursor.execute(query, values)   
            self.playerDB.conn.commit()
            self.read_games()
            
            return "Updated"
        
        except mysql.connector.Error as error:
            return f"Error in updating record: {error}"
    
    #DELETE
    def delete(self, id):
        try:
            #query to delete
            query = "DELETE FROM game WHERE id = %s;"
            self.playerDB.cursor.execute(query, (id,))
            self.playerDB.conn.commit()
            self.read_games()
            
            return "Record Deleted."
            
        except mysql.connector.Error as error:
            return f"Error deleting game: {error}"
