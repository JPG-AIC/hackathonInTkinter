import pickle
import support

a = support.User('test', 'lol')
b = support.Group()

users = {'test': a}
groups = {'test': b}

things_to_pickle = {'users': users, 'groups': groups}

pickle.dump(things_to_pickle, open("pickle_db.p", "wb"))