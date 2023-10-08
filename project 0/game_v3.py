"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число через проверку больше или меньше предполагаемое число и исходя из этого сужать диапазон
       предполагаемых чисел

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    start_range = 1 #нижняя граница для диапазона случайных чисел
    end_range = 101 #верхняя граница для диапазона случайных чисел
    while True:
        count += 1
        predict_number = np.random.randint(start_range, end_range) # предполагаемое число
        # Если предполагаемое число оказалось больше, чем загаданное число, то в следующем цикле сужаем диапазон предполагаемых
        # чисел, устанавливая текущее предполагаемое число в качестве верхней границы диапазона
        if predict_number > number: 
            end_range = predict_number
        # Если предполагаемое число оказалось меньше, чем загаданное число, то в следующем цикле сужаем диапазон предполагаемых
        # чисел, устанавливая текущее предполагаемое число в качестве нижней границы диапазона
        elif predict_number < number:
            start_range = predict_number            
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN

if __name__ == '__main__':
    score_game(random_predict)
