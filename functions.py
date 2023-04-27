

def my_simple_func():
    '''Эта функция ничего не делает'''


my_simple_func()


def print_upper_case(input_string: str):
    print(input_string.upper())

print_upper_case('hello, world!')

print_upper_case(input_string='сторока, которую мы передали в именованный аргумент')


users = [
    {'name': 'Oleg', 'age': 32},
    {'name': 'Sergey', 'age': 24},
    {'name': 'Stanislav', 'age': 15},
    {'name': 'Olga', 'age': 45},
    {'name': 'Maria', 'age': 18}
]