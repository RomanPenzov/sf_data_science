import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число - это тестовый/учебный вариант для понимания и сравнения

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def binary_search_predict(number: int=1) -> int:
    """Угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    low = 1
    high = 100
    
    while True:
        count += 1
        predict_number = (low + high) // 2
        if predict_number == number:
            break
        elif predict_number < number:
            low = predict_number + 1
        else:
            high = predict_number - 1
            
    return count


def score_game(binary_search_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        binary_search_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(binary_search_predict)