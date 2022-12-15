#Сделать поле чудес .
#Компьютер загадывает слово.
# А мы его угадываем. Делаем с помощью функций. Кто хочет посложней - добавляем очки и барабан.
import random
# база вопросов в виде словарей
questions_main = {
"Язык программирования (русским алфавитом)": "фортран",
"Устройство вывода информации": "принтер",
"Электронная схема, управляющая внешним устройством": "контроллер",
"Разъемы подключения внешних устройств": "интерфейс"
}
questions_final = {
"Тип пометки, используемый для быстрого нахождения пользователей и фотографии": "хэштег",
" Процесс разметки компьютерного диска — разбиения его на логические части сектора, дорожки и их пометка": "форматирование",
"дин из простейших логических элементов, который преобразует значение в другое ему противоположное": "инвертор",
"Наука об общих свойствах процессов управления в живых и неживых системах": "кибернетика"
}
# приветственное слово ведущего
print("Добро пожаловать на игру Поле чудес.\n\
Вам предстоит ответить на вопрос и если повезет выиграть супер приз")
print("Внимание!\n")

# выбираем случайный вопрос
question_main = random.choice(list(questions_main.keys()))

# ответ на выбранный вопрос
answer_main = questions_main[question_main]

# создаем переменную для хранения списка звездочек
star_answer = []
for i in range(len(answer_main)):
    star_answer.append("*")

print("Вопрос:", question_main)
print(*star_answer)

# список возможных очков при вращении барабана
scores = [100, 200, 300, 400, 500, 0, "next", "Б"]

score1 = 0
score2 = 0
gameOver = False
player = 0
break_main = False  # значение изменится на True, если кто-то ошибся, называя слово целиком

while not gameOver:
    # Слова ведущего
    if player % 2 == 0:
        print("\nИграет Игрок-1")
    else:
        print("\nИграет Игрок-2")
    print("Готовы ли вы назвать слово целиком? Введите 'да' или нажмите любую клавишу")
    if input().lower() == "да":
        print("Назовите слово целиком")
        answer = input().lower()
        if answer == answer_main:
            print("Поздравляю, вы ответили правильно!")
            print("Ответ", answer_main)
            break
        else:
            print("К сожалению, вы ошиблись. Вы проиграли")
            if player % 2 == 0:
                print("Победил Игрок-2")
                print("Набранное количество очков", score2)
                break_main = True
            else:
                print("Победил Игрок-1")
                print("Набранное количество очков", score1)
                break_main = True
            break
    else:
        print("Вращайте барабан")
        play_score = random.choice(scores)
        if play_score == "next":
            print("Ход переходит к другому игроку")
            player += 1
            continue
        elif play_score == "Б":
            print("У вас банкрот. Очки сгорают, а ход переходит к другому игроку")
            if player % 2 == 0:
                score1 = 0
                player += 1
                continue
            else:
                score2 = 0
                player += 1
                continue
        else:
            print("Вы заработали", play_score, "очков")
            if player % 2 == 0:
                score1 += play_score
            else:
                score2 += play_score
            print("Назовите букву")
            letter = input()
            nxt_plr = False
            for i in range(len(star_answer)):
                if letter == answer_main[i]:
                    nxt_plr = True

                    star_answer[i] = letter
            if nxt_plr == True:
                print("Вы отгадали. Откройте пожалуйста такие буквы в слове")
                print(*star_answer)
            else:
                player += 1
                print(*star_answer)

win_score = 0
if break_main == False:  # если никто не ошибся, называя слово целиком
    if player % 2 == 0 and break_main == False:
        print("Победил Игрок-1")
        print("Набранное количество очков", score1)
        win_score = score1
    else:
        print("Победил Игрок-2")
        print("Набранное количество очков", score2)
        win_score = score2
# список возможных подарков
gifts = {100: "блокнот", 200: "общая тетрадь", 300: "калькулятор", 500: "Флешка", 1000: "mp3-плеер"}

