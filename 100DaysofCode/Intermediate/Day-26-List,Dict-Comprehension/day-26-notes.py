#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Sreehari"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprehension
names = ["Sree", "Hari", "Sreehari", "Nandu", "Nandana", "Sreerag"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)

import pandas as pd

student_data = {
    "names" : ["Sree", "Hari", "Sreehari", "Nandu", "Nandana", "Sreerag"],
    "mark" : [1,2,3,4,5,6]
}
student_data_df = pd.DataFrame(student_data)
print(student_data_df)

# for (key,value) in student_data_df.items():
#     print(key)


"""
pandas have an inbuilt loops--iterrows()
"""

for (index,row) in student_data_df.iterrows():
    print(row)
    print(row.mark)