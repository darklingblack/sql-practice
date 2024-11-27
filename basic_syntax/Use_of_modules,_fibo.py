cd 'C:\Users\barba\OneDrive - University College London\Bioinformatics\BIoPythonTraining\Programming for Biologists'

python

import fibo

fibo.fib(1000)
fibo.fib2(500)

fib = fibo.fib

fib2 = fibo.fib2

fib(500)
fib2(1000)

fibo.__name__

dir(fibo)

#########################################################
from fibo import fib, fib2
fib(500)

from fibo import *
fib(500)