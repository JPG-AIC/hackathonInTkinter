from tkinter import *
import tkinter.messagebox as tm
from support import get_logins


class UserLoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.username_label = Label(self, text="Username")
        self.password_label = Label(self, text="Password")

        self.username_entry = Entry(self)
        self.password_entry = Entry(self, show="~")

        self.username_label.grid(row=0, sticky=E)
        self.password_label.grid(row=1, sticky=E)
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        self.submit_button = Button(self, text="Submit", command=self.login_button_clicked)
        self.submit_button.grid(columnspan=3)

        self.grid()

    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        login = get_logins()

        try:
            val = login[username]
            if val == password:
                tm.showinfo("Login Info", "Welcome {0}".format(username))
            else:
                tm.showerror("Login Error", "Invalid Password")
        except KeyError:
            tm.showerror("Login Error", "Invalid Username")

if __name__ == "__main__":
    root = Tk()
    ulf = UserLoginFrame(root)
    root.mainloop()