#python3.7
"""
    - this script creates a fct to compute:
    x = Sum( i*5)  for i=0 to n

"""
#=========================================================================
#                  imports and fct.
#=========================================================================

#---------------------my modules and fct.---------------------------------
def fct_my_sum( n):
    x = 0
    for i in range( n):
        x += 5*i
        print( x)
    return x

#=========================================================================
#                     parameters
#=========================================================================
n = 10


#=========================================================================
#                   compute sum
#=========================================================================
f_sum = fct_my_sum( n)
print( 'final value after %i iterations: '%( n), f_sum)