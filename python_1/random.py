# these are the 
def equations(vars):
    x, y = vars
    eq1 = x + y - 10  # Example equation 1
    eq2 = x*2 + y*2 - 25  # Example equation 2
    return [eq1, eq2]

# Initial guess
initial_guess = (1, 1)

solution = (equations, initial_guess)
print("Solution:", solution)
