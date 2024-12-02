mas = [5, 7, 4, 3, 8, 2]
n = 6   # количество элементов в массиве
for run in range(n - 1):  # цикл сравнения проходит по всем элементам массива, кроме последнего
    for i in range(n - 1 - run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)
