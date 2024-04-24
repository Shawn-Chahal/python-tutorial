import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Dataset_Iris.csv")

col_labels = df.columns[0]
features = df.columns[1:]

u_labels = df.loc[:, col_labels].unique()
n_features = len(features)

# The color and marker to be used for the 3 species.
colors = ["tab:blue", "tab:orange", "tab:green"]
markers = ["o", "D", "s"]

fig, axs = plt.subplots(nrows=n_features, ncols=n_features, figsize=(9, 9), dpi=600, layout="constrained")

for i, feature_x in enumerate(features):
    for j, feature_y in enumerate(features):
        # This is selecting the axes (e.g., subfigure) to draw
        ax = axs[j, i]  # Select the j-th row and the i-th column

        for k, label in enumerate(u_labels):
            # These concepts should be familiar from previous sections
            mask = (df.loc[:, col_labels] == label)
            x_plot = df.loc[mask, feature_x].to_numpy()
            y_plot = df.loc[mask, feature_y].to_numpy()

            # Create a scatter plot for feature_y vs feature_x for the k-th label (i.e., species)
            ax.scatter(x_plot, y_plot, label=label, color=colors[k], marker=markers[k],
                       alpha=0.7, s=16, edgecolors='none', linewidth=0.5)

        # Only set the x-axis label if the axes is in the bottom row.
        if j == n_features - 1:
            ax.set_xlabel(feature_x)

        # Only set the y-axis label if the axes is in the left column.
        if i == 0:
            ax.set_ylabel(feature_y)

# Only show the legend in the top-left subfigure.
axs[0, 0].legend(loc="upper left", fontsize=7)

filename = f"Figure_Iris_Scatter2D.png"
fig.savefig(filename)
plt.close(fig)

print(filename)
