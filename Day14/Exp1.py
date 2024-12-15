class Book:
    def __init__(self,title:str,author:str,year:int):
        self.title = title
        self.author = author
        self.year = year
    def display(self) -> int:
        print(f'''
        Title: {self.title}
        Author: {self.author}
        Published: {self.year}      
        ''')
        return "Samiul"

    def __str__(self):
        return self.title


alchemist = Book("The Alchemist","Publo qohelho","1988")
alchemist.display()
print(alchemist)
