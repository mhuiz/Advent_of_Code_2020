trees = 0
run = -3
counter = 0
iters = 0

slope = open('slope.txt').read().split('\n')

for l in slope:
    if len(l) - run > 3:
        run += 3
    else:
        run = len(l) - run
        run = 3 - run
    if l[run] == '#':
        trees += 1
        
print('You hit %s trees. '%(trees),'Ouch!')