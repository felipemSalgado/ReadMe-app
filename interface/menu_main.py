import customtkinter as ctk
# from ReadMe_app import save
from interface.menu_addbook import book_menu
from interface.menu_listbook import list_menu
from interface.menu_searchbook import book_search
from interface.menu_watchlist import watchlist_book

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Main Menu - Alpha 1.0')
        self.geometry('500x450')
        ctk.set_appearance_mode('dark')

        title = ctk.CTkLabel(self, text = 'Book Manager', font=('Arial', 18))
        title.pack(pady = 20)

        btn_add = ctk.CTkButton(self, text = 'Add a book : ', command = lambda: book_menu(self))
        btn_add.pack(pady = 20 )

        btn_watchlist = ctk.CTkButton(self, text = 'Add to Watchlist : ', command = lambda: watchlist_book(self))
        btn_watchlist.pack(pady = 20)

        btn_listbook = ctk.CTkButton(self, text = 'View Books : ', command = lambda: list_menu(self))
        btn_listbook.pack(pady = 20)

        btn_search = ctk.CTkButton(self, text = 'Search Book : ', command = lambda: book_search(self))
        btn_search.pack(pady = 20)

        btn_quit = ctk.CTkButton(self, text = 'Quit : ', command = self.quit)
        btn_quit.pack(pady = 20)