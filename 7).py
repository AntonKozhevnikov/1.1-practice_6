def has_duplicates(s):
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
print(has_duplicates([1,2,3,56,7,3]))
