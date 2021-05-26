student_heights = [180, 124, 165, 173, 189, 169, 146]
total = 0
number_of_students = len(student_heights)
for height in student_heights:
    total += height
print(f"The total height for this group is {total}")
average = total/number_of_students
print(f"The average height for this group is {average}")
