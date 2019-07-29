# bubblesort program 

numbers = [2, 5, 1, 19, 0, -82]
print(numbers)
print('⬇')

def bubble_sort(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                q = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = q

bubble_sort(numbers)
print(numbers)
