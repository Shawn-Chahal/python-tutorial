import matplotlib.pyplot as plt
import numpy as np

# matplotlib is a library for making highly-customized visualizations


# Create 31 x-values from -5 to 5 (including -5 and 5)
x = np.linspace(-5, 5, 31)

# Create 31 y-values using the following cubic function
y = x ** 3 - 9 * x

print(f"x = {x}")
print(f"y = {y}")

# Create a figure (the overall image) and an axes (a subfigure)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(3.75, 3.5), dpi=600, layout="constrained")

# Add a line plot for the x and y values to the axes
ax.plot(x, y, color="black", label="trendline", linestyle="-", linewidth=2, zorder=0)

# Add a scatter plot to visualize the actual x and y data points
ax.scatter(x, y, color="tab:orange", label="samples", marker="D", s=25, edgecolors='black', linewidth=1, zorder=1)

# Set the x-axis and y-axis labels and the title
ax.set_xlabel("x", fontsize=10)
ax.set_ylabel("y", fontsize=10)
ax.set_title("Cubic function", fontsize=11)

# Add a legend
ax.legend(loc="upper center", ncols=2, fontsize=7)

# You can also add text if there is something you want to highlight in a certain part of the figure
ax.text(x[5] + 0.5, y[5] - 0.5, "Message", ha="left", va="top")

filename = f"Figure_Cubic.png"

# Save the figure (PNG file recommended)
fig.savefig(filename)

# Close the figure
plt.close(fig)

print(filename)
