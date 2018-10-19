#QUESTION-4
class movieDetails:
    def __init__(self,artist,year,rating):
        self.name=artist
        self.year=year
        self.rating=rating
    
    def Add(self,movie):
        self.moviename=movie
    def Display(self):
        print(self.name)
        print(self.year)
        print(self.rating)
        print(self.moviename)
details=movieDetails(input("enter the artist's name:- "),int(input("enter the year:- ")),int(input("enter the rating:- ")))
details.Add(input("enter the movie:- "))
details.Display()
