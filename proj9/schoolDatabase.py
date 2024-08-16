"""
School database
Justin Choi
15 March 2023
CSP
Period 6
"""

#External Libraries
import mysql.connector
from school import School


#Container class
#Justin Choi this container class
class SchoolDatabase:
    
    def __init__(self):     
        #Connection Flag
        self.connected = False
        
            
        #Makes a list for each school 
        self.records = []
       
        #Object hold the class as self.school
        self.school = School()
   
        
        
#Connections section
#Connection must have try except for backup
    def connect(self):
        try:
            #Connecting to a certain instance in the sql
            self.conn = mysql.connector.connect(host='127.0.0.1', user='root', port=3306, password='chexmix14',
                                                    database="sql_workbench", auth_plugin='mysql_native_password')
            #Create cursor
            self.cursor = self.conn.cursor()
            #Reads the schools
            self.read_schools()
            
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
    def create_school(self):
        try:
            #makes a query to run
            query = "INSERT INTO school (name, district, county, schoolRank, sports, arts, science, misc, teacher) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            #Sets values from controller
            values = [self.school.name, self.school.district, self.school.county, self.school.schoolRank, self.school.sports, self.school.arts, self.school.science, self.school.misc, self.school.teacher] 
            
            #Executes function
            print("Here?")
            self.cursor.execute(query, values)
            self.read_schools()
            
            self.conn.commit()
            
            #Finds the id and returns that
            return f"record {self.cursor.rowcount} inserted."
           
        except mysql.connector.Error as error:
            return f"Error in insertion:  {error}"

    #READ
    def read_schools(self):
        
        try:
            #Query to select everything
            query = "Select * FROM school"
            self.cursor.execute(query)
            
            #Retrieve all records
            self.records = self.cursor.fetchall()
                    
        except mysql.connector.Error as error:
                return f"Error connecting: {error}" 
            
            


#ALEX LOU is doing the update and delete for the crud

    
    #UPDATE
    def update(self):
        try: 
            #Query to change the values of the school
            query = "UPDATE school SET " + \
                    "name = %s, " + \
                    "district = %s, " + \
                    "county = %s, " + \
                    "schoolRank = %s, " + \
                    "sports = %s, " + \
                    "arts = %s, " + \
                    "science = %s, " + \
                    "misc = %s, " + \
                    "teacher = %s" + \
                    "WHERE id = %s"
            #finds values from controller 
            values = (self.school.name, self.school.district, self.school.county, self.school.schoolRank, self.school.sports, self.school.arts, self.school.science, self.school.misc, self.school.teacher, self.school.id)
                    
            self.cursor.execute(query, values)
            self.conn.commit()
            self.read_schools()
            
            return "Updated"
        
        except mysql.connector.Error as error:
            return f"Error in updating record: {error}"
    
    #DELETE
    def delete(self, id):
        try:
            print(id)
            query = "DELETE FROM school WHERE id = " + str(id) + ";"
            self.cursor.execute(query)
            self.conn.commit()
            self.read_schools()
            
            return "Record Deleted."
            
        except mysql.connector.Error as error:
            return f"Error deleting school: {error}"