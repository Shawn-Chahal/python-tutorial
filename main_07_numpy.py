import numpy as np

# numpy arrays provide an efficient way to perform calculations on vectors and matrices
x_list = [7, 4, 5]
x_array = np.array(x_list)

y_list = [2, 1, 3]
y_array = np.array(y_list)

print(50 * "-")
print(f"x_list     = {x_list}")
print(f"x_array    = {x_array}")
print(f"x_list[1]  = {x_list[1]}")
print(f"x_array[1] = {x_array[1]}")

# Recall that adding two lists together will concatenate them
z_list = x_list + y_list
print(50 * "-")
print(f"         x_list = {x_list}")
print(f"         y_list = {y_list}")
print(f"x_list + y_list = {z_list}")

# Adding two numpy arrays will perform element-wise addition
z_array = x_array + y_array
print(50 * "-")
print(f"          x_array = {x_array}")
print(f"          y_array = {y_array}")
print(f"x_array + y_array = {z_array}")

print(50 * "-")
print(f"           x_array = {x_array}")
print(f"           y_array = {y_array}")
print("")

# You can perform many element-wise additions using numpy
print(f"x_array +  y_array = {x_array + y_array}")  # Addition
print(f"x_array -  y_array = {x_array - y_array}")  # Subtraction
print(f"x_array *  y_array = {x_array * y_array}")  # Multiplication
print(f"x_array /  y_array = {x_array / y_array}")  # Division
print(f"x_array ** y_array = {x_array ** y_array}")  # Exponentiation (i.e., x to the power of y)

# You can also perform the dot product using numpy
print(f"np.dot(x_array, y_array) = {np.dot(x_array, y_array)}")

# Many common functions are already built in to numpy
print(50 * "-")
print(f"         y_array  = {y_array}")
print("")
print(f" np.sqrt(y_array) = {np.sqrt(y_array)}")
print(f"  np.sin(y_array) = {np.sin(y_array)}")
print(f"np.log10(y_array) = {np.log10(y_array)}")
print(f"  np.exp(y_array) = {np.exp(y_array)}")

# Basic stats can be obtained using numpy
a = np.array([2, 3, 1, 12, 5])
print(50 * "-")
print(f"          a  = {a}")
print("")
print(f"  np.mean(a) = {np.mean(a)}")
print(f"   np.std(a) = {np.std(a):.2f}")
print(f"np.median(a) = {np.median(a)}")
print(f"   np.max(a) = {np.max(a)}")
print(f"   np.min(a) = {np.min(a)}")
print(f"   np.sum(a) = {np.sum(a)}")

# Consider this example with:
# 5 samples
# 3 features: Intensity of A, Intensity of B, Intensity of C

sample_0 = [1.5, 2.9, 3.5]
sample_1 = [5.8, 2.7, 9.2]
sample_2 = [6.2, 2.4, 8.4]
sample_3 = [2.9, 9.3, 6.6]
sample_4 = [2.1, 6.6, 5.1]

x = [
    sample_0,
    sample_1,
    sample_2,
    sample_3,
    sample_4
]

x = np.array(x)

# Calculate the mean and standard deviation across axis 0.
# Note that axis 0 is the rows, axis 1 is the columns.
# The easiest way to interpret this is that axis 0 will be "collapsed" or "aggregated".
# The numpy array "x" has a shape of (5, 3) (i.e., 5 rows, 3 columns)
# Therefore x_mean and x_sd will have a size of 3 since the mean and sd are calculated across rows.
x_mean = np.mean(x, axis=0)
x_sd = np.std(x, axis=0)

print(50 * "-")
print(f"x = \n{x}")
print("")
print(f"x.shape = {x.shape}")
print(f"x_mean  = {x_mean}")
print(f"x_sd    = {x_sd}")
print(f"x[1, 2] = {x[1, 2]}")  # Note the slight difference between accessing values from a 2D numpy array vs 2D list.

# You can set the number of decimals to be printed, for example, by using the ".2f" to indicate 2 decimal places.
# This will only affect the appearance of the value when printing, it won't change the original value in your code.
print(50 * "-")
print(f"Intensity A: {x_mean[0]:.2f} +/- {x_sd[0]:.2f}")
print(f"Intensity B: {x_mean[1]:.2f} +/- {x_sd[1]:.2f}")
print(f"Intensity C: {x_mean[2]:.2f} +/- {x_sd[2]:.2f}")
print(50 * "-")
