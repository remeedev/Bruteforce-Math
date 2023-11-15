# This doesn't have anything to do with passwords, it does not get you anything, it is just a fun idea I got

problem = lambda a : a/22.6
solution = 0.8

def bruteForce_math(problem, solution, approx = 5):
    ones = 0
    decimals = "0"
    precision = -1
    currdigit=0
    charge = 1 if abs(problem(1)-solution) < abs(problem(-1)-solution) else -1
    solved = False
    while not solved:
        if len(decimals) == approx:
            return float(str(ones)+"."+decimals)
        _saveDec = decimals
        if not precision < 0:
            decimals = list(decimals)
            decimals[precision] = str(currdigit)
            decimals = "".join(decimals)
        else:
            ones+=1
        _temp = problem(charge*float(str(ones)+"."+decimals))
        if not precision < 0:
            if charge*_temp > charge*solution:
                decimals = _saveDec
                currdigit = 0
                decimals = decimals+"0"
                precision+=1
            elif charge*_temp < charge*solution:
                currdigit+=1
        else:
            if charge*_temp>charge*solution:
                ones-=1
                precision+=1
        solved = _temp == solution
    return charge*float(str(ones)+"."+decimals)