from account_handler import account_handler
from pass_generator import pass_generator
from view import view

if __name__ == '__main__':
    p = pass_generator()
    pwd = p.generate_password(10)
    pwd1 = p.generate_password(10)
    a = account_handler()
    a.load_account()
    v = view()
 #   v.console_view()
    a.get_password_from_name(None)

    # a.add_account("linkedin", pwd1)

    # # a.remove_account("fb")
    # print(a.get_accounts())
    # print(len(a.get_accounts()))
