# python3.7
"""
- create a function that takes an integer number as input
  and returns all divisors from 2 to 9

- function - fct_checkIfInt takes any input put will
             only proceed with integer and raise error otherwise

"""
#=====================================================================
#                   modules
#=====================================================================
import numpy as np
#-------------------my fct.-------------------------------------------
def fct_find_divisor( int_no):
    int_no = fct_checkIfInt( int_no)
    a_test_div = np.arange( 2, 10, 1)
    l_true_div = []
    for curr_div in a_test_div:
        print( curr_div, int_no%curr_div)
        if int_no%curr_div == 0:
            l_true_div.append( curr_div)
    return l_true_div

def fct_checkIfInt( my_string):
    try:
        int( my_string)
        return int( my_string)
    except ValueError:
        error_str = "number is not an integer", my_string
        raise (ValueError(error_str))
#=====================================================================
#                   params
#=====================================================================
#user_no = '12'
# ask user for specific integer number
user_no = input( "Provide an Integer Number: ")
#=====================================================================
#                   computations
#=====================================================================
print( 'all divisors of %s (between 2 and 9) :'%(user_no),  fct_find_divisor(user_no))