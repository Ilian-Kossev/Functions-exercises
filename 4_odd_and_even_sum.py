def odd_and_even_sum(num):
    sum_even = 0
    sum_odd = 0
    for digit in input_number:
        value = int(digit)
        if value % 2 == 0:
            sum_even += value
        else:
            sum_odd += value
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


input_number = input()
print(odd_and_even_sum(input_number))


