string1 = str(input('Введите строку 1:'))
string2 = str(input('Введите строку 2:'))
changed_str1 = string2[:2] + string1[2:]  # преобразование строки 1
changed_str2 = string1[:2] + string2[2:]  # преобразование строки 2
print(changed_str1 + ' ' + changed_str2)
