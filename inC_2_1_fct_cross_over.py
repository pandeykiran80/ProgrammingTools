# -*- coding: utf-8 -*-
#!python3.7
"""
    - find all cross-over points between
      two functions (f(t) and g(t))
    - !note that points will depend on increment
      delta_t and resolution eps!
"""
#======================================
#           modules
#======================================
import numpy as np
import matplotlib.pyplot as plt
#------------my fct--------------------
def fct_g( t, A, t0):
    return A*t + t0

def fct_f( t, c, t0):
    return c*( t-t0)**2

#======================================
#           parameter
#======================================
tmin, tmax = -10, 10
f_dt       = 1e-4
i_n        = int( (tmax-tmin)/f_dt) 
t0         = 2.5
c          = 1.1
A          = 5
eps        = .001 
#======================================
#           find cross-over points
#======================================
f_curr_t = tmin
for i in range( i_n):
    f_curr_g = fct_g( f_curr_t, A, t0)
    f_curr_f = fct_f( f_curr_t, c, t0)
    if abs( f_curr_g - f_curr_f) < eps: # Mistake
        print( 'cross-over point at t = %.4f, g(t) = %.3f, f(t)=%.3f'%( f_curr_t, f_curr_g, f_curr_f))
    
    f_curr_t += f_dt


#======================================
#           plot fct.
#======================================
a_t = np.linspace( tmin, tmax, i_n)
a_g = fct_g( a_t, A, t0)
a_f = fct_f( a_t, c, t0)

plt.figure( 1)
plt.clf()
plt.plot( a_t, a_g, 'ro', label = 'g(t)')
plt.plot( a_t, a_f, 'go', label = 'f(t)')
plt.legend()
plt.xlabel( 'Time')
plt.ylabel( 'Position')
plt.show()









