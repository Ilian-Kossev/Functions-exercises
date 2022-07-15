def factorial_division(num1, num2):
    factorial_value_num1 = 1
    factorial_value_num2 = 1
    for number in range(1, num1 + 1):
        factorial_value_num1 *= number
    for number in range(1, num2 + 1):
        factorial_value_num2 *= number
    result = f'{factorial_value_num1 / factorial_value_num2:.2f}'
    return result


number1 = int(input())
number2 = int(input())
print(factorial_division(number1, number2))
CB8587AA
0893 551 664
1.5 predi gara kostandova kum Velingrad
