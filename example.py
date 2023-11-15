from bfm import bruteForce_math

problem = lambda a : 3*(a**2) + 5*a - 5
solution = 0

ans = bruteForce_math(problem=problem, solution=solution, approx=100)
print(ans)

problem = lambda a : a/27 # testing negative value answers
solution = -0.89

ans = bruteForce_math(problem=problem, solution=solution, approx=100)
print(ans)

problem = lambda a : 3*(a**3) + 2*(a**2) + 3*a-5 # Not even I know how to solve a problem like this
solution = 0

ans = bruteForce_math(problem=problem, solution=solution, approx=100)
print(ans)