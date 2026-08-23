#import csv
import pandas as pd

# with open("weather_data - Sheet1.csv") as datas:
#     data=csv.reader(datas)
#     temperatures=[]
#     for i in data:
#       temperatures.append(i[1])
#     for i in temperatures:
#         print(i)

# temps=pd.read_csv("weather_data - Sheet1.csv")["temp"]
# average=0
# for i in temps:
#   average+=i
   
# average= average/len(temps)
# print(round(average,1))

# temps=pd.read_csv("weather_data - Sheet1.csv")["temp"]

# weather=pd.read_csv("weather_data - Sheet1.csv")
# monday=(weather[weather.day == "Monday"])
# print(monday.temp * 9/5 + 32)

# squirrels=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrels["Primary Fur Color"]

# fur=squirrels["Primary Fur Color"]
# squirrel_fur_count={
#   "fur color":["grey","red","black"],
#   "count":[0,0,0]
# }
# for i in fur:
#   if i== "Gray":
#     squirrel_fur_count["count"][0]+=1
#   elif i== "Cinnamon":
#     squirrel_fur_count["count"][1]+=1
#   elif i== "Black":
#     squirrel_fur_count["count"][2]+=1
    
    
# print(squirrel_fur_count)

# fur_count=pd.DataFrame(squirrel_fur_count)

# print(fur_count)