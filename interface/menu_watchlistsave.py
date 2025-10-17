import customtkinter as ctk
from ReadMe_app.save import list_watchlist, delete_watch_item, open_edit_watch

def save_watchlist(master):
    new_window = ctk.CTkToplevel(master)
    new_window.title('List watchlist')
    new_window.geometry('500x500')

    label_title = ctk.CTkLabel(new_window, text = 'Your Watchlist', font = ('Arial', 18))
    label_title.pack(pady = 10)
    frame_list = ctk.CTkScrollableFrame(new_window, width = 400, height = 350)
    frame_list.pack(pady = 10, padx = 10, fill = 'both', expand = True)

    watchlist = list_watchlist()

    if not watchlist:
        ctk.CTkLabel(frame_list, text = 'No books found.').pack(pady = 10)
        return

    for watch in watchlist:
        title = watch.get('book', 'Untitled')
        author = watch.get('author', 'Unknown')
        note = watch.get('note', 'N/A')

        watchlist_frame = ctk.CTkFrame(frame_list)
        watchlist_frame.pack(pady = 5, padx = 10, fill = 'x')
        title_label = ctk.CTkLabel(watchlist_frame, text = f'{title} — {author}', anchor = 'w')
        title_label.pack(pady = 5, padx = 10, fill = 'x')
        header_frame = ctk.CTkFrame(watchlist_frame, fg_color='transparent')
        header_frame.pack(fill='x', padx=5, pady=2)
        details_frame = ctk.CTkFrame(watchlist_frame)
        details_frame.pack(pady = 5, padx = 10, fill = 'x')
        details_frame.pack_forget()

        ctk.CTkButton(
            header_frame, text = 'Edit', width = 50,
            command = lambda w = watch : open_edit_watch(w,frame_list)
        ).pack(side = 'right', padx = 5)
        ctk.CTkButton(
            header_frame, text = 'Delete', width = 60,
            fg_color = 'red', hover_color = '#b00000',
            command = lambda t = watch.get('book', 'Untitled') : delete_watch_item(t)).pack(side = 'right', padx = 5)

        ctk.CTkLabel(details_frame, text = f'Note : {note}').pack(anchor = 'w', padx = 5)

        def toggle_details(frame = details_frame):
            if frame.winfo_ismapped():
                frame.pack_forget()
            else:
                frame.pack(pady = 5, padx = 10, fill = 'x')

        title_label.bind('<Button-1>', lambda e, f = details_frame : toggle_details(f))

    ctk.CTkButton(new_window, text = 'Close', command = new_window.destroy).pack(pady = 5)