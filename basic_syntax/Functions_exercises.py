def meaningOfLife(x):
    return 42 * x

type(meaningOfLife)

f = meaningOfLife

print(f(2))

#This calls the function f with the argument 2.
#Since f is a reference to meaningOfLife, this is equivalent to calling meaningOfLife(2).
#The function meaningOfLife takes 2 as its argument (x) and calculates 42 * 2.
#The result of 42 * 2 is 84.


def myApply(fun, x):
    return fun(x)

myApply(meaningOfLife, 3)

apply(meaningOfLife, [3])

#####################################################################################

data = [67.2, 42.3, 33.1, 59.0, 41.3, 38.3, 44.3, 50.4, 53.5, 43.5]
print(data)

def simpleFilter(data) :
    res = []
    for d in data :
        if d >= 40 and d <= 60 :
            res.append(d)
    return res

filtered1 = simpleFilter(data)
print(len(filtered1), filtered1[:10])

#NEW EXERCISE
#if we want to change the range we filter out, we have to write a new filter function to do it

def myFilter(p, data):
    res = []
    for d in data:
        if p(d):
            res.append(d)
    return res

#Two things to note: First, we calling the test p for "predicate." Second, our filtering function is called
#myFilter because Python has a built-in function called filter that does more or less the same thing.

def inRange(d) :
    return True if d >= 40 and d <= 60 else False

filtered2 = myFilter(inRange, data)

print(len(filtered2), filtered2[:10])

def isEven(d):
    return True if (int(d) % 2 == 0) else False

onlyEven = myFilter(isEven, data)

print(len(onlyEven), onlyEven[:10])

#####################################################################################

def createRangeP(minimum, maximum):
    def p(d):
        return True if d >= float(minimum) and d <= maximum else False
    return p

p1 = createRangeP(45, 55)
p2 = createRangeP(45, 60)
print(p1(40))
print(p1(50))
print(p1(60))
print
print(p2(40))
print(p2(50))
print(p2(60))

#####################################################################################

#LAMBDAS

filtered4 = myFilter(lambda x: True if x >= 20 and x <= 80 else False, data)

print(len(filtered4), filtered4[:10])

#####################################################################################

def myMap(f, inp):
    res = []
    for i in inp:
        res.append(f(i))
    return res

def myReduce(f, inp, init = None):
    if (init == None):
        res = inp[0]
    else:
        res = f(init, inp[0])
    for i in range(1, len(inp)):
        res = f(res, inp[i])
    return res

total = myReduce(lambda x, y: x + y, data) #for each x and y, sum x and y
count = myReduce(lambda x, y: x + 1, data, 0)
avg = total/count
print(total, count, avg)

import numpy as np

sqerr = myMap(lambda x: (x - avg) ** 2, data)
var = myReduce(lambda x, y: y + x, sqerr) / count
print(var)
print(avg, np.mean(data))
print(var, np.var(data))