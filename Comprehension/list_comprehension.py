# numbers = [1, 2, 3]
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# new_list = []

# for n in numbers:
#     add_1 = n + 1

#     new_list.append(add_1)

# new_list = [n + 1 for n in numbers]
# new_list = [n * 2 for n in range(1,5)]
# new_list = [name.upper() for name in names if len(name) > 5]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [n**2 for n in numbers]
# results = [n for n in numbers if n % 2 == 0]

with open('file1.txt', 'r') as f:
    numbers1 = f.readlines()

with open('file2.txt', 'r') as f:
    numbers2 = f.readlines()

results = [int(n) for n in numbers1 if n in numbers2]

print(results)
