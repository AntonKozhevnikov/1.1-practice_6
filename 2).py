a = [1, 2, 3]
def cumsum(t):
    s = 0
    b = []
    for i in range(len(t)):
        s += t[i]
        b.append(s)
    return(b)
print(cumsum(a))
