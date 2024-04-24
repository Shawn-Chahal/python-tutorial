# You can define a function to perform different tasks.
# The advantage of functions is that it is easy to reuse code, even across projects.
# It also makes it clear what a piece of code is doing.
# For example, this function can be used to model the Hill equation.
def hill_equation(concentration):
    r_max = 20 * 10 ** 6
    ec50 = 10
    n = -1.2

    response = r_max / (1 + (ec50 / concentration) ** n)

    return response


# If your write this code and come back to it years later, it will still be clear as to what it's doing.
for c in [10, 30, 50, 100]:
    r = hill_equation(c)
    print(f"{c:3d} mg/kg -> {r:10.0f} cell population")
