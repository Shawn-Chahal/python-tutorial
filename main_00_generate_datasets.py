from sklearn.datasets import load_wine, load_iris

"""
    Downloads and cleans the Iris Dataset so that 
    the first column contains the targets and
    the remaining columns contain the features. 
"""
df_iris = load_iris(as_frame=True).frame
target_names_iris = load_iris().target_names
columns_iris = list(df_iris.columns)[:-1]
df_iris.loc[:, "species"] = [target_names_iris[i] for i in df_iris.loc[:, "target"]]
columns_iris = ["species"] + columns_iris
filename_iris = "Dataset_Iris.csv"
df_iris.loc[:, columns_iris].to_csv(filename_iris, index=False)
print(filename_iris)

"""
    Downloads and cleans the Wine Dataset so that 
    the first column contains the targets and
    the remaining columns contain the features. 
"""
df_wine = load_wine(as_frame=True).frame
target_names_wine = load_wine().target_names
columns_wine = list(df_wine.columns)[:-1]
df_wine.loc[:, "wine"] = [target_names_wine[i].replace("class", "wine") for i in df_wine.loc[:, "target"]]
columns_wine = ["wine"] + columns_wine
filename_wine = "Dataset_Wine.csv"
df_wine.loc[:, columns_wine].to_csv(filename_wine, index=False)
print(filename_wine)
