a = input ("Введите цвет (с заглавной буквы): ")
b = input ("Введите 2 цвет (с заглавной буквы): ")

if a == "Красный":
    if b == "Синий":
        print("Фиолетовый")
    else:
        print("Оранжевый")

elif a == "Синий":
    if b == "Красный":
        print("Фиолетовый")
    else:
        print("Зеленый")

elif a == "Жёлтый":
    if b == "Красный":
        print("Оранжевый")
    else:
        print("Зелёный")

else:
    print("Неправильный цвет.")