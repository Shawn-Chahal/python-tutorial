from collections import defaultdict

import pandas as pd

# The pandas library can be used to import data and export statistical results

# These settings allow you to see the full dataframe in these examples.
# If you aren't printing your dataframes then these lines won't do anything.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Import your data as a csv file
df = pd.read_csv("Dataset_Iris.csv")

# Print the dataframe
print("df")
print(df)
print(100 * "-")

# Group the samples by the values in the column named "species" and
# calculate the mean of each of the remaining columns for each species.
df_mean = df.groupby("species").mean()

# Export the dataframe to a csv file.
df_mean.to_csv("Table_Iris_Mean.csv")

print("df_mean")
print(df_mean)
print(100 * "-")

# Repeat the process for standard deviation.
df_sd = df.groupby("species").std()
df_sd.to_csv("Table_Iris_SD.csv")

print("df_sd")
print(df_sd)
print(100 * "-")

s = "versicolor"
f = "sepal width (cm)"

# Print the statistics for a single species and feature.
print(f"{s} - {f}: {df_mean.at[s, f]:.2f} +/- {df_sd.at[s, f]:.2f}")
print(100 * "-")

u_species = df.loc[:, "species"].unique()  # Gets all the unique values in the column named "species"
features = df.columns[1:]  # Gets the header for all the columns except the first one

print(f"u_species = {u_species}")
print(f"features = {features}")
print(100 * "-")

data_export = defaultdict(list)
# The keys in the dictionary data_export will become the column headers for the csv file you export.
# The values (i.e., the list associated with each key) will contain the values under each column header.

# Each iteration of the outer loop adds a row to our future csv file.
for s in u_species:
    data_export["species"].append(s)

    # This inner loop will make sure each feature gets its own column for the mean and SD.
    for f in features:
        data_export[f"{f} (mean)"].append(df_mean.at[s, f])
        data_export[f"{f} (SD)"].append(df_sd.at[s, f])

print("data_export")
print(data_export)
print(100 * "-")
# Convert the dictionary into a pandas dataframe.
df_export = pd.DataFrame.from_dict(data_export)

print("df_export")
print(df_export)
print(100 * "-")
# Export the dataframe as a csv file.
# index=False indicates not to print the index which will just be a numbered list in this case (e.g., 0, 1, 2)
df_export.to_csv("Table_Iris_MeanSD.csv", index=False)
