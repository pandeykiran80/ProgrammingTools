# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:59:39 2020

@author: Kiran Pandey
"""

# Program for computing the height of a ball in vertical motion

v0 = 5             # Initial velocity
g = 9.81           # Acceleration of gravity
t = 0.6            # Time

y = v0*t - 0.5*g*t**2        # Vertical position

print( y)
