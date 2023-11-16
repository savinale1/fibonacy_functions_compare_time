# test v2 define code effectiveness on execution time

from fibonacy_recursion_nov_14_23 import fibonacy_recursion
from fibonacy_straight_nov_14_23 import fibonacy_straight
import time

start = time.time()
fibonacy_straight()
end = time.time()
total_fib_strt = end - start

start = time.time()
fibonacy_recursion()
end = time.time()
total_fib_recur = end - start

if total_fib_strt > total_fib_recur:
    print(f"1. Total recur {total_fib_recur} better strt {total_fib_strt}.")
elif total_fib_recur > total_fib_strt:
    print(f"2. Total strt {total_fib_strt} better recur {total_fib_recur}.")
else:
    print("Equal")
