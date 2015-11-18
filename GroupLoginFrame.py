from tkinter import *
from support import get_groups
import tkinter.messagebox as tm


class GroupLoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.group_login_label = Label(self, text="Group ID")
        self.group_login_entry = Entry(self)
        self.submit_button = Button(self, text="Login to Group", command=self.login_to_group)

        self.group_login_label.grid(row=0, sticky=E)
        self.group_login_entry.grid(row=0, column=1)
        self.submit_button.grid(columnspan=1)

        self.grid()

    def login_to_group(self):
        print("Entering login_to_group")
        group_name = self.group_login_entry.get()
        group = get_groups()
        print("Logging in to group: {0}".format(group_name))
        try:
            val=group[group_name]
            tm.showinfo("Group Login Info", "Welcome to group {0}".format(group_name))
        except KeyError:
            tm.showerror("Group Login Error", "Invalid Group Name")


if __name__ == "__main__":
    root = Tk()
    ucf = GroupLoginFrame(root)
    root.mainloop()
