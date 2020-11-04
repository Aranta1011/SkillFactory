#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#Алгоритм из примера с изменённым шагом
def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        '''Исходим из того, что в счётчик идёт число циклов while, а не сравнений'''
        count += 1
        '''Убираем пробелы в сравнении согласно pep-8'''
        if number>predict: 
            '''Относительно приведенного примера увеличиваем шаг спуска с 1 до 2'''
            predict += 2
            '''Если загаданное число становится меньше предскажанного, то, очевидно, загаданное нами число
            всего на 1 меньше предсказанного'''
            '''Убираем пробелы в сравнении согласно pep-8'''
            if number<predict:
                predict -= 1
                return(count)
        elif number<predict: #Убираем пробелы в сравнении согласно pep-8
            predict -= 2
            '''По аналогии со случаем number>predict'''
            '''Убираем пробелы в сравнении согласно pep-8'''
            if number>predict:
                predict += 1
                return(count)
    return(count) # выход из цикла, если угадали


#Алгоритм бинарного поиска
def game_core_v4(number):
    '''Сначала ищется середина интервала, на котором может быть число, а затем двигаем границы интервала'''
    count = 1
    lim_lower = 1
    lim_upper = 101
    '''Данный цикл найдёт заданное на интервале число'''
    '''Убираем пробелы в сравнении согласно pep-8'''
    while ((lim_upper - lim_lower)>1):
        '''Исходим из того, что в счётчик идёт число циклов while, а не сравнений'''
        count += 1
        middle = (lim_lower + lim_upper) / 2
        '''Убираем пробелы в сравнении согласно pep-8'''
        if (middle>=number):
            lim_upper = middle
        else:
            lim_lower = middle
    return(count) # выход из цикла, если угадали
        
        
#Основной код для запуска проекта
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

#Запускаем проект
score_game(game_core_v4)

