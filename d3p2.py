import time

trees = 0
run = 0
rise = 0

slope = open('slope.txt').read().split('\n')

def sloper(w,x,y,z):
    run = x - 2*x
    trees = 0
    rise = w
    
    for l in slope[::y]:
        if len(l) - run > x:
            run += x
        else:
            run = len(l) - run
            run = x - run
        if l[run] == '#':
            trees += 1
        rise += 1
    return trees

first = sloper(0,1,1,0)
second = sloper(0,3,1,0)
third = sloper(0,5,1,0)
fourth = sloper(0,7,1,0)
fifth = sloper(0,1,2,0.15)

print(first*second*third*fourth*fifth)