password = input()
symbol_list = [a for a in " ".join(password)]


def password_validator(word):
    if not len(word) in range(6, 11):
        print("Password must be ...")

    if not password.isalnum():
        print("Password must consist of only ...")

    digit_counter = [x for x in symbol_list if x.isdigit()]
    if len(digit_counter) < 2:
        print("Password must have at least ...")

    if len(word) in range(6, 11) and password.isalnum() and len(digit_counter) >= 2:
        print("Password is valid")


password_validator(password)

