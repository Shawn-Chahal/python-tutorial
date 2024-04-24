# This while loop will continue as long as the condition x < 5 is true.
x = 0
while x < 5:
    print(x)
    x += 1  # Increase the value of x by 1.

print(50 * "-")

# Print the first ten square numbers
for i in range(10):  # Iterate 10 times with i ranging from 0 to 9.
    print(f"{i} ** 2 = {i ** 2}")

print(50 * "-")

# print all the numbers between 1 and 100 that are divisible by 7, but not 3
for i in range(1, 101):
    if (i % 7 == 0) and (i % 3 != 0):
        print(i)

print(50 * "-")

movies = ["The Dark Knight", "Inception", "Interstellar"]

# You can also iterate over elements in a list directly
for movie in movies:
    print(movie)

print(50 * "-")

# Sometimes you may want to keep track of a number as you iterate
for i, movie in enumerate(movies, start=1):
    print(f"{i}) {movie}")

print(50 * "-")
