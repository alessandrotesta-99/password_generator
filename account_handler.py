from file_handler import file_handler


class account_handler:

    def __init__(self):
        self.file_handler = file_handler()
        self.accounts = list()

    def get_accounts(self):
        return self.accounts

    def add_account(self, name, password):
        if not self.all_accounts_name().__contains__(name):
            self.accounts.append(name + " --> " + password + " ;")
            self.save_account()
        else:
            raise Exception("this name account is already exists.")

    def remove_account(self, name):
        # todo
        self.accounts.remove(name)

    def edit_account(self, name):
        # todo
        pass

    def save_account(self):
        self.file_handler.create_file("account.txt")
        for acc in self.get_accounts():
            self.file_handler.write_file(str(acc))
            for char in acc:
                if char == ";":
                    self.file_handler.write_file(str("\n"))
        if self.get_accounts().__contains__("\n"):
            self.accounts.remove("\n")
        self.file_handler.close_file()

    def load_account(self):
        # todo correggere aggiunta di account. mette ogni volta lo spazio dopo il ;. anche in quelli gia esistenti.
        file = self.file_handler.open_file("account.txt", "r")
        for acc in file.readlines():
            self.get_accounts().append(acc)
        if self.get_accounts().__contains__("\n"):
            self.accounts.remove("\n")
        self.file_handler.close_file()

    def all_accounts_name(self):
        all_accounts_name = list()
        for acc in self.get_accounts():
            i = 0
            for char in acc:
                i += 1
                if char == " ":
                    name_account = acc[0:i - 1]
                    all_accounts_name.append(name_account)
                    break
        return all_accounts_name
