from account_handler import account_handler
from pass_generator import pass_generator

if __name__ == '__main__':
    p = pass_generator()
    pwd = p.generate_password(10)
    pwd1 = p.generate_password(10)
    a = account_handler()
    # a.load_account()
    a.add_account("fb", pwd)
    a.add_account("instagram", pwd1)
    print(a.get_accounts())
    # # a.remove_account("fb")
    # print(a.get_accounts())
    # print(len(a.get_accounts()))

