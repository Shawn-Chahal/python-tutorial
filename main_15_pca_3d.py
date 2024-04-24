import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# If you have problems with rendering the 3D plot, uncomment the two lines below.
# import matplotlib
# matplotlib.use("QtAgg")


def plot_pca_3d(dataset):
    df = pd.read_csv(f"Dataset_{dataset}.csv")

    col_groups = df.columns[0]
    features = df.columns[1:]

    u_groups = df.loc[:, col_groups].unique()
    data = df.loc[:, features].to_numpy()

    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    pipe_dr = PCA(random_state=0)
    data_dr = pipe_dr.fit_transform(data)

    colors = ["tab:blue", "tab:orange", "tab:green"]
    markers = ["o", "D", "s"]

    # The main difference between setting up a 2D and 3D scatter plot is the way the axes are generated
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # The rest is relatively similar, with the addition of a z-axis
    for i, group in enumerate(u_groups):
        mask = (df.loc[:, col_groups] == group)
        x_plot = data_dr[mask, 0]
        y_plot = data_dr[mask, 1]
        z_plot = data_dr[mask, 2]
        # Note the additional z-axis
        ax.scatter(x_plot, y_plot, z_plot, label=group, color=colors[i], marker=markers[i],
                   alpha=0.7, s=16, edgecolors='black', linewidth=0.5)

    ax.set_xlabel(f"PC1 ({pipe_dr.explained_variance_ratio_[0]:.1%})")
    ax.set_ylabel(f"PC2 ({pipe_dr.explained_variance_ratio_[1]:.1%})")
    ax.set_zlabel(f"PC3 ({pipe_dr.explained_variance_ratio_[2]:.1%})")  # Note the additional z-axis
    ax.legend()

    plt.show()


plot_pca_3d("Iris")
plot_pca_3d("Wine")
