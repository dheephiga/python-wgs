from bokeh.plotting import figure, output_file, show
import pandas as pd
# x = [1,2,3,4,5]
# y=[4,6,2,4,3]
# output_file('op.html')
# p = figure(
#     title = 'Bokehhh',
#     x_axis_label = 'x axis',
#     y_axis_label = 'y axis',
# )
# p.line(x,y)
# show(p)

df = pd.read_csv('cars.csv')
car = df['Car']
hp = df['Horsepower']

p = figure(
    y_range = car,
    title = 'cars',
    tools=""
)

p.hbar(y=car,right=hp, left=0,fill_alpha=0.5)
show(p)
