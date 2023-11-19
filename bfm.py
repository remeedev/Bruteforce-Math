# This doesn't have anything to do with passwords, it does not get you anything, it is just a fun idea I got

def bruteForce_math(problem, solution, approx = 5):
    # function that changes last decimal
    def change_dec(decimal, number):
        decimal = [i for i in decimal]
        decimal[-1] = str(number)
        decimal = "".join(decimal)
        return decimal
    # ones section of the number
    ones = 0
    # Decimal digits
    decimal = "0"
    curr_digit = 0
    decimal_active = False
    # function that returns the final value
    num = lambda  : charge*float(str(ones)+"."+decimal)
    # Check whether the charge is positive or negative
    charge = 1
    if abs(problem(1)-solution) > abs(problem(-1)-solution):
        charge = -1
    standard = problem(0) > solution
    solved = False
    while not solved and len(decimal) != (approx+1):
        if problem(num()) == solution:
            break
        if not decimal_active:
            ones += 1
            _ans = problem(num())
            if not standard:
                if _ans > solution:
                    decimal_active = True
                    ones-=1
            else:
                if _ans < solution:
                    decimal_active = True
                    ones-=1
        else:
            if curr_digit > 9:
                curr_digit = 0
                decimal += "0"
            _dec = decimal
            decimal = change_dec(decimal, curr_digit)
            curr_digit+=1
            _ans = problem(num())
            if not standard:
                if _ans > solution:
                    decimal = _dec
                    decimal += "0"
                    curr_digit = 0
            else:
                if _ans < solution:
                    decimal = _dec
                    decimal += "0"
                    curr_digit = 0
    return num()