import numpy as np


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    """ Делим число наполовину а потом уменьшаеи или увеличиваем наполовину. Если число которое нужно разделить равно
        трем мы это число не делим, вместо этого мы ищем заданное число c шагом 1 """
    predict = 50  # Изначально берем половину от интервала в котором задано число
    step = 25  # Начальный шаг с которым мы будем двигаться по интервалу
    count = 0

    while number != predict:
        count += 1
        if step > 4:  # если число меньше 4 нет смысла его делить
            if predict > number:  # если предположение больше мы шагаем назад
                predict -= step
                step //= 2  # Делим шаг на 2
            else:
                predict += step  # если педположение меньше мы шагаем вперед
                step //= 2
        else:
            if predict > number:  # Здесь до числа остается меньше 4-х чисел
                predict -= 1  # Мы проходим до этого числа с шагом 1
            else:
                predict += 1
    return count


score_game(game_core_v3)
