def true_false(answer):
    levels = {
        0: "Нулевой",
        1: "Так себе",
        2: "Можно лучше",
        3: "Норм",
        4: "Хорошо",
        5: "Отлично"
    }
    count_true = 0
    true_list = []
    false_list = []
    for keys in answer:
        if answer[keys] == 'True':
            count_true += 1
            true_list.append(keys)
        else:
            false_list.append(keys)
    if len(true_list) > 0:
        print('Правильно отвечены слова:')
        for i in true_list:
            print(i)
    if len(false_list) > 0:
        print('Неправильно отвечены слова:')
        for i in false_list:
            print(i)
    print(f'Ваш уровень - {levels[count_true]}')

def answer_for_user(words):
    answer = {}
    count = 0
    for i in range(len(words)):
        user_answer = input(
            f"{list(words.keys())[count]}, {len(words[list(words.keys())[count]])} букв, начинается на {words[list(words.keys())[count]][0]}...").strip().lower()
        if user_answer == words[list(words.keys())[count]]:
            print(f'Верно {list(words.keys())[count]} - это {words[list(words.keys())[count]]}')
            answer[list(words.keys())[count]] = 'True'
        else:
            print(f'Неверно. {list(words.keys())[count]} — это {words[list(words.keys())[count]]}.')
            answer[list(words.keys())[count]] = 'False'
        count += 1

    return answer

def dictionary():
    words_easy = {
        "family": "семья",
        "hand": "рука",
        "people": "люди",
        "evening": "вечер",
        "minute": "минута",
    }
    words_medium = {
        "believe": "верить",
        "feel": "чувствовать",
        "make": "делать",
        "open": "открывать",
        "think": "думать",
    }
    words_hard = {
        "rural": "деревенский",
        "fortune": "удача",
        "exercise": "упражнение",
        "suggest": "предлагать",
        "except": "кроме",
    }
    words_dicts = {
        'easy': words_easy,
        'medium': words_medium,
        'hard': words_hard}

    return words_dicts

