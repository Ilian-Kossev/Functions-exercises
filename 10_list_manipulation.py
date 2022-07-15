initial_list = input().split()
integer_list = [int(el) for el in initial_list]
command = input()
while not command == 'end':
    action = command.split()
    if action[0] == 'exchange':
        parameter = int(action[1])
        if parameter > len(integer_list) - 1 or parameter < 0:
            print('Invalid index')
        else:
            sub_list1 = integer_list[parameter + 1: len(integer_list)]
            sub_list2 = integer_list[:parameter + 1]
            integer_list = sub_list1 + sub_list2
            sub_list1.clear()
            sub_list2.clear()
    elif action[0] == 'max':
        if action[1] == 'even':
            even_list = [el for el in integer_list if el % 2 == 0]
            if len(even_list) > 0:
                max_value = max(even_list)
                counter = -1
                index = 0
                for el in integer_list:
                    counter += 1
                    if el == max_value:
                        index = counter
                print(index)
            else:
                print('No matches')
        elif action[1] == 'odd':
            odd_list = [el for el in integer_list if el % 2 == 1]
            if len(odd_list) > 0:
                max_value = max(odd_list)
                counter = -1
                index = 0
                for el in integer_list:
                    counter += 1
                    if el == max_value:
                        index = counter
                print(index)
            else:
                print('No matches')
    elif action[0] == 'min':
        if action[1] == 'even':
            even_list = [el for el in integer_list if el % 2 == 0]
            if len(even_list) > 0:
                min_value = min(even_list)
                counter = -1
                index = 0
                for el in integer_list:
                    counter += 1
                    if el == min_value:
                        index = counter
                print(index)
            else:
                print('No matches')
        elif action[1] == 'odd':
            odd_list = [el for el in integer_list if el % 2 == 1]
            if len(odd_list) > 0:
                min_value = min(odd_list)
                counter = -1
                index = 0
                for el in integer_list:
                    counter += 1
                    if el == min_value:
                        index = counter
                print(index)
            else:
                print('No matches')
    elif action[0] == 'first':
        limit = int(action[1])
        if limit > len(integer_list):
            print('Invalid count')
            command = input()
            continue
        if action[2] == 'even':
            even_list_first = [el for el in integer_list if el % 2 == 0]
            even_list_first = even_list_first[: limit]
            print(even_list_first)
        elif action[2] == 'odd':
            odd_list_first = [el for el in integer_list if el % 2 == 1]
            odd_list_first = odd_list_first[: limit]
            print(odd_list_first)
    elif action[0] == 'last':
        integer_list.reverse()
        limit = int(action[1])
        if limit > len(integer_list):
            print('Invalid count')
            command = input()
            continue
        if action[2] == 'even':
            even_list_last = [el for el in integer_list if el % 2 == 0]
            even_list_last = even_list_last[:limit]
            print(even_list_last)
        elif action[2] == 'odd':
            odd_list_last = [el for el in integer_list if el % 2 == 1]
            odd_list_last = odd_list_last[:limit]
            print(odd_list_last)
        integer_list.reverse()

    command = input()
print(integer_list)
#judge - 70/100

