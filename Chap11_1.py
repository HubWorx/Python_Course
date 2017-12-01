name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_47815.txt"
handle = open(name)

import re
count = 0
for line in handle:
    number = re.findall('[0-9]+', line)
    #Need to convert the list to integers
    print(number)
    for num in range(len(number)):
        number[num] = int(number[num])
    count = count + sum(number)
    print(count)
