class User():
    def __init__(self, name, username, password, is_admin):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__is_admin = is_admin

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username


    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password
    

    @property
    def is_admin(self):
        return self.__is_admin
    @is_admin.setter
    def is_admin(self, is_admin):
        self.__is_admin = is_admin