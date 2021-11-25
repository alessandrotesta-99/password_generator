from account_handler import account_handler
from pass_generator import pass_generator


def hello_print():
    print("*******************************************"
          "\n*                                         *"
          "\n*                 WELCOME!                *"
          "\n*                                         *"
          "\n*******************************************")


class view:

    def __init__(self):
        self.a = account_handler()
        self.a.load_account()
        self.p = pass_generator()
        self.password_g = 0

    def console_view(self):
        hello_print()
        while True:
            self.choose(input("\n1 - add account"
                              "\n2 - remove account"
                              "\n3 - edit account"
                              "\n4 - generate password"
                              "\n5 - view all accounts"
                              "\n6 - get password from account"
                              "\n0 - exit"
                              "\nselect: "
                              " "))

    def choose(self, x):
        match x:
            case "1":
                # add account
                name = input("insert account name: ")
                pwd_decoded = input("insert password or press g to generate automatic: ")
                self.__check_name(name)
                self.__check_pwd(pwd_decoded)
                if pwd_decoded == "g":
                    pwd_encoded = self.__password_g()
                else:
                    pwd_encoded = self.p.encode_password(bytes(pwd_decoded, 'utf-8'))
                self.a.add_account(name, pwd_encoded)
                print("Account added!")
            case "2":
                # remove account
                name = input("insert account name: ")
                self.__check_name(name)
                self.a.remove_account(name)
                print("Account removed!")
            case "3":
                # edit account
                name = input("insert account name: ")
                self.__check_name(name)
                self.a.edit_account(name)
                print("Account edited!")
            case "4":
                # generate password
                pwd_generated = self.__decode_g()
                print("password generated! \nThe password is: " + self.p.decode_password(pwd_generated))
            case "5":
                # get accounts
                print(self.a.get_accounts())
            case "6":
                # get password da nome account
                name = input("insert account name: ")
                self.__check_name(name)
                print("The password is (between b' '): " + self.p.decode_password(self.a.get_password_from_name(name)))
            case "0":
                # exit
                quit()

    def __decode_g(self):
        pwd_decoded = str()
        pwd_encoded = self.__password_g()
        flag = False
        start_index = 0
        for c in pwd_encoded:
            if c == "'":
                start_index += 1
                flag = True
            if start_index == 1 and flag:
                pwd_decoded += c
            if start_index == 2:
                break
        return pwd_decoded

    def __check_name(self, name):
        if name == "":
            raise Exception("ERROR- name is not valid.")

    def __check_pwd(self, pwd):
        if pwd == "":
            raise Exception("ERROR- password is not valid.")

    def __password_g(self):
        lun = input("insert password length: ")
        length = int(lun)
        if length <= 0 or None:
            raise Exception("ERROR-This length isn't valid.")
        self.password_g = self.p.generate_password(length)
        return self.password_g
