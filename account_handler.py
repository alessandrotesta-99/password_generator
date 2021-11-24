from file_handler import file_handler


class account_handler:

    def __init__(self):
        self.file_handler = file_handler()
        self.accounts = list()

    def get_accounts(self):
        return self.accounts

    def add_account(self, name, password):
        if not self.get_all_account_names(self.get_accounts()).__contains__(name):
            self.accounts.append(name + " --> " + password + " ;")
            self.save_account()
        else:
            raise Exception("this name account is already exists.")

    def remove_account(self, name):
        if self.get_all_account_names(self.get_accounts()).__contains__(name):
            self.get_accounts().remove(self.get_account_from(name))
            self.reload_account()
        else:
            raise Exception("This account isn't exists.")

    def reload_account(self):
        self.file_handler.open_file("account.txt", "w")
        for acc in self.get_accounts():
            self.file_handler.write_file(str(acc))
        self.file_handler.close_file()

    def get_all_account_names(self, a_list):
        all_accounts_name = list()
        for acc in a_list:
            i = 0
            for char in acc:
                i += 1
                if char == " ":
                    name_account = acc[0:i - 1]
                    all_accounts_name.append(name_account)
                    break
        return all_accounts_name

    def get_account_from(self, name):
        for acc in self.get_accounts():
            i = 0
            for _ in acc:
                i += 1
                sub = acc[0:i - 1]
                if sub == name:
                    return acc

    def get_name_from(self, account):
        for name in self.get_all_account_names(self.get_accounts()):
            if self.get_account_from(name) == account:
                return name

    def edit_account(self, name):
        # todo
        pass

    def save_account(self):
        account_names_in_list = self.get_all_account_names(self.get_accounts())
        account_names_in_file = self.all_account_names_on_file()
        self.file_handler.create_file("account.txt")
        for acc in self.get_accounts():
            for name in account_names_in_list:
                if not account_names_in_file.__contains__(name):
                    self.file_handler.write_file(str(acc) + (str("\n")))
                else:
                    account_names_in_list.remove(name)
                    break
        self.file_handler.close_file()

    def all_account_names_on_file(self):
        file = self.file_handler.open_file("account.txt", "r")
        return self.get_all_account_names(file.readlines())

    def load_account(self):
        file = self.file_handler.open_file("account.txt", "r")
        for acc in file.readlines():
            if not self.get_accounts().__contains__(acc):
                self.get_accounts().append(acc)

    def get_password_from_name(self, name):
        if not self.get_all_account_names(self.get_accounts()).__contains__(name):
            raise Exception("this name doesn't exists.")
        for acc in self.get_accounts():
            if acc == self.get_account_from(name):
                indexStartPoint, indexEndPoint, flagStop = 0, 0, 0
                flagStartPoint = False
                for c in acc:
                    if not flagStartPoint:
                        indexStartPoint += 1
                        indexEndPoint = indexStartPoint
                    if c == "'":
                        flagStop += 1
                        flagStartPoint = True
                    if flagStop == 2:
                        break
                    if flagStartPoint:
                        indexEndPoint += 1
                return acc[indexStartPoint:indexEndPoint - 1]
            else:
                break
