#1. Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('Задача №1')
array = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(array)):
    if (i % 2 != 0):
        sum += array[i]
print(f'- {[2, 3, 5, 9, 3]} -> сумма элементов стоящих на нечетных позициях = {sum}')
           #0 #1 #2 #3 #4
print()
#2. Написать программу,
#которая генерирует двумерный массив на A x B элементов
#( A и B вводим с клавиатуры)
#И считаем средне-арифметическое каждой строки
#(не пользуемся встроенными методами подсчета суммы)
print('Задача №2')
from random import randint
a = int(input('A = '))
b = int(input('B = '))
ab_list = []
for index in range(a):
    ab_list.append([])
    for value in range(b):
        ab_list[index].append(randint(1, 10))

print('Среднее-арифметическое каждой строки: ')
for i in range(a):
    b_sum = 0
    for j in range(b):
        b_sum += ab_list[i][j]
    print(f'{i+1} Строка {ab_list[i]} - {round(b_sum / b, 2)}')
print()
#3.Сгенерируйте список на 30 элементов.
#Отсортируйте список по возрастанию, методом сортировки выбором.
print('Задача №3')
from random import randint
def rand_list(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr
test_list = [randint(1, 99) for i in range(30)]
print(f'Random list: {test_list}')
print(f'Ordered list: {rand_list(test_list)}')
