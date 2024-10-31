def assign_grades(scores):
    grades = []
    for name, score in scores.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades.append((name, grade))
    return grades
scores = {input('Enter the name: '): int(input('Enter the scores: ')) for _ in range(4)}
print(assign_grades(scores))