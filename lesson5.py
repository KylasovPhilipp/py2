               # task1

with open('file.txt', 'w') as f:
    line = input('Введите данные: ')
    f.write(line + '\n')

              # task2

with open('file2.txt', 'w') as f:
    lines = f.readlines()
    print('Количество строк: ', len(line))
    for num_line, line in enumerate(lines, start=1):
        print('{} строка содержит - {} слов'.format(num_line,len(line.split())))



              # task3

with open('file3.txt') as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' : ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('средняя зп:', sum(salaries) / len(salaries))

               # task4

with open('file4E.txt', encoding='utf-8') as f:
    lines = f.readlines()
with open('file4R.txt', 'w', encoding='utf-8') as f:
    if '1' in line:
        line = line.replace('One', 'Один')
    elif '2' in line:
        line = line.replace('Two', 'Два')
    elif '3' in line:
        line = line.replace('Three', 'Три')
    elif '4' in line:
        line = line.replace('Four', 'Четыре')
    f.write(line)

               # task5

with open('file5.txt', 'w') as f:
    numbers = input('Введите числа: ')
    f.write('Введенные числа: ' + numbers + '\n')
    numbers = map(int, numbers.split())
    sum_numbers =sum(numbers)
    f.write('Сумма чисел: ' + str(sum_numbers))
    print('Сумма введенных чисел: ', sum_numbers)
print('Выполнено')

                # task 6

