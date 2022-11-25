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

#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#для всех значений предикат.

print('Задача №2')
predicate = [True, False]
for x in predicate:
    for y in predicate:
        for z in predicate:
            res = not (x or y or z) == (not x) and (not y) and (not z)
            print('X=', x, 'Y=', 'Z=', z, ':' '¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z' '=', res)
