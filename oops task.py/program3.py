class Book:
    def __init__(self ,title,author):
        self.title=title
        self.author=author
    def book(self):
        print("Title:",self.title)
        print("author:",self.author)
s1=Book("paradise","Nani")  
   
s1.book()
print(f":{s1.title},{s1.author}")


 

