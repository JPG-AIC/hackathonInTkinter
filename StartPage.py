from tkinter import *
import tkinter.messagebox as tm
import UserLoginFrame, UserCreationFrame

class StartPage(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.start_label = Label(self, text="Start Page")
        self.login_as_user_button = Button(self, text="Login as User",  command=lambda: self.goto_user_login)
        self.login_to_group_button = Button(self, text="Login to Group", command=lambda: self.goto_user_creation)
        self.create_user_button = Button(self, text="Create User")
        self.create_group_button = Button(self, text="Create Group")

        self.start_label.grid(row=1)
        self.login_as_user_button.grid(row=2, sticky=E)
        self.login_to_group_button.grid(row=2, column=1)
        self.create_user_button.grid(row=3, sticky=E)
        self.create_group_button.grid(row=3, column=1)

        self.grid()

    def goto_user_login(self):
        login = UserLoginFrame(self.master)

    def goto_user_creation(self):
        root2 = Toplevel(self)
        group_login = UserCreationFrame(root2)

root = Tk()
mpg = StartPage(root)
root.mainloop()