subjects_dict = {}

with open("subjects.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(":")

    if len(parts) == 2:
        subject = parts[0].strip()
        info = parts[1].strip()

        lesson_parts = info.split()

        total_lessons = 0

        for part in lesson_parts:
            if "(" in part and ")" in part:
                num_lessons = int(part.split("(")[0])
                total_lessons += num_lessons

        subjects_dict[subject] = total_lessons

print(subjects_dict)
