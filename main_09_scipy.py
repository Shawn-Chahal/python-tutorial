import pandas as pd
from scipy.stats import f_oneway

# scipy is a library that can be used to perform a variety of statistical analyses

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("Dataset_Iris.csv")

print("df")
print(df)
print(100 * "-")

u_species = df.loc[:, "species"].unique()
features = df.columns[1:]

# Many of the statistical tests in scipy require data to be divided into a list
# where each element in the list represents one "group". In this case the group is the species.

x_groups = []
for s in u_species:
    # This creates a mask which identifies all the rows in df that belong to species s.
    mask = (df.loc[:, "species"] == s)

    # The mask can then be used to only access the data for species s.
    x_group = df.loc[mask, features].to_numpy()  # The data is converted into a numpy array.
    x_groups.append(x_group)

# Perform a one-way ANOVA
statistic, pvalue = f_oneway(*x_groups)
# Note the * symbol here. This is just saying to "unpack" the elements in the list.
# E.g., if x_groups = [a, b, c]
# then the following function calls are equivalent
# f_oneway(*x_groups)
# f_oneway(x_groups[0], x_groups[1], x_groups[2])
# f_oneway(a, b, c)

# Create the dictionary to export
data_export = {
    "feature": features,
    "F_statistic": statistic,
    "p_value": pvalue
}

# Convert the dictionary to a pandas dataframe
df_export = pd.DataFrame.from_dict(data_export)

# Export ANOVA results to a csv file
df_export.to_csv("Table_Iris_1WayAnova.csv", index=False)

print("df_export")
print(df_export)
print(100 * "-")
