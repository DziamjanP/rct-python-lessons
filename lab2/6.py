def find_scoring_student(students: dict):
    max_student = list(students.keys())[0]
    for student in students.keys():
        if students[student] > students[max_student]: max_student = student
    return max_student

if __name__ == '__main__':
    students = {
        'Мікола': 9.4,
        'Андрэй': 5.6,
        'Васіль': 9.2,
        'Дар\'я': 8.4,
        'Аляксей': 7.8,
        'Ірына': 6.9,
    }
    print(find_scoring_student(students))