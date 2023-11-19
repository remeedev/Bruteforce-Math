# Checker code that verifies code working

from bfm import bruteForce_math

def test_problem(problem):
    _ans = bruteForce_math(problem[0], problem[1], approx=100)
    if abs(problem[0](_ans)-problem[1]) > 1:
        return f"{problem[0](_ans)} is not {problem[1]}"
    else:
        return "Test succesfull!"

# Generated problems with chatGPT

problem_list = [
    [lambda x: 2 * x - 5, 0, 2.5],        # 2 * x - 5 = 0, x = 2.5
    [lambda x: x**2 - 4, 0, 2],           # x^2 - 4 = 0, x = 2
    [lambda x: 3 * x + 7, 0, -7/3],       # 3 * x + 7 = 0, x = -7/3
    [lambda x: 4 * x + 3, 0, -0.75],      # 4 * x + 3 = 0, x = -0.75
    [lambda x: 0.5 * x**2 - 2, 0, 2],    # 0.5 * x^2 - 2 = 0, x = -4
    [lambda x: -x + 10, 0, 10],           # -x + 10 = 0, x = 10
    [lambda x: 2**x - 8, 0, 3],           # 2^x - 8 = 0, x = 3
    [lambda x: 5 * x - 2, 0, 0.4],        # 5 * x - 2 = 0, x = 0.4
    [lambda x: x**3 - 27, 0, 3],          # x^3 - 27 = 0, x = 3
    [lambda x: -2 * x**2 + 6 * x - 4, 0, 1],  # -2 * x^2 + 6 * x - 4 = 0, x = 1
    [lambda x: 6 * x + 2, 0, -1/3],       # 6 * x + 2 = 0, x = -1/3
    [lambda x: x**2 + 5 * x + 6, 0, -2], # x^2 + 5 * x + 6 = 0, x = -2
    [lambda x: 3 * x**3 - 27, 0, 3],      # 3 * x^3 - 27 = 0, x = 3 wrong
    [lambda x: 0.1 * x**2 - 2, 0, 14],   # 0.1 * x^2 - 2 = 0, x = -14
    [lambda x: -4 * x + 8, 0, 2],         # -4 * x + 8 = 0, x = 2
    [lambda x: 1.5 * x**2 - 6 * x + 5, 0, 1],  # 1.5 * x^2 - 6 * x + 5 = 0, x = 1
    [lambda x: 2**x - 16, 0, 4],          # 2^x - 16 = 0, x = 4
    [lambda x: 7 * x - 3, 0, 3/7],        # 7 * x - 3 = 0, x = 3/7
    [lambda x: x**2 - 10, 0, -10],        # x^2 - 10 = 0, x = -10
    [lambda x: -3 * x + 15, 0, 5],        # -3 * x + 15 = 0, x = 5
    [lambda x: 0.2 * x**2 - 4, 0, -10],   # 0.2 * x^2 - 4 = 0, x = -10
    [lambda x: 2 * x**2 + 3 * x - 5, 0, 1],  # 2 * x^2 + 3 * x - 5 = 0, x = 1
    [lambda x: 5 * x**2 - 50, 0, 4],      # 5 * x^2 - 50 = 0, x = 4
    [lambda x: -x**3 + 64, 0, 4],         # -x^3 + 64 = 0, x = 4
    [lambda x: 0.3 * x - 0.6, 0, 2],      # 0.3 * x - 0.6 = 0, x = 2
    [lambda x: x**2 + 3 * x + 2, 0, -1],  # x^2 + 3 * x + 2 = 0, x = -1
    [lambda x: -2 * x**2 + 10 * x - 12, 0, 3],  # -2 * x^2 + 10 * x - 12 = 0, x = 3
    [lambda x: 4 * x**2 - 16, 0, 2],      # 4 * x^2 - 16 = 0, x = 2
    [lambda x: -x**2 + 9, 0, -3],         # -x^2 + 9 = 0, x = -3
    [lambda x: 0.5 * x**2 - 5, 0, -5],    # 0.5 * x^2 - 5 = 0, x = -5
    [lambda x: 3 * x**2 - 27, 0, 3],      # 3 * x^2 - 27 = 0, x = 3
    [lambda x: x**3 - 64, 0, 4],          # x^3 - 64 = 0, x = 4
    [lambda x: -5 * x**2 + 75, 0, 3],     # -5 * x^2 + 75 = 0, x = 3
    [lambda x: 1.2 * x - 3, 0, 2.5],      # 1.2 * x - 3 = 0, x = 2.5
    [lambda x: -2 * x**3 + 16, 0, 2],     # -2 * x^3 + 16 = 0, x = 2
    [lambda x: 2 * x**3 - 18, 0, 3],      # 2 * x^3 - 18 = 0, x = 3
    [lambda x: 0.8 * x**2 - 8, 0, -4],    # 0.8 * x^2 - 8 = 0, x = -4
    [lambda x: -4 * x**2 + 32, 0, 4],     # -4 * x^2 + 32 = 0, x = 4
    [lambda x: 6 * x**2 - 54, 0, 3],      # 6 * x^2 - 54 = 0, x = 3
    [lambda x: -0.5 * x + 2.5, 0, 5],     # -0.5 * x + 2.5 = 0, x = 5
    [lambda x: x**3 - 8, 0, 2],           # x^3 - 8 = 0, x = 2
    [lambda x: -3 * x**2 + 15 * x - 18, 0, 3],  # -3 * x^2 + 15 * x - 18 = 0, x = 3
    [lambda x: 5 * x**3 - 125, 0, 5],     # 5 * x^3 - 125 = 0, x = 5
    [lambda x: 2 * x**2 - 10, 0, 5],      # 2 * x^2 - 10 = 0, x = 5
    [lambda x: -0.1 * x**2 + 2, 0, -20],  # -0.1 * x^2 + 2 = 0, x = -20
    [lambda x: 4 * x**3 - 64, 0, 4],      # 4 * x^3 - 64 = 0, x = 4
]

count = 1
for problem in problem_list:
    print(f"{count}| {test_problem(problem)}")
    count+=1
