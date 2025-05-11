import math

# math.gcd()
def gcd(num1, num2):
    if num1 < 0:
        num1 = abs(num1)
    if num2 < 0:
        num2 = abs(num2)
    mx = max(num1, num2)
    mn = min(num1, num2)
    if mn == 0:
        return mx
    return gcd(mn, mx%mn)

def gcdHistory(num1, num2, l=[]):
    if num1 < 0:
        num1 = abs(num1)
    if num2 < 0:
        num2 = abs(num2)
    mx = max(num1, num2)
    mn = min(num1, num2)
    l.append([mx, mn])
    if mn == 0:
        return l
    return gcdHistory(mn, mx%mn, l)

# solves for u,v in A*u + B*v = gcd(A,B)
# INEFFICIENT
# RETURNS u, v
def extendedGCD(A, B):
    # Divide both sides by gcd(A,B)
    history = gcdHistory(A,B)
    quotients = []
    for i in range(len(history)-1):
        # history[i][0] = history[i+1][0] * Q + history[i+1][1]
        quotients.append((history[i][0] - history[i+1][1]) // history[i+1][0])

    # establish two row array
    arr = []
    arr_size = len(quotients)+2
    arr.append([0]*arr_size)
    arr.append([0]*arr_size)
    arr[0][1] = 1
    arr[1][0] = 1    

    # start filling values
    for i in range(2, len(arr[0])):
        arr[0][i] = quotients[i-2]*arr[0][i-1] + arr[0][i-2]
        arr[1][i] = quotients[i-2]*arr[1][i-1] + arr[1][i-2]

    return [arr[1][-2], -arr[0][-2]]

print(extendedGCD(17, 46))