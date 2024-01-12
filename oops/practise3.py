class book:
    def __init__(self,price,author,title):
        self.price=price
        self.author=author
        self.title=title
    def show_details(self):
        print(self.price)
        print(self.author)
        print(self.title)
b=book(2000,'aditya',"pcode")
(b.show_details())