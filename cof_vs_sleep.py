import csv
import plotly.express as v


with open("coffee_vs_sleeping_hours.csv") as csv_file:
    df = csv.DictReader(csv_file)
    graph=v.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
    graph.show()