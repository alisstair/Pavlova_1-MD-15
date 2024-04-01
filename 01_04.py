def prv():
    l = {'Россия': 'Москва', 'Казахстан': 'Астана', 'Норвегия': 'Осло', 'Германия': 'Берлин'}
    for c in l:
        print(f'{c} - {l[c]}')

    a = input()
    if a in l:
        print(f'Столица {a}: {l[a]}.')
    else:
        print('Введите другую страну.')

    s = sorted(l)
    for c in s:
        print(f'{c} - {l[c]}')
#prv()

def dva():
    b = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
         'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
         'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
         'Й': 4, 'Ы': 4,
         'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
         'Ш': 8, 'Э': 8,'Ю': 8,
         'Ф': 10, 'Щ': 10,'Ъ': 10}
    word = input('Введите слово (НА КИРИЛЛИЦЕ):').upper()
    total = 0
    for letter in word:
        if letter in word:
            m = b[letter]
        else:
            m = 0
        total += m
    print(f'Стоимость слова {word}: {total} очко(-в)')
#dva()

def tri():
    students = {'Иванов': ['англ', "франц", "нем"],
                'Смирнов': ["франц", "нем", "кит", "исп"],
                "Петров": ["рус", "яп", "англ", "кит"]}
    all_l = []
    for s in students:
        lgs = students[s]
        for l in lgs:
            if l not in all_l:
                all_l.append(l)
    all_l.sort()
    print(all_l)

    kit = []
    for s in students:
        lgs = students[s]
        if 'кит' in lgs:
            kit.append(s)
    print(f'Китайцы: {kit}')
tri()
