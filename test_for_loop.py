"""
home
"""
digits = [1, 3, 5, 8]

for i in digits:
    print(i)

# if is there nested json file for loop can be usable

print(f"The sum of digitd is: {sum(i for i in digits)}")

# EXAMPLE: how many quakes were felt by more than 500 people?
"""
print(sum(quake['properties']['felt'] is not None and
          quake['properties']['felt'] > 500 for quake in data['features']))
"""