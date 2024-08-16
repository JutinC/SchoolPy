"""
Chess database
Justin Choi and Alex Lou
15 March 2023
IDT
Period 3
"""

#This is the Model sections with is our data.
#Alex Lou did this section
class Game:
    
    def __init__(self):
        #Game values
        self.id = -1
        self.player = ""
        self.moveList = ""
        self.gameType = ""
        self.result = ""
        self.comments = ""
