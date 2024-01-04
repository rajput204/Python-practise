def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(5))

def oddsum(n):
    if n==1:
        return 1
    else:
        return 2*n+1 +oddsum(n-1)
print(oddsum(5))


def evensum(n):
    if n==1:
        return 1
    else:
        return 2*n+evensum(n-1)
print(evensum(5))

def sumsquare(n):
    if n==1:
        return 1
    else:
        return n*n +sumsquare(n-1)
print(sumsquare(5))

def cubesum(n):
    if n==1:
        return 1
    else:
        return n*n*n+cubesum(n-1)
print(cubesum(2))




