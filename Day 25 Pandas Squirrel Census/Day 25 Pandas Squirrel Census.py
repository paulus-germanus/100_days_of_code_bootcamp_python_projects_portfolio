import pandas as pd

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
fur_colors_dict = data["Primary Fur Color"].value_counts().to_csv("fur_colors.csv")
print(pd.read_csv("fur_colors.csv"))