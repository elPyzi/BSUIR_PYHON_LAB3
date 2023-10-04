with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку данных (пустая строка для завершения): ")
        if not line:
            break
        f1.write(line + "\n")
with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    for line in f1:
        cleaned_line = line.strip()
        if cleaned_line.endswith("А") or cleaned_line.endswith("а"):
            f2.write(cleaned_line + "\n")
        elif cleaned_line.endswith("A") or cleaned_line.endswith("a"):
            f2.write(cleaned_line + "\n")
print("Программа завершена. Строки, заканчивающиеся на 'A' или 'А', скопированы в файл F2.")