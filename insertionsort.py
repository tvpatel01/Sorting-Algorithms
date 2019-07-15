# insertionsort program 

numbers = [3, 8, 0, 19, 1, -6, 5]
print(numbers)
print('⬇')

def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        position = numbers[index]
        i = index - 1
        while i>=0:
            if position < numbers[i]:
                numbers[i+1] = numbers[i]
                numbers[i] = position
                i = i - 1
            else:
                break

insertion_sort(numbers)
print(numbers) 