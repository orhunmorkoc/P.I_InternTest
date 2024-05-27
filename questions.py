import pandas as pd

# Question 4
file_path_vaccination =  r'C:\Users\ORHUN\Desktop\country_vaccination_stats.csv'
df = pd.read_csv(file_path_vaccination)
#fills the nan values with 0's for now
df_filled_with_0 = df.fillna(0)
print(df_filled_with_0.head())


#Question 5
def fill_missing_vaccinations(df):

    min_vaccinations = df.groupby('country')['daily_vaccinations'].transform('min')
    df['daily_vaccinations'] = df['daily_vaccinations'].fillna(min_vaccinations)  #Gets the min vacations for each country then fills nan values with them
    df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

    return df

df_filled_with_min_vacation = fill_missing_vaccinations(df)
print("Question 5")
print(df_filled_with_min_vacation.head())

#Question 6
median_vaccinations_per_country = df_filled_with_min_vacation.groupby('country')['daily_vaccinations'].median().reset_index()
top_3_countries = median_vaccinations_per_country.sort_values(by='daily_vaccinations', ascending=False).head(3)

print("Question 6")
print(top_3_countries)

#Question 7

df_filled_with_min_vacation['date'] = pd.to_datetime(df_filled_with_min_vacation['date'])

specific_date_data = df_filled_with_min_vacation[df_filled_with_min_vacation['date'] == '2021-01-06']

# Calculate the total vaccinations done on 1/6/2021
total_vaccinations_on_specific_date = specific_date_data['daily_vaccinations'].sum()

print("Question 7")
print(f"Total vaccinations on 1/6/2021: {total_vaccinations_on_specific_date}")