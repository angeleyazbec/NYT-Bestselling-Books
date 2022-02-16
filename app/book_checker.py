class BookChecker:
    def __init__(self,b_list):
        self.book_number=0
        self.book_list=b_list
        self.current_book=None
        

    def still_has_book(self):
        return self.book_number<len(self.book_list)

    def nex_book(self):
        return self.book_number<len(self.book_list)
        self.current_book=self.book_list[self.book_number]
        self.book_number+=1


    
        
