
def pigeonhole_sort(numbers): 
    minimum = min(numbers)
    maximum = max(numbers)

    holes_num = maximum - minimum + 1

    holes = [0] * holes_num

    for x in numbers:
        holes[x - minimum] += 1

    sortedNumbers = [0]

    for y in range(holes_num): 
        while holes[y] > 0: 
            holes[y] -= 1
            sortedNumbers.append(y + minimum)
    return sortedNumbers



numbers = [1, 21, 3, -4, 5, 6, 7, 8, 96, 10]

print(f" Sorted list =  {pigeonhole_sort(numbers)}")
