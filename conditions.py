
f = False

if True:
    print('истина!')
else:
    print('ложь!')

code = 300

if code == 200:
    print('Хороший ответ!')
elif code == 201:
    print('Тоже неплохой ответ')
else:
    print('Плохой ответ!')


if 200 <= code < 400:
    print('Хороший ответ!')
else:
    print('Плохой ответ!')


try:
    1/0
except ZeroDivisionError:
    print('Нельзя делить на ноль!')

print(bool('abc'))
print(bool(''))
print(bool(123))
print(bool(-123))
print(bool(0))
print(bool([0, '']))
print(bool([]))

user_list = []

if user_list:
    print(user_list)

if len(user_list) !=0:
    print(user_list)

