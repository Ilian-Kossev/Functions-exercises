def perfect_number(num):
    list_of_dividors = []
    for number in range(1, int(num/2) + 1):
        if num % number == 0:
            list_of_dividors.append(number)
    if sum(list_of_dividors) == num:
        message = 'We have a perfect number!'
    else:
        message = "It's not so perfect."

    return message


input_number = int(input())
print(perfect_number(input_number))


