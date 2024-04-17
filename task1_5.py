
# 1) Попросите пользователя ввести строку и выведите ее в обратном порядке, не используя метод reverse() и sorted().
s= input('введите строку: ')
print(s[-1::-1])

#2) Замените в пользовательской строке все появления буквы h на букву H, кроме первого и последнего вхождения.
def replaceh(str):

    start = str.find('H')
    end = str.rfind('H')
    res=''
    if start!=-1 and end!=-1:
        res = str[:start+1] + str[start+1:end].replace('H','h') + str[end:]
    return res

s="sdfsfHdsfHHHdfdsHdfH H"
print(replaceh(s))

#3) Выведите количество слов в строке
str='ddsd ds sd  '
print('Количество слов в строке: ', len(str.split()))

#4) Выведите количество слов в строке, не используя метод split()
str=str.strip()
print('Количество слов в строке:',str.count(' ')+1)

# 5) У Вас есть строка, состоящая из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
s = 'asdaas cxxxzc'
arr=s.split()
s=s.replace(arr[0],arr[1])
print(s[:s.find(arr[1])+1]+s[s.find(arr[1])+1:].replace(arr[1],arr[0]))





