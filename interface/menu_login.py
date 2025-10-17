import customtkinter as ctk

class LoginApp(ctk.CTk):
    def check_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.title('Login')
        self.geometry('500x500')

        self.label_user = ctk.CTkLabel(self, text='User')
        self.label_user.pack(pady=10)
        self.entry_user = ctk.CTkEntry(self, placeholder_text='Enter your username : ')
        self.entry_user.pack(pady=10)

        self.label_password = ctk.CTkLabel(self, text='Password')
        self.label_password.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self, placeholder_text='Enter your password : ')
        self.entry_password.pack(pady=10)

        "ctk.CTkButton(app, text='Login/Create User', command=)"

        self.feedback = ctk.CTkLabel(self,text='')
        self.feedback.pack(pady=10)

        self.mainloop()