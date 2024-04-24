import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols


# The statsmodels library contains more advanced statistical analysis such as two-way ANOVA

def clean_feature_label(feature_label):
    set_alphanumeric = set(list("0123456789abcdefghijklmnopqrstuvwxyz"))
    new_feature_label = "feature_"
    for char in feature_label.lower():
        if char in set_alphanumeric:
            new_feature_label += char
        else:
            new_feature_label += "_"

    return new_feature_label


def two_way_anova(df_data, feature_, factor_1, factor_2):
    # The statsmodels formula has certain requirements on how the features must be named
    # This function cleans the feature names accordingly by replacing non-alphanumeric symbols with an underscore
    feature_clean = clean_feature_label(feature_)
    df_data.loc[:, feature_clean] = df_data.loc[:, feature_]

    # The following is code from the statsmodels library to perform a Two-Way ANOVA
    # Note: This format can easily be expanded to do an n-way ANOVA.
    formula = f"{feature_clean} ~ C({factor_1}) + C({factor_2}) + C({factor_1}):C({factor_2})"
    model = ols(formula=formula, data=df_data).fit()
    df_anova = sm.stats.anova_lm(model, typ=2)

    return df_anova, feature_clean


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("Dataset_Iris.csv")

# Create a fake factor for the purpose of this example
features = list(df.columns[1:])
regions = len(df) * ["North", "East", "South", "West"]
regions = regions[:len(df)]
df.loc[:, "region"] = regions
columns = ["species", "region"] + features
df = df.loc[:, columns]

print("df")
print(df)
print(100 * "-")

# for each feature, do a two-way ANOVA using factor_1 and factor_2 and export the results
for feature in features:
    df_export, feature_name = two_way_anova(df, feature, factor_1="species", factor_2="region")
    df_export.to_csv(f"Table_Iris_2WayANOVA_{feature_name}.csv")

    print(feature)
    print(df_export)
    print(100 * "-")
