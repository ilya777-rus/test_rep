
#11)дан словарь:
date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(f'{date_dict["year"]}-{date_dict["month"]}-{date_dict["day"]}')

#12) На вход от пользователя поступает строка с числами, разделёнными запятой. Вам нужно составить список и кортеж с этими числами.
ss = '  1, 2, 8,4 , 23 '
print(list(map(int,ss.split(','))))
print(tuple(map(int,ss.split(','))))

# 13) Вам
# дано
# множество
# студентов:

students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print('все люди:', students | employees)
print('все люди:', students.union(employees))
print('Всех тех, кто одновременно учится и работает:', students & employees)
print('Всех тех, кто одновременно учится и работает:', students.intersection(employees))
print('Всех тех, кто только работает, но не учится:', employees - students)
print('Всех тех, кто только работает, но не учится:', employees.difference(students))
print('Всех тех, кто либо учится, либо работает, но не одновременно:', students ^ employees)
print('Всех тех, кто либо учится, либо работает, но не одновременно:', students.symmetric_difference(employees))
