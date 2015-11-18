from tkinter import *
from support import Group, read_db
import tkinter.messagebox as tm
import pickle


class GroupCreationFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.group_name_label = Label(self, text="Group Name")
        self.groupname_entry = Entry(self)

        self.submit_button = Button(self, text="Submit", command=self.submit_group_for_creation)

        self.group_name_label.grid(row=0, sticky=E)
        self.groupname_entry.grid(row=0, column=1)
        self.submit_button.grid(columnspan=2)

        self.grid()

    def submit_group_for_creation(self):
        group_name = self.groupname_entry.get()
        new_group = Group()
        # groups_dict = pickle.load(open("groups.p", "rb"))
        groups_dict = read_db()
        groups_dict.update({str(group_name): new_group})
        pickle.dump(groups_dict, open("groups.p", "wb"))
        tm.showinfo("Group Creation Successful", "Created group: {0}, {1}".format(group_name, groups_dict))

if __name__ == "__main__":
    root = Tk()
    gcf = GroupCreationFrame(root)
    root.mainloop()
