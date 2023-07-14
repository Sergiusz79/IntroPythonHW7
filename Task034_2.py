# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке.

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам

# Версия улучшеная

def count_a(poem, alphabet):
    counts = []
    for i in range(len(poem)):
        counts.append(len(list(filter(lambda x: x in alphabet, poem[i])))) # добавляем в конец списка к-во согласных букв во фразе
    return counts

def true_false(counts):
    counts = set(counts) 
    if len(counts) == 1:
        print('Парам пам-пам :)')
    else:
        print('Пам парам :(')

def task()  :
    alphabet = 'аеёиоуыэюя'
    poem = str(input('Введите стихотворение:>\n')).split()
    counts = count_a(poem, alphabet)
    true_false(counts)

task()