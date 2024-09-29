"""Filtration Python Script"""
import pandas as pd

read_data = pd.read_csv("data.csv")

read_data.drop(columns=["Footnote", "Data As Of", "Pneumonia Deaths", "Influenza Deaths", "Pneumonia or Influenza",
                        "Pneumonia, Influenza, or COVID-19 Deaths", "Week Ending Date", "Indicator", "Group"], inplace=True)

regional_data = read_data[read_data["Jurisdiction"].str.contains("HHS")]
regional_data_final = regional_data[regional_data["Age Group"].str.contains("All Ages")]

regional_data_final.drop(columns=["Age Group"], inplace=True)

year_2019_2020 = regional_data_final[regional_data_final["MMWRyear"] == 2020]

year_2021 = regional_data_final[regional_data_final["MMWRyear"] == 2021]

year_2022 = regional_data_final[regional_data_final["MMWRyear"] == 2022]

year_2023 = regional_data_final[regional_data_final["MMWRyear"] == 2023]

list_of_regions = [year_2019_2020, year_2021, year_2022, year_2023]

for i in range(4):
    for j in range(1, 11):
        current = list_of_regions[i][list_of_regions[i]["Jurisdiction"].str.contains(r'\b' + "HHS Region " + str(j) + r'\b', regex=True, case=False)]
        current.to_csv(f"covid_frame{i}{j-1}.csv", index=False)

"""Data for Tableau"""
read_data = pd.read_csv("data.csv")

read_data.drop(columns=["Footnote", "Data As Of", "Pneumonia Deaths", "Influenza Deaths", "Pneumonia or Influenza",
                        "Pneumonia, Influenza, or COVID-19 Deaths", "Week Ending Date", "Indicator", "Group"], inplace=True)

regional_data2 = read_data[read_data["Jurisdiction"].str.contains("HHS")]
regional_data_final2 = regional_data[regional_data["Age Group"].str.contains("All Ages")]

regional_data_final2.drop(columns=["Age Group"], inplace=True)
regional_data_final2 = regional_data_final2[regional_data_final2["Jurisdiction"].str.contains(r'\b' + "HHS Region " + r'\b', regex=True, case=False)]

winter1 = regional_data_final2[((regional_data_final2["MMWRweek"] >= 49) & (regional_data_final2["MMWRweek"] <= 52))]
winter2 = regional_data_final2[((regional_data_final2["MMWRweek"] >= 1) & (regional_data_final2["MMWRweek"] <= 9))]
winter = pd.concat([winter1, winter2], ignore_index = True)
winter_sums = []
spring = regional_data_final2[((regional_data_final2["MMWRweek"] >= 10) & (regional_data_final2["MMWRweek"] <= 22))]
spring_sums = []
summer = regional_data_final2[((regional_data_final2["MMWRweek"] >= 23) & (regional_data_final2["MMWRweek"] <= 35))]
summer_sums = []
fall = regional_data_final2[((regional_data_final2["MMWRweek"] >= 36) & (regional_data_final2["MMWRweek"] <= 49))]
fall_sums = []
for i in range(1, 11):
    spring_sums.append((spring.loc[spring["Jurisdiction"] == "HHS Region " + str(i), ["COVID-19 Deaths"]]).sum())
    winter_sums.append((winter.loc[winter["Jurisdiction"] == "HHS Region " + str(i), ["COVID-19 Deaths"]]).sum())
    summer_sums.append((summer.loc[summer["Jurisdiction"] == "HHS Region " + str(i), ["COVID-19 Deaths"]]).sum())
    fall_sums.append((fall.loc[fall["Jurisdiction"] == "HHS Region " + str(i), ["COVID-19 Deaths"]]).sum())

print(winter_sums)
print(spring_sums)
print(summer_sums)
print(fall_sums)