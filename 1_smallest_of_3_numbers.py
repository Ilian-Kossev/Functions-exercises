def smallest(int_1, int_2, int_3):
    if int_1 < int_2 and int_1 < int_3:
        return int_1
    elif int_2 < int_1 and int_2 < int_3:
        return  int_2
    elif int_3 < int_1 and int_3 < int_2:
        return  int_3


integer_1 = int(input())
integer_2 = int(input())
integer_3 = int(input())

print(smallest(integer_1, integer_2, integer_3))