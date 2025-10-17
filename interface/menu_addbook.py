import customtkinter as ctk
from ReadMe_app import save

def book_menu(master):
    new_window = ctk.CTkToplevel(master)
    new_window.title('Add book')
    new_window.geometry('700x600')

    label_title = ctk.CTkLabel(new_window, text='Title : ')
    label_title.pack(pady = 5)
    entry_title = ctk.CTkEntry(new_window)
    entry_title.pack(pady = 5)

    label_author = ctk.CTkLabel(new_window, text='Author : ')
    label_author.pack(pady = 5)
    entry_author = ctk.CTkEntry(new_window)
    entry_author.pack(pady = 5)

    label_start_date = ctk.CTkLabel(new_window, text='Start  : ')
    label_start_date.pack(pady = 5)
    entry_start_date = ctk.CTkEntry(new_window)
    entry_start_date.pack(pady = 5)

    label_end_date = ctk.CTkLabel(new_window, text='End date : ')
    label_end_date.pack(pady = 5)
    entry_end_date = ctk.CTkEntry(new_window)
    entry_end_date.pack(pady = 5)

    label_review = ctk.CTkLabel(new_window, text='Review : ')
    label_review.pack(pady = 5)
    entry_review = ctk.CTkTextbox(new_window, width = 500, height = 150)
    entry_review.pack(pady = 5)

    feedback = ctk.CTkLabel(new_window, text='')
    feedback.pack(pady = 5)

    def storage():
        book = {
            'title' : entry_title.get(),
            'author' : entry_author.get(),
            'start_date' : entry_start_date.get(),
            'end_date' : entry_end_date.get(),
            'review' : entry_review.get('1.0', 'end-1c')
        }
        save.save_book(book)
        feedback.configure(text='✅ Book successfully saved!', text_color='green')
        new_window.destroy()

    btn_save = ctk.CTkButton(new_window, text= 'Save', command = storage)
    btn_save.pack(pady = 10)

