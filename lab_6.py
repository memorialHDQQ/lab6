import math

# Открываем файл для чтения
with open("in1.txt", "r", encoding="utf-8") as f_in:
    lines = f_in.readlines()  # Читаем все строки в список

# Открываем файл для записи
with open("out1.txt", "w", encoding="utf-8") as f_out:
    f_out.write("a\t\tx\t\tz1\t\tz2\n")  # Шапка таблицы

    for line in lines:
        if line.strip() == "": continue  # Пропускаем пустые строки

        # Разделяем строку на две переменные
        parts = line.split()
        a = float(parts[0])
        x = float(parts[1])

        # Вычисляем z1 и z2 (формулы 30 варианта)
        z1 = (math.sin(a) ** 4 + 2 * math.sin(a) * math.cos(a) - math.cos(a) ** 4) / (math.tan(2 * a) - 1)
        z2 = math.cos(2 * a)

        # Записываем результат в файл
        f_out.write(f"{a:.2f}\t\t{x:.2f}\t\t{z1:.4f}\t\t{z2:.4f}\n")

print("Готово! Результаты в файле out1.txt")