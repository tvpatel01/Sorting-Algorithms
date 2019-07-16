# tremorsense program 
# goal = find variation between each number, then the average

raw_data = [2, 5, 2, 10, -2]
total = 0
counter = 0

print(f"Raw Data:        {raw_data}")
print('⬇')

variation = [raw_data[i + 1] - raw_data[i] for i in range(len(raw_data) - 1)]
print(f"Variation:       {variation}")
print('⬇')


abs_val = [abs(k) for k in variation]

print(f"Abs. Value:       {abs_val}")
print('⬇')


for x in abs_val:
    total = total + x
    counter = counter + 1

avg = total/counter

print(f"Average (Index):  {avg}")