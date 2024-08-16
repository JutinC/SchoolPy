"""
School
Justin Choi
27 March 2024
CSP
Period 6
"""

#This is the model class module. This model represents or "Models" our data.

#Imports section (Preprocessor directives)
    
import tkinter as tk
import sqlite3

class School:
    
    def __init__(self):
        
        self.id = -1
        self.name = ""
        self.district = ""
        self.county = ""
        self.schoolRank = -1
        self.sports = ""
        self.arts = ""
        self.science = ""
        self.misc = ""
        self.teacher = ""