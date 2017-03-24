import pandas

from bokeh.plotting import figure , output_file , show

df = pandas.read_excel("C:\\Repos\\bertugmete.git\\samples\\Python\\InteractiveDataVisualization\\InteractiveDataVisualization\\verlegenhuken.xlsx",sheetname = 0)

df["Temperature"] = df["Temperature"] / 10

df["Pressure"] = df["Pressure"] / 10

p = figure(plot_width  = 500 , plot_height = 500)

p.title = "Sicaklik ve Hava Basinci"

p.xaxis.minor_tick_line_color = None

p.yaxis.minor_tick_line_color = None

p.xaxis.axis_label = "Temperature (Celcius)"

p.yaxis.axis_label = "Pressure"

p.circle(df["Temperature"] , df["Pressure"],size = 0.5) 

output_file("weather.html")

show(p)