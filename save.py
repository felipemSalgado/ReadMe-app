import os
import json
import customtkinter as ctk

books_folder = os.path.join('data', 'books')
watchlist_folder = os.path.join('data', 'watchlist')

os.makedirs(books_folder, exist_ok = True)
os.makedirs(watchlist_folder, exist_ok = True)

def save_book(book : dict):
    title = book.get('title', 'untitled').replace(' ', '_')
    path = os.path.join(books_folder, f'{title}.json')
    try :
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(book, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Writing to file failed: {e}')
def list_books():
    books = []
    for file in os.listdir(books_folder):
        if file.endswith('.json'):
            path = os.path.join(books_folder, file)
            try :
                with open(path, 'r', encoding='utf-8') as f:
                    books.append(json.load(f))
            except Exception as e:
                print(f'Writing to file failed {e}')
    return books

def save_watchlist_item(item: dict):
    title = item.get('book', 'untitled').replace(' ', '_')
    path = os.path.join(watchlist_folder, f'{title}.json')
    try :
        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump(item, f, indent = 4, ensure_ascii = False)
    except Exception as e:
        print(f'Writing to file failed : {e}')
def list_watchlist():
    watchlist = []
    for file in os.listdir(watchlist_folder):
        if file.endswith('.json'):
            path = os.path.join(watchlist_folder, file)
            try:
                with open(path, 'r', encoding = 'utf-8') as f:
                    watchlist.append(json.load(f))
            except Exception as e:
                print(f'Reading file failed : {e}')
    return watchlist

def delete_book(title):
    filename = f'{title.replace(' ', '_')}.json'
    path = os.path.join(books_folder,filename)

    if os.path.exists(path):
        os.remove(path)
def edit_book(old_title, new_data):
    old_filename = f'{old_title.replace(' ', '_')}.json'
    path = os.path.join(books_folder, old_filename)

    if os.path.exists(path):
        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump(new_data, f, indent = 4, ensure_ascii = False)
def delete_and_refresh(title, parent_frame):
    delete_book(title)
    for widget in parent_frame.winfo_children():
        widget.destroy()
    update_books = list_books()
def open_edit_window(book, parent):
    edit_window = ctk.CTkToplevel(parent)
    edit_window.title('Edit Book')
    edit_window.geometry('400x370')

    entry_title = ctk.CTkEntry(edit_window)
    entry_title.insert(0, book.get('title', ''))
    entry_title.pack(pady = 5)
    entry_author = ctk.CTkEntry(edit_window)
    entry_author.insert(0, book.get('author', ''))
    entry_author.pack(pady = 5)
    entry_start_date = ctk.CTkEntry(edit_window)
    entry_start_date.insert(0, book.get('start date', ''))
    entry_start_date.pack(pady = 5)
    entry_end_date = ctk.CTkEntry(edit_window)
    entry_end_date.insert(0, book.get('end date', ''))
    entry_end_date.pack(pady = 5)
    entry_review = ctk.CTkTextbox(edit_window, width = 300, height = 150)
    entry_review.insert('1.0', book.get('review', ''))
    entry_review.pack(pady = 5)
    def save_charges():
        update_book = {
            'title' : entry_title.get(),
            'author' : entry_author.get(),
            'start_date' : entry_start_date.get(),
            'end_date' : entry_end_date.get(),
            'review' : entry_review.get('1.0', 'end').strip()
        }
        edit_book(book.get('title'), update_book)
        edit_window.destroy()
    ctk.CTkButton(edit_window, text = 'Save', command = save_charges).pack(pady = 10)

def delete_watch_item(title):
    filename = f'{title.replace(' ', '_')}.json'
    path = os.path.join(watchlist_folder, filename)
    if os.path.exists(path):
        os.remove(path)
def edit_watch(old_title, new_data):
    old_filename = f'{old_title.replace(' ', '_')}.json'
    path = os.path.join(watchlist_folder, old_filename)

    if os.path.exists(path):
        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump(new_data, f, indent = 4, ensure_ascii = False)
def delete_wath_and_refresh(title, parent_frame):
    delete_watch_item(title)
    for widget in parent_frame.winfo_children():
        widget.destroy()
    update_watchlist = list_watchlist()
def open_edit_watch(watchlist, parent):
    edit_window = ctk.CTkToplevel(parent)
    edit_window.title('Edit WatchList')
    edit_window.geometry('400x350')

    entry_title = ctk.CTkEntry(edit_window)
    entry_title.insert(0, watchlist.get('book', ''))
    entry_title.pack(pady = 5)
    entry_author = ctk.CTkEntry(edit_window)
    entry_author.insert(0, watchlist.get('author', ''))
    entry_author.pack(pady = 5)
    entry_note = ctk.CTkTextbox(edit_window, width = 300, height = 150)
    entry_note.insert('1.0', watchlist.get('note', ''))
    entry_note.pack(pady = 5)

    def save_charges():
        update_watch = {
            'book': entry_title.get(),
            'author' : entry_author.get(),
            'note' : entry_note.get('1.0', 'end').strip()
        }
        edit_watch(watchlist.get('book'), update_watch)
        edit_window.destroy()
    ctk.CTkButton(edit_window, text='Save', command=save_charges).pack(pady=10)