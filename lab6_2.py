import math, random

with open("in2.txt", "r", encoding="utf-8") as f_in:
    n = int(f_in.readline())  # Читаем количество точек
    params = f_in.readline().split()  # Читаем строку с параметрами кольца
    x0 = float(params[0])
    y0 = float(params[1])
    r1 = float(params[2])
    r2 = float(params[3])

# Генерируем точки
points = []
for i in range(n):
    points.append([random.uniform(-10, 10), random.uniform(-10, 10)])

# Ищем точки в кольце
with open("out2.txt", "w", encoding="utf-8") as f_out:
    f_out.write(f"Центр кольца: ({x0}, {y0}), R1={r1}, R2={r2}\n")
    f_out.write("Точки в кольце:\n")

    count = 0
    for p in points:
        dist = math.sqrt((p[0] - x0) ** 2 + (p[1] - y0) ** 2)
        if r1 <= dist <= r2:
            f_out.write(f"({p[0]:.2f}, {p[1]:.2f})\n")
            count += 1

    if count == 0:
        f_out.write("Нет таких точек\n")

print("Готово! Результаты в файле out2.txt")