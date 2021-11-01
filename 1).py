a = [[1, 2, 5], [1, 2, 3]]
def nested_sum(c):
    s = 0
    for l in range(len(c)):
            for q in range(len(c[l])):
                s += c[l][q]
    return(s)
print(nested_sum(a))
    
