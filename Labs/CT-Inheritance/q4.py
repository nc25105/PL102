class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Reading '{self.title}' author: {self.author}.")

class EBook(Book):
    def download(self):
        print(f"Downloading '{self.title}'..")

class PrintedBook(Book):
    def flip_page(self):
        print("Next page..")

mein_kampf = EBook("Mein Kampf", "Radiant Fitter")
harrypotter_book = PrintedBook("Harry Potter and the philosopher's stone", "J.K. Rowling")

mein_kampf.download()
mein_kampf.read()

harrypotter_book.read()
harrypotter_book.flip_page()