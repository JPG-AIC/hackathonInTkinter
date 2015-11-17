import pickle

def get_logins():
    return pickle.load(open("logins.p", "rb"))

class Group(object):

    def __init__(self, group_id):
        self.group_id = group_id
        self.users = []


class User(object):

    def __init__(self, user_id, password):
        self.group = Group('None')
        self.login = {user_id, password}
