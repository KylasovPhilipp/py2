                               # task 1

import sys

hours, salary_our, bonus = map(float, sys.argv[1:])
print('salary - {}'.format(hours * salary_our + bonus))

                               # task 2

list_1 = [3, 9, 15, 23, 42, 12, 7, 3]
list_2 = [number for i, number in enumerate(list_1) if list_1[i] > list_1[i-1] and i != 0]
print(list_2)

                               # task 3

print([a for a in range(20, 241) if a % 20 == 0 or a % 21 == 0])

                               # task 4

list_1 = [1, 2, 3, 3, 4, 5, 5, 7, 9, 9]
list_2 = [a for a in list_1 if list_1.count(a) == 1]

                               # task 5

from  functools import reduce
def my_list1(num1, num2):
    return num1 * num2
my_list2 = [a for a in range(100,1001) if a % 2 == 0]
reduce(my_list1, my_list2)

                               # task 6

from itertools import count, cycle
for i in count(int(input('Введите число'))):
    print(i)
