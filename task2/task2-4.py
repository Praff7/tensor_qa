string1 = (input('укажите путь к файлу:'))
s = string1.split('\\')
m = len(s)
file = s[m - 1]
s2 = file.split('.')
print('Имя файла:', s2[0], 'Диск:', s[0], 'Корневая папка:', s[1])
