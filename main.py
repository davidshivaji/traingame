import sys
from itertools import permutations, product

def traingame(nums, res):
    """pass a 4 digit integer and a desired result integer.
    traingame will return possible solutions.
    """
    solutions = []
    ops = ["+", "-", "*", "/"]
    digits = [i for i in str(nums)]

    x = []
    arrangements = permutations(digits, 4) # == x
    for arr in arrangements:
        x.append(arr)

    # print(('6', '0', '5', '5') in x)

    y = []
    ops_prod = product(ops, repeat=3) #  == y
    for order in ops_prod:
        y.append(order)


    for i in x:
        # print(i)
        for j in y:
            alt = i[0] + j[0] + i[1] + j[1] + i[2] + j[2] + i[3]
            # print(alt)
            if '/0' in alt: # division by zero.
                pass
            else:
                result = eval(alt)
                if result == int(res):
                    solutions.append(alt)

    if solutions == []:
        print('impossible')
    else:
        # for sol in solutions:
            # print(sol, '=', res)
        print(solutions[0], "=", res)
        print(f'found {len(solutions)-1} other solutions resulting in {res}')

traingame(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 10)
