# tremorsense program 
# goal = find variation between each number, then the average... 
# edit goal = to find the variation between SETS within a set

input = [3, 5, 2, 10, -2, 0, 6, -5, 12, 8, 1, -11]
print(input)
raw1 = input[0:len(input)//2]
raw2 = input[len(input)//2:len(input)]

set1 = raw1[0:len(raw1)//2]
set2 = raw1[len(raw1)//2:len(raw1)]
set3 = raw2[0:len(raw2)//2]
set4 = raw2[len(raw2)//2:len(raw2)]


def calculateVariation(input):
    total = 0
    counter = 0
    variation = [input[i + 1] - input[i] for i in range(len(input) - 1)]
    abs_val = [abs(k) for k in variation]
    for x in abs_val:
        total = total + x
        counter = counter + 1
    avg = total/counter
    return avg

overall_result = calculateVariation(input)
result1 = calculateVariation(set1)
result2 = calculateVariation(set2)
result3 = calculateVariation(set3)
result4 = calculateVariation(set4)
result_set = [result1, result2, result3, result4]

print(result_set)


max = result_set[0]
min = result_set[0]
for x in result_set:
    total = 0
    counter = 0
    total = total + x
    counter = counter + 1
    if(x > max):
        max = x
    if (x < min):
        min = x


indexmax = result_set.index(max)
indexmin = result_set.index(min)

 
del result_set[indexmax]
del result_set[indexmin]

new_set = result_set
print(new_set)

final_avg = sum(new_set) / len(new_set)
print(f"Avg of broken up set... {final_avg}")
print(f"Avg of orig set... {overall_result}")