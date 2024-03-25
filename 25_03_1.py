import random
def task1():

    n =  [4, 5, 7, 8, 56]
    b = int(input())
    if b in n:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')

#task1()
def task2():
    n = [4, 5, 7, 8, 56]
    b = 0
    for c in n:
        if n.count(c) > 1:
            b = c
            break
    if b != 0:
        print(b)
    else:
        print('нет')
#task2
def task3():
    n = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    b = int(input())
    #n.reverse()
    #print(n)
    #d = n[-b:]
    #v = n[:-b]
    print(f'Ваши выходные дни: {n[-b:]}' )
    print(f'Ваши рабочие дни: {n[:-b]}')
#task3
def task4():
    l1 = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров']
    l2 = ['Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Голубев','Виноградов', 'Богданов', 'Воробьёв']
    s = tuple(random.sample(l1, 5) + random.sample(l1, 5))
    ss = tuple(sorted(s))
    if 'Иванов' in ss:
        #c = ss.count('Иванов')
        print(f'Иванов есть {ss.count('Иванов')} раз(-a)')
    else:
        print('Иванова нет')

    print(l1, l2, s, len(s), ss, sep='\n')
task4()