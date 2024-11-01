import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        tst = BookLover('Michael','jme-sds','fiction')
        book = '1Q84'
        tst.add_book(book,5)
        actual = len(tst.book_list)
        expected = 1
        self.assertEqual(actual,expected)
        
    def test_2_add_book(self):
        tst = BookLover('Michael','jme-sds','fiction')
        book = 'The Diamond Age'
        tst.add_book(book,5)
        tst.add_book(book,3)
        actual = len(tst.book_list['book_name'].values[tst.book_list['book_name'].values==book])
        expected = 1
        self.assertTrue(actual,expected)
        
    def test_3_has_read(self):
        tst = BookLover('Michael','jme-sds','fiction')
        book = 'Kindred'
        tst.add_book(book,5)
        self.assertTrue(tst.has_read(book))
        
    def test_4_has_read(self):
        tst = BookLover('Michael','jme-sds','fiction')
        book = 'The Death of Ivan Ilych'
        tst.add_book('Savage Detectives',4)
        self.assertFalse(tst.has_read(book))
        
    def test_5_num_books_read(self):
        books = pd.DataFrame({
            'book_name':['Rainbows End','Crying of Lot 49','The Double','Neuromancer','Count of Monte Cristo'],
            'book_rating':[4,3,4,5,4]
        })
        tst = BookLover('Michael','jme-sds','fiction',book_list=books)
        tst.add_book('Sirens of Titan',5)
        tst.add_book('Foucault\'s Pendulum',4)
        expected = 7
        actual = tst.num_books
        self.assertEqual(actual,expected)
        
    def test_6_fav_books(self):
        tst = BookLover('Michael','jme-sds','fiction')
        tst.add_book('Go Tell It on the Mountain',5)
        tst.add_book('Inherent Vice',3)
        tst.add_book('The Picture of Dorian Gray',4)
        tst.add_book('Moby Dick',3)
        tst.add_book('The Baron in the Trees',2)
        favs = tst.fav_books()['book_rating']
        actual = len(favs[favs<4])
        expected = 0
        self.assertEqual(actual,expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)