import random as r
import pandas as pd

# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# scores = {student:r.randint(1, 100) for student in names}
# passed = {student:score for (student,score) in scores.items() if score > 60}

# sentence = 'What is the air velocity of an unladen swallow?'
# results = {word:len(word) for word in sentence.split()}

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {day:temp*9/5+32 for (day,temp) in weather_c.items()}
students = {
    'students': ['Angela', 'Lilly', 'James'],
    'scores': [56, 98, 76]
}

# Looping through dictionaries
# for (key,value) in students.items():
#     print(value)

students_df = pd.DataFrame(students)

# Looping through dataframes
# for (key, value) in students_df.items():
#     print(value)

# for (index, row) in students_df.iterrows():
#     print(row)