"""
hello
"""
dic12 = {1: 2, 4: 67, -5: 9, -1: 7}

res1 = min(dic12)
print(res1) # smallest key

print(min(dic12, key= lambda x:dic12[x])) # prints key with the smallest value

key1 = min(dic12, key= lambda x:dic12[x])

print(dic12[key1]) # print the smallest value in the dictionary
