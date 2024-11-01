import pandas as pd
import numpy as np

class BookLover:
    def __init__(self,name,email,fav_genre,num_books=0,book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.book_list=book_list
        self.num_books=len(self.book_list)
                 
    def add_book(self,book_name,rating):
        assert isinstance(rating,int) * (rating<=5) * (rating>=0), "Rating must be integer between 0 and 5."
        if book_name not in self.book_list['book_name'].values.tolist():      
            new_book = pd.DataFrame({
                'book_name':[book_name],
                'book_rating':[rating]
            })

            self.book_list = pd.concat([self.book_list,new_book],ignore_index=True)
            self.num_books+=1   
        else:
            print(f"Book was not added. {book_name} is already in book list.")
            
    def has_read(self,book_name):
        return book_name in self.book_list['book_name'].values.tolist()
                 
    def num_books_read(self):
        self.num_books = len(self.book_list)
        return self.num_books
                 
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)