"""
Example Tkinter Database Program
Justin Choi
27 January 2023
IDT
Period 3
"""

#This is the model class module. This model represents or "Models" our data.

#Imports section (Preprocessor directives)
    
import tkinter as tk
import sqlite3

class Album:
    
    def __init__(self):
        
        self.id = -9
        self.artist = ""
        self.title = ""
        self.genre = ""
        self.rating = 0
        
        