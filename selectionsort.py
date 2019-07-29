numbers = [2, 5, 1, 0, 9, 7, 3]

numbers[0] = -1


print (numbers)

min_index = 0
min = numbers[min_index]

for i in range (0, len(numbers)-1):
    for j in range (i, len(numbers)-1):
        # Find min and Index of it (5, 2, 7)
        # Flip min with starting index (i)
        print()

