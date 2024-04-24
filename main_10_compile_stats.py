import pandas as pd
from scipy.stats import f_oneway


# You can make a function that generalizes the code written in previous sections
def compile_stats(dataset):
    # The function takes a dataset name as input. Note how the Dataset file should be named.
    df = pd.read_csv(f"Dataset_{dataset}.csv")

    # This assumes that the groups are located in the first column and the remaining columns are features
    col_groups = df.columns[0]
    features = df.columns[1:]

    # Get the mean and standard deviation of each group for each feature
    df_mean = df.groupby(col_groups).mean()
    df_sd = df.groupby(col_groups).std()

    # Create the dictionary to eventually be exported as a csv
    data_export = {"feature": features}

    # Fill up the dictionary while also setting up the data structure for the ANOVA
    x_groups = []
    for group in df.loc[:, col_groups].unique():
        mask = (df.loc[:, col_groups] == group)
        x_group = df.loc[mask, features].to_numpy()
        x_groups.append(x_group)
        data_export[f"{group} (mean)"] = df_mean.loc[group, features].to_numpy()
        data_export[f"{group} (SD)"] = df_sd.loc[group, features].to_numpy()

    # Perform the ANOVA
    statistic, pvalue = f_oneway(*x_groups)

    # Fill up the dictionary with ANOVA results
    data_export["F_statistic"] = statistic
    data_export["p_value"] = pvalue

    # Convert dictionary to a pandas dataframe
    df_export = pd.DataFrame.from_dict(data_export)

    # You can rearrange the order the columns will appear in. In this case the columns are rearranged such that
    # the ANOVA results will appear before the mean and sd of each group.
    columns = list(df_export.columns[:1]) + list(df_export.columns[-2:]) + list(df_export.columns[1:-2])
    df_export = df_export.loc[:, columns]
    filename = f"Table_{dataset}_Stats.csv"

    # Export the dataframe as a csv file
    df_export.loc[:, columns].to_csv(filename, index=False)

    # Since this is being performed in a function, you may want it to print something when it's done exporting.
    print(filename)


# The Iris and Wine datasets have the same structure.
# I.e., groups in the first column, features in the remaining columns.
# Therefore, the same function can be used to perform statistical analysis on both of these datasets.

compile_stats("Iris")
compile_stats("Wine")
