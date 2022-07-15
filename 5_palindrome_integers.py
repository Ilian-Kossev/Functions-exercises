def palindrome_meter(number_list):
    input_list = number_list.split(', ')
    palindrome_found_list = []
    palindrome_found = bool
    for i in range(len(input_list)):
        input_number = input_list[i]
        list_of_input_number = []
        list_of_input_number_backward = []
        palindrome_found = False
        for symbol in input_number:
            value_symbol = int(symbol)
            list_of_input_number.append(value_symbol)
        for index in range(len(list_of_input_number) - 1, - 1, -1):
            digit = list_of_input_number[index]
            list_of_input_number_backward.append(digit)
        if list_of_input_number == list_of_input_number_backward:
            palindrome_found = True

        palindrome_found_list.append(palindrome_found)
    return palindrome_found


input_data = input()
print(palindrome_meter(input_data))
