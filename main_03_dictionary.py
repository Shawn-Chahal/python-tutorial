from collections import defaultdict

# A dictionary works by using a key to access the corresponding value
# E.g., my_dict = { key: value }

data_employees = {
    "John": "Engineer",
    "Sara": "Doctor",
    "Paul": "Lawyer",
    "Jane": "Dentist"
}

print(f'data_employees = {data_employees}')
print(f"data_employees['John'] = {data_employees['John']}")  # Access a value using its key

data_employees['John'] = "Astronaut"  # Change the value for a given key
print(f'data_employees = {data_employees}')
print(50 * "-")

data_movies = {
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Inception": ["Action", "Adventure", "Sci-Fi"]
}

print(f'data_movies = {data_movies}')

data_movies['Inception'].append("Drama")  # 1) Access the list using the key. 2) Append a new genre.
print(f'data_movies = {data_movies}')

data_movies['Oppenheimer'] = ["Biography", "Drama", "History"]  # Add a new key on-demand
print(f'data_movies = {data_movies}')
print(50 * "-")

# Create an empty dictionary. However, when a new key is used it will assume there is an empty list as its value.
data_watchlist = defaultdict(list)  # Try replacing with a regular empty dictionary (i.e., {}) and see what happens.
print(f'data_watchlist = {data_watchlist}')

# You can now dynamically append data to lists.
data_watchlist["Movies"].append("Harry Potter")
data_watchlist["Movies"].append("Dune")
data_watchlist["TV"].append("3 Body Problem")
data_watchlist["TV"].append("Curb Your Enthusiasm")
data_watchlist["Music"].append("Taylor Swift")
print(f'data_watchlist = {data_watchlist}')
print(50 * "-")
