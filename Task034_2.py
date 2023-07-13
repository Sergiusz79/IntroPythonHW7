




def count_a(poem, alphabet):
    counts = []
    for i in range(len(poem)):
        counts.append(len(list(filter(lambda x: x in alphabet, poem[i]))))
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