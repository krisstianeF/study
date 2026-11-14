# Bisection method

```puthon
def square_root_bisection(number, tolerance = 1e-7, max_iterations = 1000):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 1 or number == 0:
        print(f'The square root of {number} is {number ** 0.5:.0f}')
        return number
    
    low = 0.0
    high = max(1.0, number)

    iteration = 0
    while iteration < max_iterations and (high - low) > tolerance:
        mid = (low + high) / 2.0
        if mid * mid < number:
            low = mid          # root is in the right half
        else:
            high = mid         # root is in the left half
        iteration += 1

    # Check convergence after the loop
    if (high - low) <= tolerance:
        root = (low + high) / 2.0
        print(f"The square root of {number} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {max_iterations} iterations")
        return None




square_root_bisection(0)
square_root_bisection(5)

square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(0.25, 1e-7, 50) 
```
