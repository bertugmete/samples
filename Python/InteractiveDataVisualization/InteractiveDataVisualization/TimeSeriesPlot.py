import pandas

from bokeh.plotting import figure , output_file , show

df = pandas.read_csv("http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",parse_dates = ["Date"])

p = figure(width = 500 , height = 500 ,x_axis_type = "datetime",responsive = True)

p.line(df["Date"] , df["Close"],color = "Orange",alpha = 0.5)

output_file("Timeseries.html")

show(p)