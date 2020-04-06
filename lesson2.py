                                         # task 1
singer = ['Selin', 45, [45], True]
print(singer)
for i in singer:
    print(type(i))


# task 2
animals = list(input('Введите животных: '))
for i in range(1, len(animals), 2):
    animals[i - 1], animals[i] = animals[i], animals[i - 1]
print(animals)


# task 3
# list
seasons_list = ['',
    'winter',
    'winter',
    'spring',
    'spring',
    'spring',
    'summer',
    'summer',
    'summer',
    'autumn',
    'autumn',
    'autumn',
    'winter',]
month = int(input('Введите месяц от 1 до 12: '))
print(seasons_list[month])

#  dict
seasons_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
}
month = int(input('Введите месяц от 1 до 12: '))
print(seasons_dict[month])

# task 4
some = input('Введите несколько слов: ')
words = some.split()
for i, word in enumerate(words):
    print(i, word[:10])

# task 5
my_list = [7, 5, 3, 3, 2]
request = input('Введите число: ')
for index, number in enumerate(my_list):
    if int(request) < int(number):
        continue
    my_list.insert(index, request)
    print(my_list)
    break
else:
    my_list.append(request)
    print(my_list)
