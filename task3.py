a = input("Введите год: ")

if (int(a) % 4 == 0 and not int(a) % 100 == 0) or (int(a) % 400 == 0):
    print("Год " + a + " - високосный")
else:
    print("Это год не високосный.")