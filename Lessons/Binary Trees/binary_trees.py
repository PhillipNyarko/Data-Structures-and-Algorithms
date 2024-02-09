class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User Created!")

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []  # define a list to store all the users in the database

    def insert(self, user):
        i = 0
        while i < len(self.users):
            #  Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


bob = User("bobIsCool", "Bob Hunt", "HuntBob@gmail.com")
tim = User("timRunsTheWorld", "Timothy Chalamet", "ChalametTimothy@yahoo.com")
mary = User("maryLovesFlowers", "Mary Schafer", "SchaferMary@gmail.com")
cameron = User("camIsGrand", "Cameron Boyle", "BoyleCameron@hotmail.com")
elda = User("eldaNotEldin", "Elda Minuet", "MinuetaElda@outlook.com")
princess = User("princessesAndPeaches", "Princess Imbatu", "ImbatuPrincess@gmail.com")
olaf = User("olafIsUnderTheWeather", "Olaf Snow", "SnowOlaf@aol.com")

database = UserDatabase()

class TreeNode:
    def __init__(self, key) :
        self.key = key  # every node gets a key as an identifier...
        self.left = None  # and a left
        self.right = None # and right node


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:  # if the passed in data is a tuple and the tuple is a length of 3...
        node = TreeNode(data[1])  # set the root node to equal the second value in the passed in tuple(should be root)
        node.left = parse_tuple(data[0])  # set the root node's left value to the first item in the passed in tuple
        node.right = parse_tuple(data[2])  # set the root node's right value to the last item in the passed in tuple

    elif data is None: # base case reached when there are no more nodes to look through
        node = None
    else:
        #  if we havent reached the base case, set the node to equal a new node with the subset of data passed in.
        node = TreeNode(data)


tree = parse_tuple(((1, 3, None), 2, ((None,3, 4), 5, (6, 7, 8))))

print(tree)  # should be 2
print(tree.left.key, tree.right.key)  # should be 3, 5
print(tree.left.left.key, tree.left.right.key, tree.right.left.key, tree.right.right.key)  # should be 1, None, 3, 7
print(tree.right.left.right.key, tree.right.right.left.key, tree.right.right.right.key)  # should be 4, 6, 8

