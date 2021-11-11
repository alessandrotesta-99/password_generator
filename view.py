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
                              "\n6 - copy password from account"
                              "\n0 - exit"
                              "\nselect: "
                              " "))

    def choose(self, x):
        match x:
            case "1":
                # add account
                name = input("insert account name: ")
                password = input("insert password or press g to generate automatic: ")
                if password == "g":
                    len = int(input("password length: "))
                    password = self.p.generate_password(len)
                    self.a.add_account(name, password)
            case "2":
                # remove account
                nome = input("insert account name: ")
                self.a.remove_account(nome)
            case "3":
                # edit account
                pass
            case "4":
                # generate password
                len = input("password length: ")
                self.password_g = self.p.generate_password(len)
                print("password is: " + self.password_g)
            case "5":
                # get accounts
                print(self.a.get_accounts())
            case "6":
                # get password da nome account
                name = input("insert account name: ")
                print(self.a.get_password_from_name(name))
            case "0":
                # exit
                quit()
