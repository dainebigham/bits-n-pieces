import pandas

# data = pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()

# # get data in columns
# # print(data.temp)
# # print(data['temp'].mean())
# max = data.temp.max()

# # get data in rows
# monday = data[data.day == 'Monday']
# print(data[data.temp == max])
# print(monday.temp)
# # print((monday.temp * 9) / 5 + 32) fahrenheit conversion

data_dict = {
    'names': ['Harry', 'Ron', 'Hermione'],
    'score': ['80', '77', '100']
}

data = pandas.DataFrame(data_dict)

data.to_csv('hogwarts.csv')