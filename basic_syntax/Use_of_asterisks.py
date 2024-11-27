def function(arg, *vargs, **kargs):
    print(arg)
    print(vargs)
    print(kargs)

function(1, 2, 3, 4, 5, test1="abc", test2="def")

################################################################################################

def function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

args = (1,2,3
        )
function(*args)

################################################################################################

def function(arg1=None, arg2=None):
     print(arg1, arg2)     

data = {"arg1":"1", "arg2":"2"}

function(**data)

################################################################################################

x = [1, 2, 3]
y = [4, 5, 6]
list(zip(x, y))

x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)

################################################################################################

#2. Unpacking with *
#The asterisk * is used for unpacking. When you use * with zip(x, y), it unpacks the list of tuples:

zip(*zip(x, y))
#This effectively transforms [(1, 4), (2, 5), (3, 6)] into the original two lists, but transposed:

zip((1, 4), (2, 5), (3, 6))
#The second zip re-zips these tuples into two separate tuples:

zip((1, 4), (2, 5), (3, 6))
#This produces two tuples, one for each original list:

((1, 2, 3), (4, 5, 6))