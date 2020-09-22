import datetime
from unittest.mock import MagicMock

#from bokeh.plotting import figure, output_file, show

import bokeh.plotting

#output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
#show(p)

def test_draw(monkeypatch):
    figure_mock = MagicMock()
    line_mock = MagicMock()
    #show_mock = MagicMock()
    monkeypatch.setattr(bokeh.plotting, 'figure', figure_mock)
    monkeypatch.setattr(bokeh.plotting.figure, 'line', line_mock)
    #monkeypatch.setattr(bokeh.plotting.show, 'show', show_mock)

    fig = figure()
    hours = [datetime.datetime.now()]
    temperatures = [14.52]
    fig.line(hours, temperatures)

    _, called_temperatures = plot_date_mock.call_args[0]
    assert called_temperatures == temperatures  # check that plot_date was called with temperatures as second arg
    show_mock.assert_called()  # check that show is called

