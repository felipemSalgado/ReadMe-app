import customtkinter as ctk
from ReadMe_app import search

def book_search(master):
    new_window = ctk.CTkToplevel(master)
    new_window.title('Search Book')
    new_window.geometry('700x600')

    label_search = ctk.CTkLabel(new_window, text = 'Search Book : ')
    label_search.pack(pady = 5)

    entry_search = ctk.CTkEntry(new_window, placeholder_text='Enter book title...')
    entry_search.pack(pady=5)

    btn_search = ctk.CTkButton(new_window, text = 'Search', command = lambda : run_search())
    btn_search.pack(pady = 5)

    frame_list = ctk.CTkScrollableFrame(new_window, width = 400, height = 300)
    frame_list.pack(pady = 10, padx = 10, fill = 'both', expand = True)

    feedback = ctk.CTkLabel(new_window, text = '')
    feedback.pack(pady = 5)

    def run_search() :
        for widget in frame_list.winfo_children():
            widget.destroy() # limpa os dados antigos e adiciona os novos

        title = entry_search.get().strip()
        if not title :
            feedback.configure(text = 'Please enter a book title.', text_color = 'orange')
            return
        feedback.configure(text = 'Searching...', text_color = 'gray')
        results = search.search_book(title)

        if not results :
            feedback.configure(text = 'No books found.', text_color = 'red')
            return
        feedback.configure(text = f'Found {len(results)} results : ', text_color = 'green')

        for book in results :
            ctk.CTkLabel(
                frame_list,
                text = f'{book['title']} - {book['author']}',
                anchor = 'w'
            ).pack(pady = 3, padx = 5, fill = 'x')