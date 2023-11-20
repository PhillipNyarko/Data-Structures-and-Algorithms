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


Bob = User("bobIsCool", "Bob Hunt", "HuntBob@gmail.com")
Tim = User("timRunsTheWorld", "Timothy Chalamet", "ChalametTimothy@yahoo.com")
Mary = User("maryLovesFlowers", "Mary Schafer", "SchaferMary@gmail.com")
Cameron = User("camIsGrand", "Cameron Boyle", "BoyleCameron@hotmail.com")
Elda = User("eldaNotEldin", "Elda Minuet", "MinuetaElda@outlook.com")
Princess = User("princessesAndPeaches", "Princess Imbatu", "ImbatuPrincess@gmail.com")
Olaf = User("olafIsUnderTheWeather", "Olaf Snow", "SnowOlaf@aol.com")

Users = [Bob, Tim, Mary, Cameron, Elda, Princess, Olaf]

