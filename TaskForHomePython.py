#1.Напишите программу, которая принимает на вход цифру,
#обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

print('Задача №1')
number = int(input('Введите число недели от 1 до 7: '))
if number < 1 or number > 7:
    print('Вы ввели не верное число: ')
elif number > 5:
    print(f'{number} -> Этот день выходной!')
else:
    print(f' {number} -> Это рабочий день!')
print()

#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#для всех значений предикат.

print('Задача №2')
predicate = [True, False]
for x in predicate:
    for y in predicate:
        for z in predicate:
            res = not (x or y or z) == (not x) and (not y) and (not z)
            print('X=', x, 'Y=', 'Z=', z, ':' '¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z' '=', res)
print()

#3. Напишите программу,
#которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
print('Задача №3')
x = float(input('Введите координату Х: '))
y = float(input('Введите координату Y: '))
if x > 0 and y > 0:
    print('1 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
print()

#4. Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).
print('Задача №4')
coordinate_num = int(input('Введите номер четверти: '))
if coordinate_num == 1:
    print('x > 0 and y > 0')
elif coordinate_num == 4:
    print('x > 0 and y < 0')
elif coordinate_num == 2:
    print('x < 0 and y > 0')
elif coordinate_num == 3:
    print('x < 0 and y < 0')
elif coordinate_num < 1 or coordinate_num > 4:
    print('Введено неверное число')
print()

#5. Напишите программу,
#которая принимает на вход координаты двух точек
#и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
print('Задача №5')
from math import sqrt
X1 = float(input('Ведите координату Х первого числа: '))
Y1 = float(input('Ведите координату Y первого числа: '))
X2 = float(input('Ведите координату Х второго числа: '))
Y2 = float(input('Ведите координату Y второго числа: '))
distance = round(sqrt((X2-X1)**2 + (Y2-Y1)**2), 2)
print(f'Расстояние между двумя точками: {distance}')
print()
