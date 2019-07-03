# bubblesort program 

numbers = [2, 5, 1, 9, 0, -15, 3, 11, 4, 90, 11, 7, 12, 962, 43, 20]

def bubble_sort(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1):
            if numbers[j] > numbers[j+1]:
                Q = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = Q

bubble_sort(numbers)
print(numbers)