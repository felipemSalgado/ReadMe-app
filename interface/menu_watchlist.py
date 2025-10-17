import customtkinter as ctk
from ReadMe_app import save
from interface.menu_watchlistsave import save_watchlist

def watchlist_book(master):
    new_window = ctk.CTkToplevel(master)
    new_window.title('Watchlist')
    new_window.geometry('700x600')

    label_view = ctk.CTkButton(new_window, text = 'View watchlist', command = lambda: save_watchlist(master))
    label_view.pack(pady = 5)

    label_tile = ctk.CTkLabel(new_window, text = 'Title : ')
    label_tile.pack(pady = 5)
    entry_title = ctk.CTkEntry(new_window)
    entry_title.pack(pady = 5)

    label_author = ctk.CTkLabel(new_window, text = 'Author : ')
    label_author.pack(pady = 5)
    entry_author = ctk.CTkEntry(new_window)
    entry_author.pack(pady = 5)

    label_note = ctk.CTkLabel(new_window, text = 'Note : ')
    label_note.pack(pady = 5)
    entry_note = ctk.CTkTextbox(new_window, width = 400, height = 150)
    entry_note.pack(pady = 5)

    def storage():
        watchlist = {
            'book' : entry_title.get(),
            'author' : entry_author.get(),
            'note' : entry_note.get('1.0', 'end-1c')
        }
        save.save_watchlist_item(watchlist)
        new_window.destroy()

    btn_save = ctk.CTkButton(new_window, text = 'Save', command = storage)
    btn_save.pack(pady = 5)