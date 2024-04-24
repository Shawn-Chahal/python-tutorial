# List: You can make a list of variables
x = [0, 1, 2, 3, 4]
y = [5, 6, 7, 8, 9, 10, 11]
z = x + y

# Adding lists together will concatenate them (i.e., join them)
print(50 * "-")
print(f"    x = {x}")
print(f"    y = {y}")
print(f"x + y = {z}")

# You can access elements in a list via their index.
# The first element in a list is accessed using an index of 0.
print(50 * "-")
print(f"        z = {z}")
print(f"     z[0] = {z[0]}")  # Access the 1st value in the list.
print(f"     z[1] = {z[1]}")  # Access the 2nd value in the list.
print(f"    z[-1] = {z[-1]}")  # Access the last value in the list.
print(f"    z[-2] = {z[-2]}")  # Access the 2nd last value in the list.

# You can access a slice of the list by various methods
print(50 * "-")
print(f"   z[2:4] = {z[2:4]}")  # Select indices 2 to 4, without including 4
print(f"z[1:10:2] = {z[1:10:2]}")  # Select indices 1 to 10, without including 10, in steps of 2.
print(f"  z[::-1] = {z[::-1]}")  # Select all indices, in steps of -1. This reverses the list.
print(f"   len(z) = {len(z)}")  # Return the length of the list.

print(50 * "-")
print(f"z = {z}")

# You can modify an element in a list.
z[5] = 473
print(f"z = {z}")

# You can append a new value to the end of the list.
z.append(241)
print(f"z = {z}")

# You can extend a list with content from another list.
a = [700, 800, 900]
z.extend(a)
print(f"z = {z}")

z[-1] = 12
print(f"z = {z}")

print(50 * "-")

# Integer vs float
x_int = 5
x_float = 5.0
print(f"              z = {z}")
print(f"          x_int = {x_int}")
print(f"       z[x_int] = {z[x_int]}")
# print(f"     z[x_float] = {z[x_float]}") # This won't work. You need to use an integer as an index.
print(f"z[int(x_float)] = {z[int(x_float)]}")  # You can convert a float into an integer and then use it as an index.

# 2D Lists are a "list of lists"
a = [
    [1, 2, 3],
    [5, 2, 9],
    [6, 2, 8],
    [2, 9, 6],
    [2, 6, 5],
]

# The same rules of indexing apply here.
# Get the 2nd list (at index 1): [5, 2, 9]
# Get the 3rd value in this list (at index 2): 9
print(50 * "-")
print(f"a       = {a}")
print(f"a[1]    = {a[1]}")
print(f"a[1][2] = {a[1][2]}")
print(50 * "-")
