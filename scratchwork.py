result_set = [1,2,8,2]



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

print(max)
indexmax = result_set.index(max)
print(indexmax)
print(min)
indexmin = result_set.index(min)
print(indexmin)
 
del result_set[indexmax]
del result_set[indexmin]

new_set = result_set
print(new_set)

for x in new_set:
    total = 0
    counter = 0
    total = total + x
    counter = counter + 1
avg = total/counter

print(avg)