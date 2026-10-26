import random

# Читаем n из файла
with open("in3.txt", "r", encoding="utf-8") as f_in:
    n = int(f_in.readline())
size = 2 * n

# Создаем матрицу
matrix = [[random.randint(1, 9) for j in range(size)] for i in range(size)]

# Перестановка блоков
new_matrix = [[0] * size for i in range(size)]
for i in range(size):
    for j in range(size):
        if i < n and j < n:
            new_matrix[i + n][j + n] = matrix[i][j]
        elif i >= n and j >= n:
            new_matrix[i - n][j - n] = matrix[i][j]
        elif i < n and j >= n:
            new_matrix[i + n][j - n] = matrix[i][j]
        elif i >= n and j < n:
            new_matrix[i - n][j + n] = matrix[i][j]

# Записываем в файл
with open("out3.txt", "w", encoding="utf-8") as f_out:
    f_out.write("Исходная матрица:\n")
    for row in matrix:
        f_out.write(str(row) + "\n")

    f_out.write("\nНовая матрица (блоки переставлены):\n")
    for row in new_matrix:
        f_out.write(str(row) + "\n")

print("Готово! Результаты в файле out3.txt")