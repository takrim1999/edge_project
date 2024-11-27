student_tuple = ("John Doe", 21, "Computer Science")
print("Name of the Student:", student_tuple[0])
print("Previous:",student_tuple)
student_tuple = list(student_tuple)
student_tuple[1] = 22
student_tuple = tuple(student_tuple)
print("Modified:", student_tuple)