# Задача №1

# def function(list: list) -> dict:
#     dict = {}
#     for i in list:
#         if dict.get(i, 0):
#             dict[i] += 1 
#         else:
#             dict[i] = 1
#     return dict

# numbers_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# print(function(numbers_list))

# Задача №2

import csv

results = []

with open("lesson7.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        results.append(row)
        
    with open("lesson7.xlsx", "w") as f:
        writer = csv.DictWriter(f, fieldnames = [" ", "id", "name", "phone"])
        writer.writeheader()
        keys_ = list(results[0].keys())
        values_0 = list(results[0].values())
        values_1 = list(results[1].values())
        values_2 = list(results[2].values())
        values_ = [values_0, values_1, values_2]

        for i in range(len(keys_)):
             writer.writerow({" ": f"person{i+1}", "id" : values_[i][0], "name" : values_[i][1], "phone": values_[i][3]})