import customtkinter as ctk
from ReadMe_app.save import list_books,delete_and_refresh, open_edit_window

def list_menu(master):
    new_window = ctk.CTkToplevel(master)
    new_window.title('Book List')
    new_window.geometry('500x500')

    label_title = ctk.CTkLabel(new_window, text = 'Your Books', font = ('Arial', 18))
    label_title.pack(pady = 10)

    frame_list = ctk.CTkScrollableFrame(new_window, width = 400, height = 300)
    frame_list.pack(pady = 10, padx = 10, fill = 'both', expand = True)

    books = list_books()

    if not books:
        ctk.CTkLabel(frame_list, text = 'No books found.').pack(pady = 10)
        return
    for book in books:
        title = book.get('title', 'Untitled')
        author = book.get('author', 'Unknown')
        start = book.get('start_date', 'N/A')
        end = book.get('end_date', 'N/A')
        review = book.get('review', 'N/A')

        book_frame = ctk.CTkFrame(frame_list)
        book_frame.pack(pady = 5, padx = 10, fill = 'x')
        header_frame = ctk.CTkFrame(book_frame, fg_color = 'transparent')
        header_frame.pack(fill = 'x', padx = 5, pady = 2)
        title_label = ctk.CTkLabel(book_frame, text = f'{title} — {author}', anchor = 'w')
        title_label.pack(fill = 'x', pady = 5, padx = 5)

        ctk.CTkButton(
            header_frame, text = 'Edit', width = 50,
            command = lambda b = book : open_edit_window(b, frame_list)
        ).pack(side = 'right', padx = 5)
        ctk.CTkButton(
            header_frame, text = 'Delete', width = 60,
            fg_color = 'red', hover_color = '#b00000',
            command = lambda t = title : delete_and_refresh(t, frame_list)).pack(side = 'right', padx = 5)


        details_frame = ctk.CTkFrame(book_frame)
        details_frame.pack(fill = 'x', pady = 5, padx = 10)
        details_frame.pack_forget()

        ctk.CTkLabel(details_frame, text = f'Start date : {start}').pack(anchor = 'w')
        ctk.CTkLabel(details_frame, text = f'End date : {end}').pack(anchor = 'w')
        ctk.CTkLabel(details_frame, text = f'Review : {review}').pack(anchor = 'w')

        def toggle_details(frame = details_frame):
            if frame.winfo_ismapped():
                frame.pack_forget()
            else:
                frame.pack(fill = 'x', pady = 5, padx = 10)

        title_label.bind('<Button-1>', lambda e, f = details_frame : toggle_details(f))

    ctk.CTkButton(new_window, text = 'Close', command = new_window.destroy).pack(pady = 10)

