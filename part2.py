nums = []

with open('nums.txt') as text:
    nums = text.read()
    numslst = nums.split('\n')

for item1 in numslst:
    for item2 in numslst:
        for item3 in numslst:
            if int(item1) + int(item2) + int(item3) == 2020:
                print(int(item1)*int(item2)*int(item3))