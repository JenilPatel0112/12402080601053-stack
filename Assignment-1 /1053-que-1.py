n, k, m = map(int, input().split())

students = []
semester_data = {}
subject_topper = {}
subject_marks = {}

for _ in range(n):
    data = input().split()

    enrollment = data[0]
    name = data[1]
    semester = int(data[2])
    cpi = float(data[3])
    marks = list(map(int, data[4:]))

    avg_marks = sum(marks) / m

    student = (enrollment, name, semester, cpi, avg_marks, marks)
    students.append(student)

    if semester not in semester_data:
        semester_data[semester] = []

    semester_data[semester].append(student)

    for i in range(m):
        subject = f"S{i + 1}"
        mark = marks[i]

        if subject not in subject_topper or mark > subject_topper[subject]:
            subject_topper[subject] = mark
            subject_marks[subject] = [enrollment]

        elif mark == subject_topper[subject]:
            subject_marks[subject].append(enrollment)

for semester in sorted(semester_data):
    records = semester_data[semester]

    records.sort(key=lambda x: (-x[3], -x[4], x[0]))

    top_students = [student[0] for student in records[:k]]

    print(f"Semester {semester}: {' '.join(top_students)}")

for i in range(m):
    subject = f"S{i + 1}"
    toppers = sorted(subject_marks[subject])

    print(f"{subject}: {' '.join(toppers)}")
