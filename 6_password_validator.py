def password_validator(password):
    counter_symbols = 0
    counter_digits = 0
    not_only_letters_and_digits = False
    not_correct_number_of_characters = False
    not_at_least_two_digits = False
    result_1 = ""
    result_2 = ""
    result_3 = ""
    result_4 = ""
    for element in password:
        counter_symbols += 1
        value_element = ord(element)
        if 65 <= value_element <= 90 or 97 <= value_element <= 122 or 48 <= value_element <= 57:
            pass
        else:
            not_only_letters_and_digits = True
        if 48 <= value_element <= 57:
            counter_digits += 1
    if not 6 <= counter_symbols <= 10:
        not_correct_number_of_characters = True
    if counter_digits < 2:
        not_at_least_two_digits = True
    if not_only_letters_and_digits:
        result_1 = "Password must consist only of letters and digits"
    if not_correct_number_of_characters:
        result_2 = "Password must be between 6 and 10 characters"
    if not_at_least_two_digits:
        result_3 = "Password must have at least 2 digits"
    if not not_only_letters_and_digits and not not_correct_number_of_characters and not not_at_least_two_digits:
        result_4 = "Password is valid"
    return result_1, result_2, result_3, result_4


input_password = input()
result_1, result_2, result_3, result_4 = password_validator(input_password)
print(password_validator(input_password))
