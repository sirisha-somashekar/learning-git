# create a nested list taking user input.
# this list should contain sublists containing names and marks of x subjects.
# output name and average marks.

# [['sirisha', 32, 34, 43], ['muzammil', 99, 99, 99], ..]

# enter number of students: 2
# enter number of subjects: 5
# enter name: sirisha
# enter marks: 99
# enter marks: 99
# enter marks: 99
# enter marks: 99
# enter marks: 99
# enter name: muzammil
# enter marks: 99
# enter marks: 99
# enter marks: 99
# enter marks: 99
# enter marks: 99
# student name: sirisha average marks: 99
# student name: muzammil average marks: 99

students_size = int(input('enter number of students: '))
subjects_size = int(input('enter number of subjects: '))
name_and_subjects_size = subjects_size + 1

students_list = []
for index in range(0, students_size):
    name_and_subjects_list = []
    for index in range(0, name_and_subjects_size):
        if index == 0:
            print('-' * 10)
            name = input('enter name: ')
            name_and_subjects_list.append(name)
        else:
            marks = int(input('enter marks: '))
            name_and_subjects_list.append(marks)
    students_list.append(name_and_subjects_list)

for student in students_list:
    name = student[0]
    marks = student[1:]
    avg_marks = sum(marks)/len(marks)
    print(f"student name: {name} average marks: {avg_marks}")

