# python-tips

How to ind the sum of squares of all the even numbers between 1 and 151 in one line:

1) Using list comprehension:
    sum( [x*x for x in range(1,151) if x % 2 == 0] )
    
2) Using filter,map and reduce:
    from functools import reduce
    x = reduce( lambda x,y : x+y  , map( lambda x : x *x , filter( lambda x : x % 2 == 0 , range(1,151))) )
    print(x)
    
    Notes: 
    Filter can take a lambda function and then a list
    Map can take a lambda functions and then lists
    Reduce will take a lambda function and 'reduces' the list values based on the anonymous function.
    
  
