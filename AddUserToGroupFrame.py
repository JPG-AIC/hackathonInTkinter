from tkinter import *
import tkinter.messagebox as tm
import pickle
from support import read_db, Group


class AddUserToGroupFrame(Frame):

    def __init__(self, master, group):
        super().__init__(master)

        self.current_group = group

        self.username_label = Label(self, text="User to be added")

        self.username_entry = Entry(self)
        self.submit_button = Button(self, text="Submit", command=self.submit_user)

        self.username_label.grid(row=0, sticky=E)
        self.username_entry.grid(row=0, column=1)
        self.submit_button.grid(columnspan=1)

        self.grid()

    def submit_user(self):
        username = self.username_entry.get()

        users = read_db()
        real_users = users['users']

        self.current_group.add_user(real_users[username])


if __name__ == "__main__":
    root = Tk()
    a = Group()
    gcf = AddUserToGroupFrame(root, a)
    root.mainloop()