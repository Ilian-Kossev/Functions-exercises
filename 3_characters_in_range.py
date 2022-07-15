def character_in_range(chr_1, chr_2):
    chr_to_num_1 = ord(chr_1)
    chr_to_num_2 = ord(chr_2)
    list_of_strings = []
    string_of_chars = " "
    for number in range(chr_to_num_1 + 1, chr_to_num_2):
        number_to_chr = chr(number)
        list_of_strings.append(number_to_chr)
        string_of_chars = ' '.join(list_of_strings)

    return string_of_chars


char_1 = input()
char_2 = input()
print(character_in_range(char_1, char_2))



