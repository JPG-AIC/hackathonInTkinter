from tkinter import *
import tkinter.messagebox as tm
import pickle
import support

users = {}


class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.username_label = Label(self, text="Username")
        self.password_label = Label(self, text="Password")

        self.user_entry = Entry(self)
        self.password_entry = Entry(self, show="*")

        self.username_label.grid(row=0, sticky=E)
        self.password_label.grid(row=1, sticky=E)
        self.user_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        self.login_button = Button(self, text="Login", command=self.login_button_clicked)
        self.login_button.grid(columnspan=2)

        self.new_user_button = Button(self, text="Create User", command=self.new_user_clicked)
        self.new_user_button.grid(columnspan=3)

        self.pack()

    def login_button_clicked(self):
        username = self.user_entry.get()
        password = self.password_entry.get()
        logins = LoginFrame.get_logins()
        try:
            val = logins[username]
            if val == password:
                tm.showinfo("Login info", "Welcome {0}".format(username))
            else:
                tm.showerror("Login Error", "Incorrect Password")
        except KeyError:
            tm.showerror("Login Error", "Invalid Username")

    @staticmethod
    def get_logins():
        load_dict = pickle.load(open("logins.p", "rb"))
        logins = load_dict['logins']
        return logins



class AddToGroupFrame(Frame):

    def __init__(self, master, group_name):
        super().__init__(master)

        self.group_name_label = Label(self, text="Add user to {0}".format(group_name))
        self.user_name_entry = Entry(self)

        self.pack()


def save_all():
    save_dict = {'users', users}


root = Tk()
lf = LoginFrame(root)
root.mainloop()


class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.username_label = Label(self, text="Username")
        self.password_label = Label(self, text="Password")
        self.username_entry = Entry(self)
        self.password_entry = Entry(self)
        self.pack()


def add_user(username, user):
    global users
    users[username] = user