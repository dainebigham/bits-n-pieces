import pandas

data = pandas.read_csv('squirrel_data.csv')

fur_color_count = data['Primary Fur Color'].value_counts().rename_axis('Fur Color').to_frame('Count')
fur_color_count.reset_index(level=0, inplace=True)

fur_color_count.to_csv('fur_color_count.csv')