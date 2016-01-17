class Person(object):
    name = ''

def person_cmp(x, y):
    if(x.name < y.name):
        return -1
    if(x.name > y.name):
        return 1
    return 0

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]

L2 = sorted(L1, person_cmp)

print L2[0].name
print L2[1].name
print L2[2].name