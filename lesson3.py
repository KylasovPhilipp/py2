                    # task 1
numbers = []
for i in range(2):
    numbers = int(input('Введите число: '))
print(numbers1 / numbers2)

                    # task 2

def characteristic_person(**kwargs):
    for a, b, c, d, e, f in kwargs.items():
        print(a, b, c, d, e, f)
print(characteristic_person(
    name = input('Имя'),
    surname = input('Фамилия'),
    bith = input('годрождения'),
    city = input('город'),
    email = input('почта'),
    number_phone = input('телефон'),))

                    # task 3

def my_func(num_1, num_2, num_3):
    try:
        my_list = [num_1, num_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
print(my_func(1,2,3))

                    # task 4

def my_func(x,y):
    try:
        result = x ** y
        return result
print(my_func(7, 5))

# второй вариант

def my_func(x,y):
    try:
        x, y = float(x), int(y)
        result = x
        for i in range(abs(y) - 1):
            result = *x
        return 1 / result

                # task 5

def summary():
    exist = False
    result = 0
    while exist == False:
        numbers = input('Введите числа или введите z и завершите: ').split()
        result.line = 0
        for number in numbers:
            if 'z' in number:
                exist = True
                break
            result_line += int(number)
        result += result.line
    print(result)

                 # task 6

def int_func(text):
    return text.title()
print(int_func('text'))
result_int_func = int_func('text in task')
print(result_int_func)
