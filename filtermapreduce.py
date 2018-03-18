#find the sum of squares of all the even numbers between 1 and 151 in one line

#using list comprehension
sum( [x*x for x in range(1,151) if x % 2 == 0] )

from functools import reduce
x = reduce( lambda x,y : x+y  , map( lambda x : x *x , filter( lambda x : x % 2 == 0 , range(1,151))) )
print(x)
