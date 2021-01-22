#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
def game_core_v9(number):
    count = 1 #счетчик попыток
    left =0 #левая граница диапазона неизвестного числа
    right = 101 #правая граница диапазона неизвестного числа
    predict = np.random.randint(left, right) #попытка угадать неизвестное число
    number = np.random.randint(left, right) #неизвестное число
    while number != predict:
        count += 1
        number = (left+right)//2
        if number > predict:
            right = number - 1
        else:
            left = number + 1
    return(count) # выход из цикла, если угадали
def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size = (1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)
score_game(game_core_v9)


# In[ ]:




