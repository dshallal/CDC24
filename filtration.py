"""Filtration Python Script"""
import pandas as pd

read_data = pd.read_csv("data.csv")

read_data.drop(columns=["Footnote", "Data As Of", "Pneumonia Deaths", "Influenza Deaths", "Pneumonia or Influenza",
                        "Pneumonia, Influenza, or COVID-19 Deaths"], inplace=True)

regional_data = read_data[read_data["Jurisdiction"].str.contains("HHS")]
regional_data_final = regional_data[regional_data["Age Group"].str.contains("All Ages")]

regional_data_final.drop(columns=["Age Group"], inplace=True)

year_2019_2020 = regional_data_final[regional_data_final["MMWRyear"] == 2020]

year_2021 = regional_data_final[regional_data_final["MMWRyear"] == 2021]

year_2022 = regional_data_final[regional_data_final["MMWRyear"] == 2022]

year_2023 = regional_data_final[regional_data_final["MMWRyear"] == 2023]

list_of_regions = [year_2019_2020, year_2021, year_2022, year_2023]

list_of_regions2 = []

for i in range(4):
    for j in range(1, 11):
        current = list_of_regions[i][list_of_regions[i]["Jurisdiction"].str.contains(r'\b' + "HHS Region " + str(j) + r'\b', regex=True, case=False)]
        list_of_regions2.append(current)



print(list_of_regions2[10])