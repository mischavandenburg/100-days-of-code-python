import pandas

data = pandas.read_csv("squirrel.csv")
series = data["Primary Fur Color"].value_counts()
print(series.Gray)

result = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [series.Gray, series.Cinnamon, series.Black]
        }

file = pandas.DataFrame(result)
file.to_csv("new_squirrels.csv")
