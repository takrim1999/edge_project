import csv
header = ["Student Name", "Marks"]
n = int(input("How Many Students?\n>"))
student_dictionary = {}
marks = []
student_list = []
for i in range(n):
    name = input("Name: ")
    sub = int(input("how many subjects: "))
    for i in range(sub):
        marks.append(input(f"Mark of sub{i}: "))
    student_dictionary[name] = marks
# student_record = [
#     ["Takrim", 70],
#     ["Shehab", 80],
#     ["Sabbir", 80]
# ]
print(student_dictionary)
for i in student_dictionary:
    student_list.append([i,student_dictionary[i]])
# print(student_list)
with open('Stdent_name_marks.csv', "w", newline="") as record_file:
    writer = csv.writer(record_file)
    writer.writerow(header)
    writer.writerows(student_list)