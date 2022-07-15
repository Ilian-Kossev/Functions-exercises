def loading_bar(num):
    loading_list = 10*['.']
    for _ in range(0, num, 10):
        loading_list.remove('.')
        loading_list.append('%')
    loading_list.reverse()
    percent_complete = input_number
    result = ''.join(loading_list)
    if not percent_complete == 100:
        final_message = f'{percent_complete}% [{result}]\nStill loading...'
    else:
        final_message = f'100% Complete!\n[{result}]'

    return final_message


input_number = int(input())
print(loading_bar(input_number))