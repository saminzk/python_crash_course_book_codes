dimensions = (200,50)

# print(dimensions[0])
# print(dimensions[1])

# elements of a tuple cannot be changed
# dimensions[0] = 250  # This will raise a TypeError
# print(dimensions)

for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)