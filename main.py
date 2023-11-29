# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
import pandas
# data_new = pandas.read_csv("./weather_data.csv")
# print(data_new)
#
# data_dict = data_new.to_dict()
# print(data_dict)
#
# data_list = data_new["temp"].to_list()
# print(data_list)
#
# # Calculate the average temperature
# total_temp = 0
# for i in range(0, len(data_list)):
#     total_temp += data_list[i]
#
# avg_temp = int(total_temp / 7)
# print(avg_temp)
#
# # another way to calculate average temp
# print(int(data_new["temp"].mean()))
#
# # max temp from data frame
# print(data_new["temp"].max())
#
# # print out a column - Day column
# print(data_new.day)
#
# # print out a row - Monday
# print(data_new[data_new.day == "Monday"])
#
# # print out the row with the max temp
# print(data_new[data_new.temp == data_new["temp"].max()])
#
# # print Monday's temp in Fahrenheit
# monday = data_new[data_new.day == "Monday"]
# mon_temp = monday.temp[0]
# mon_temp_F = (mon_temp * (9/5)) + 32
# print(mon_temp_F)
#
# # Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Ryan"],
#     "score": [90, 72, 57],
# }
# new_dict = pandas.DataFrame(data_dict)
# print(new_dict)


# Create a new data frame for squirrels of different colors.
squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_data.rename(columns={'Primary Fur Color': "Primary_Fur_Color"}, inplace= True)
fur_data = squirrel_data.Primary_Fur_Color
black = 0
gray = 0
cinnamon = 0
for row in fur_data:
    if row == "Gray":
        gray += 1
    elif row == "Cinnamon":
        cinnamon += 1
    elif row == "Black":
        black += 1

squirrel_fur_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [f"{gray}", f"{cinnamon}", f"{black}"]
}
new_fur_data = pandas.DataFrame(squirrel_fur_data)
with open("squirrel_count.csv", mode='w') as new_file:
    new_file.write(new_fur_data.to_csv())

