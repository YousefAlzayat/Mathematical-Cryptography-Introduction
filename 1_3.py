from math import gcd

def isCongruentModuloM(a,b,m):
    return ((a-b)%m == 0)

def unitGroupModuloM(m):
    units = []
    for i in range(m):
        if gcd(i, m) == 1:
            units.append(i)
    
    units = ['.']+units
    dim = len(units)
    units = [units]
    
    for i in range(dim-1):
        units.append(units[0].copy())

    for i in range(1,dim):
        units[i][0] = units[0][i]

    return multiplication_table(units, m)

def multiplication_table(table, m):
    for i in range(1, len(table)):
        for j in range(1, len(table)):
            table[i][j] = (table[i][0] * table[0][j]) % m
    return table

def fast_power(a,b,m):
    powers_needed = bin(b)
    powers_needed = powers_needed[2:]
    powers_needed = powers_needed[::-1]

    table = [a]

    for i in range(1, len(powers_needed)):
        table.append((table[i-1] * table[i-1]) % m)
    
    result = 1
    for i in range(len(powers_needed)):
        if powers_needed[i] == '1':
            result *= table[i]
            result = result % m
    
    return result


# print(fast_power(3,218,1000))
# print(isCongruentModuloM(6,9,3))
# x = unitGroupModuloM(7)
# for i in x:
#     print(i)
# print()


