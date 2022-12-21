#1)Нужно напистаь программу
#В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
#В самой программе вводим список всех студентов.
#В программе нужно вывести список студентов, отсортированный по имени,
# А так же студентов, у которых низкие оценки
print('Задача №1')
def fill_students():
    stud_number = input('Введите кол-во студентов: ')
    students_lst = []
    for i in range(0, int(stud_number)):
        students_lst.append(Student(input('Введите имя студента: '), input('Введите номер группы: ')))
    return students_lst


def fill_stud_progress(students_lst):
    for student in students_lst:
        student.fill_progress()
    return students_lst


def stud_sort_key(student):
    return student.name[0]


def low_marks(students_lst):
    low_marks_lst = []
    for student in students_lst:
        for subject, mark in student.progress.items():
            if int(mark) <= 3:
                low_marks_lst.append(student)
                break
    return low_marks_lst


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.progress = dict()

    def fill_progress(self):
        subject_lst = ['Химия', 'Математика', 'Физика', 'Информатика', 'Геометрия']
        self.progress = {}
        print(f'Успеваемость студента - {self.name}: ')
        for subject in subject_lst:
            self.progress[subject] = input(f'Введите оценку по предмету {subject}: ')
        return self.progress

    def __str__(self):
        progress_str = ''
        for subject, mark in self.progress.items():
            progress_str += f'{subject} - {mark}\n'
        return f'Студент - {self.name}\nНомер группы - {self.group}\nУспеваемость:\n{progress_str}'


class Journal:
    def __init__(self, students):
        self.students = students

    def sort_students(self, sort_key):
        return self.students.sort(key=sort_key)

    def __str__(self):
        self.sort_students(stud_sort_key)
        print("Список студентов по алфавиту: ")
        out_str = ''
        for student in self.students:
            out_str += f'{str(student)}\n'
        return out_str


NewJournal = Journal(fill_stud_progress(fill_students()))
print()
print(NewJournal)

LowMarksJournal = Journal(low_marks(NewJournal.students))
print('Студенты с низкой успеваемостью:')
print(LowMarksJournal)


#Реализуйте кодирование строки "по Хаффману".
#У вас два пути:
#1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
#Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
#и оптимизации.
#2) тема понятна? постарайтесь сделать свою реализацию.

print('Задача №2 (своя)')
class HuffmanCode:
    def __init__(self, probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if value >= self.probability[j]:
                return j
        return index - 1

    def characteristics_huffman_code(self, code):
        length_of_code = [len(k) for k in code]

        mean_length = sum([a * b for a, b in zip(length_of_code, self.probability)])

        print("Average length of the code: %f" % mean_length)
        # print("Efficiency of the code: %f" % (entropy_of_code / mean_length))

    def compute_code(self):
        # получаем необходимое число кодов
        num = len(self.probability)
        # заполняем массив нужным кол-вом пустых строк
        huffman_code = [''] * num

        # перебираем элементы списка по два
        for i in range(num - 2):
            # ищем сумму вероятностей двух крайних элементов
            val = self.probability[num - i - 1] + self.probability[num - i - 2]
            if huffman_code[num - i - 1] != '' and huffman_code[num - i - 2] != '':
                # к каждому элементу списка последнего элемента клеим '1'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                # к каждому элементу списка предпоследнего элемента клеим '0'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif huffman_code[num - i - 1] != '':
                # предпоследний элемент проставляем как '0'
                huffman_code[num - i - 2] = '0'
                # у последнего элемента, к каждому элементу добавляем '1' слева
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif huffman_code[num - i - 2] != '':
                # последний элемент проставляем как '1'
                huffman_code[num - i - 1] = '1'
                # у предпоследнего(который список), к каждому элементу добавляем '0' слева
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:  # проставляем '1' последнему элементу, '0' предпоследнему
                huffman_code[num - i - 1] = '1'
                huffman_code[num - i - 2] = '0'

            # ищем позицию для вставки в первоначальный список вероятностей
            position = self.position(val, i)
            # отсекаем от изначального списка 2 последних элемента
            probability = self.probability[0:(len(self.probability) - 2)]
            # вставляем полученное значение в нужную позицию
            probability.insert(position, val)
            if isinstance(huffman_code[num - i - 2], list) and isinstance(huffman_code[num - i - 1], list):
                # последний и предпоследний элементы списки, тогда клеим в общий список
                complete_code = huffman_code[num - i - 1] + huffman_code[num - i - 2]
            elif isinstance(huffman_code[num - i - 2], list):
                # предпоследний элемент - список, клеим список + значение последнего элемента
                complete_code = huffman_code[num - i - 2] + [huffman_code[num - i - 1]]
            elif isinstance(huffman_code[num - i - 1], list):
                # последний элемент - список, клеим список + значение предпоследнего элемента
                complete_code = huffman_code[num - i - 1] + [huffman_code[num - i - 2]]
            else:  # формируем итоговый код, как список из значений двух последних элементов списка
                complete_code = [huffman_code[num - i - 2], huffman_code[num - i - 1]]

            # отсекаем крайний элемента из списка строк кодов
            huffman_code = huffman_code[0:(len(huffman_code) - 2)]
            # вставляем получившийся код в нужную позицию
            huffman_code.insert(position, complete_code)

        # клеим строки для первого и второго элементов
        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        # если длина второго элемента 0, то вписываем туда '1'
        if len(huffman_code[1]) == 0:
            huffman_code[1] = '1'

        count = 0
        # финальные коды
        final_code = [''] * num

        # в huffman_code должно остаться 2 элемента
        for i in range(2):
            for j in range(len(huffman_code[i])):
                # последовательно вытаскиваем элементы из первого элемента(список)
                final_code[count] = huffman_code[i][j]
                count += 1

        # сортируем полученный массив по длине строк по возрастанию
        final_code = sorted(final_code, key=len)
        return final_code


# генерирует по строке словарь символов с кол-вом повторений символа в строке
def generate_frequencies(str):
    freq = {}
    for c in str:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq


string = input("Enter the string to compute Huffman Code: ")

# словарь, где ключ это символ, а значение кол-во повторений
freq = generate_frequencies(string)
# сортируем словарь по значениям(частотам) в порядке убывания
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# длина строки
length = len(string)
# подсчет вероятностей для каждого символа - частота появления, деленная на длину строки
probabilities = [float("{:.2f}".format(frequency[1] / length)) for frequency in freq]
# сортируем по убыванию
probabilities = sorted(probabilities, reverse=True)
# создаем объект
huffmanClassObject = HuffmanCode(probabilities)
# создаем метод, который строит список кодов
huffman_code = huffmanClassObject.compute_code()

print(' Char | Huffman code ')
print('----------------------')

for id, char in enumerate(freq):
    if huffman_code[id] == '':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman_code[id]))

huffmanClassObject.characteristics_huffman_code(huffman_code)