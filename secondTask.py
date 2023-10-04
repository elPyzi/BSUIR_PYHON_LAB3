with open("students.txt", "w") as file:
    while True:
        student_data = input(
            "Введите фамилию студента и его средний балл через пробел (пустая строка для завершения): ")
        if not student_data:
            break
        parts = student_data.split()
        if len(parts) != 2:
            print("Ошибка: Введите фамилию и средний балл через пробел.")
            continue
        name, score = parts
        try:
            score = float(score)
        except ValueError:
            print("Ошибка: Средний балл должен быть числом.")
            continue
        file.write(f"{name} {score}\n")

with open("students.txt", "r") as file:
    lines = file.readlines()
low_scores = []
medium_scores = []
high_scores = []
max_score = -1
max_score_student = ""
for line in lines:
    parts = line.split()
    if len(parts) == 2:
        name = parts[0]
        score = float(parts[1])
        if 4 <= score < 6:
            low_scores.append(name)
        elif 6 <= score < 8:
            medium_scores.append(name)
        elif score >= 8:
            high_scores.append(name)
        if score > max_score:
            max_score = score
            max_score_student = name


print("Студенты с баллами от 4 до 6:")
print(", ".join(low_scores))

print("\nСтуденты с баллами от 6 до 8:")
print(", ".join(medium_scores))

print("\nСтуденты с баллами выше 8:")
print(", ".join(high_scores))

# Выводим студента с максимальным баллом
print("\nСтудент с максимальным баллом:")
print(f"{max_score_student}: {max_score}")
