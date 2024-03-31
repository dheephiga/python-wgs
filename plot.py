from bokeh.plotting import figure, output_file, show
x = [1,2,3,4,5]
y=[4,6,2,4,3]

output_file('op.html')


p = figure(
    title = 'Bokehhh',
    x_axis_label = 'x axis',
    y_axis_label = 'y axis',
)

p.line(x,y)
show(p)