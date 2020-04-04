#!python3.7
#Kiran Pandey
#HW6_Heat
# refered from ground_temp.py and class lecture

from numpy import linspace, zeros, linspace, exp, sin, cos, pi, sqrt
import time
import sys
import matplotlib.cm as cm
#from matplotlib.mlab import griddata
import scipy.interpolate
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib as mpl
mpl.use( 'Qt5Agg')
import numpy as np
import matplotlib.pyplot as plt

def U_ana(t):
    """ True temperature """
    return U_bar + U_delta*exp(-a_x*sqrt(omega/(2*Alpha)))*cos((-a_x*sqrt(omega/(2*Alpha)))+(omega*t))

def U_top(t):
    return U_bar + U_delta*cos(t*omega)

def dU_topdt(t):
    return -U_delta*t*sin(t*omega)

#=====================================================================
#                   parameters
#=====================================================================
Alpha = 1E-5
U_bar = 0 # as we are only worried about temperature fluctuation
U_delta = 100
P = 24*3600	# period, 24 hours
omega = 2*pi/P
L = 4		# depth vertically down in the ground
N = 50
t_max    = 4*24*3600 #10 days, in seconds
dt      = 50 # time step in
gamma   = 0
f_Uout  = -50
#-------spatial discretization--------
i_Nx      = 50 # number of nodes in x
f_dx      = L/(i_Nx-1) # node spacing

#------plotting----------------
plot_step = 50 #plot every nth step

#=========================1===========================================
#              space/time discretization and IC
#=====================================================================
a_x    = np.linspace( 0, L, i_Nx)
a_t    = np.arange( 0, t_max+dt, dt)
i_Nt   = len( a_t) #int( round( f_tmax/f_dt))+1 # n nodes in t
print('space', i_Nx, len( a_x), a_x[1]-a_x[0],    f_dx)
print('time',  i_Nt, len( a_t), a_t[1]-a_t[0], dt)

aU     = np.ones(i_Nx)*U_bar
print( 'number of time steps', i_Nt, 'tmax in days: ', t_max/(24*3600))
# time it takes for an anomaly to diffuse across the grid
print( 'delta t: ', dt, 'in [s],   stability lim for delta t: ', f_dx**2/(2*Alpha))


#=====================================================================
#                     solve 1d-heat
#=====================================================================
# initialize time derivative vector
a_dUdt   = np.zeros( len( a_x))
m_U = np.zeros([len(a_t),2])
aU_final = np.zeros( len( a_t))
#plt.figure(1)
fig, ax1 = plt.subplots( )
for n in range( len(a_t)):# loop over time increments
    # set boundary conditions
    aU[0] = U_top(a_t[n])
    aU[-1]= f_Uout  
    
    a_dUdt[1:-1]=aU[2::]-2*aU[1:-1]+aU[0:-2]

    a_dUdt[0]=dU_topdt(a_t[n])
    a_dUdt[-1]=(2*Alpha/f_dx**2)*((aU[-2]+gamma*f_dx-aU[-1]))
    # forward Euler Formula to get u(x,t)
    aU_new  = aU + Alpha*dt/f_dx**2 * a_dUdt
    # update temp. profile for next iteration
    aU      = aU_new
    m_U[n,0] = n  # Nt time step
    m_U[n,1] = aU[1]  # Nx values
    aU_ana = U_ana(a_t[n])
    
    #====================================================================
    #               plot temp. u(x) for every nth time step
    # plotting temperature profile of numerical solution & analytical solution
    #=====================================================================
    print( 'time step: ', round( a_t[n]/3600,3), 'h')#,(n+1)/plot_step,(n+1)%plot_step
    if (n+1)%plot_step == 0:
        ax1.cla()
        ax1.set_title( 'Time Step: %.2f [h]'%( a_t[n]/3600))
    
        ax1.plot( a_x, aU,  'ko', ms = 4, mew = 1, mfc = 'none', label = 'Numerical, u(x,t)')
        
        # plot analytical solution
        ax1.plot( a_x, aU_ana, 'r-',label = 'analytical')
        #-----------------limits and labels-------------------------------------
        ax1.set_xlabel( 'Distance [m]')
        ax1.set_ylabel( 'Temperature [degree C]')
        ax1.legend( loc = 'upper right')
        ax1.set_xlim( -.1*L, 1.1*L)
        ax1.set_ylim(-100,100)
        ax1.grid(True)
        plt.pause( 0.01)

plt.show()
#=======================color map=============================
# x = m_U[n,0]
# y = m_U[n,1]
# xi = np.linspace(min(m_U[n,0]), max(m_U[n,0]))
# yi = np.linspace(min(m_U[n,1]), max(m_U[n,1]))
# zi = scipy.interpolate.griddata((x,y),temp,(xi,yi),method="linear")

# matplotlib.rcParams['xtick.direction'] = 'out'
# matplotlib.rcParams['ytick.direction'] = 'out'
# plt.imshow(zi, vmin=temp.min(), vmax=temp.max(), origin="lower", 
#             extent=[x.min(), x.max(), y.min(), y.max()])
# plt.colorbar()
# plt.show()

