import csv
import os 

class Account:
    def __init__(self,person):
        pass

class Person:

    def __init__(self,name = None, age = None, gender = None):
        if not name or not age or not gender:
            self.set_info()
        else:
            self.name = name
            self.age = age
            self.gender = gender

    def set_info(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")
    
    def get_info(self):
        return {'name': self.name, 'age' : self.age, 'gender' : self.gender}

choice = True

while choice != "exit":
    choice = input("Your choice\n> ")
    if choice == "create person":
        new = Person()
        
        with open('persons.csv','w',newline='') as file:
            print(new.get_info())
            writer = csv.DictWriter(file,fieldnames = list(new.get_info()),delimiter="****")
            if not file:
                writer.writeheader()
            writer.writerow(new.get_info()) 
    elif choice == "show persons":
        with open('persons.csv','r') as file:
            person_data =  csv.reader(file,delimiter='####')
        print(person_data)
    