counter = 0
passwdlst = []
l = 0

passwdlst = open('source.txt').read().split('\n')

def chkpwd(w,x,y,z):
    v = w.count(x)
    if v in range(y,z):
        return 'yes'
    else:
        return 'no'

for line in passwdlst:
    a = line.split(': ')[1]
    b = line.split(' ')[1].split(':')[0]
    c = int(line.split('-')[0])
    d = int(line.split('-')[1].split(' ')[0])+1
    if chkpwd(a, b, c, d) == 'yes':
        counter = counter + 1
    else:
        counter = counter

print(counter)