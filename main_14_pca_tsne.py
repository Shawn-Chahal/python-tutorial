import pandas as pd
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


# The scikit-learn library (sklearn) contains various unsupervised and supervised machine learning models

def plot_dimensionality_reduction(dataset, dr_type):
    df = pd.read_csv(f"Dataset_{dataset}.csv")

    col_groups = df.columns[0]
    features = df.columns[1:]

    u_groups = df.loc[:, col_groups].unique()

    data = df.loc[:, features].to_numpy()

    # In the wine dataset, some of the features have very large values and others have very small values
    # Therefore, it is important to place all the features on the same scale before doing a PCA or t-SNE
    # The standard scaler will subtract the mean of each feature and divide by its standard deviations
    # In other word's it will convert the data into z-scores centered at 0 with a standard deviation of 1
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    fig, ax = plt.subplots(1, 1, figsize=(4.0, 4.0), dpi=600, layout='constrained')

    if dr_type == "PCA":
        pipe_dr = PCA(random_state=0)

    elif dr_type == "TSNE":
        # perplexity can typically be set from 5 to 50
        # Many algorithms in the scikit-learn package rely on random number generation
        # If random_state is not set for T-SNE, then the figures will likely look different each time the code is run
        # It is recommended to set the random_state so that you get the same random_numbers each time your code is run
        pipe_dr = TSNE(perplexity=30, random_state=0)

    else:
        pipe_dr = None

    # Perform the dimensionality reduction
    data_dr = pipe_dr.fit_transform(data)

    # The colors and markers to be used for each group
    # For example, if there are only 3 groups, then the first three colors and markers will be used
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:gray", "tab:olive"]
    markers = ["o", "D", "s", "^", "X", "P", "*", "v"]

    for i, group in enumerate(u_groups):
        mask = (df.loc[:, col_groups] == group)
        x_plot = data_dr[mask, 0]
        y_plot = data_dr[mask, 1]

        ax.scatter(x_plot, y_plot, label=group, color=colors[i], marker=markers[i],
                   alpha=0.7, s=16, edgecolors='black', linewidth=0.5)

    if dr_type == "PCA":
        # Write the explained variance on each axis for PCA
        ax.set_xlabel(f"PC1 ({pipe_dr.explained_variance_ratio_[0]:.1%})")
        ax.set_ylabel(f"PC2 ({pipe_dr.explained_variance_ratio_[1]:.1%})")
    else:
        ax.set_xlabel(f"{dr_type}1")
        ax.set_ylabel(f"{dr_type}2")

    ax.set_title(f"{dataset} ({len(features)} features)")
    ax.legend()

    filename = f"Figure_{dataset}_{dr_type}.png"

    fig.savefig(filename)
    plt.close(fig)

    print(filename)


for dataset_ in ["Iris", "Wine"]:
    for dr_type_ in ["PCA", "TSNE"]:
        plot_dimensionality_reduction(dataset_, dr_type_)

# Consider the effect of scaling
# Consider the effect of perplexity for T-SNE
