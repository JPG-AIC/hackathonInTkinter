from tkinter import *
import pickle


class UserCreationFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.username_label = Label(self, text="Username")
        self.password_label = Label(self, text="Password")

        self.username_entry = Entry(self)
        self.password_entry = Entry(self)

        self.username_label.grid(row=0, sticky=E)
        self.password_label.grid(row=1, sticky=E)
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        self.debug_label = Label(text="Debug:")
        self.debug_label.grid(columnspan=4)

        self.create_button = Button(self, text="Create User", command=self.create_user)
        self.create_button.grid(columnspan=3)

        self.grid()

    def create_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        logins_dict = pickle.load(open("logins.p", "rb"))
        logins_dict.update({str(username): str(password)})
        pickle.dump(logins_dict, open("logins.p", "wb"))

        self.debug_label.configure(text="Debug: {0}, {1}".format((logins_dict[username]), username))

if __name__=="__main__":
    root = Tk()
    ucf = UserCreationFrame(root)
    root.mainloop()
