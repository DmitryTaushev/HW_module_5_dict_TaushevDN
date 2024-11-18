from utils import true_false,answer_for_user,dictionary

words = {}
answer = {}
user_level = input("Введите уровень сложности:\nEasy\nMedium\nHard: ")
if user_level not in dictionary():
    print('По умолчанию выбран уровень easy')
    words = dictionary()['easy']
else:
    words = dictionary()[user_level.strip().lower()]

true_false(answer_for_user(words))
