import numpy as np

'''
Biblioteca de funciones para cálculo de albedo
'''

#Calcula hora solar
def get_st_local(n, lon_local, hora, zona_h):
    B=(n-1)*360/365
    B=np.radians(B)
    E=229.2*(0.000075+0.001868*np.cos(B)-0.032077*np.sin(B)-0.014615*np.cos(2*B)-0.04089*np.sin(2*B))
    #local standard meridian
    LSTM=15*(zona_h)#+180
    ts=hora+(4*(lon_local-LSTM)+E)/60
    return(ts)

#calcula cos(θ)
def get_cosT(n, lat_local, st_local):
    B=(n-1)*360/365
    B=np.radians(B)
    w=15*(st_local-12)
    #print('w:',w)
    w=np.radians(w)
    #declination Cooper
    #d=23.45*np.sin(np.radians((360/365)*(284+n)))
    #declination spencer
    d=0.006918-0.399912*np.cos(B)+0.070257*np.sin(B)\
            -0.006758*np.cos(2*B)+0.000907*np.sin(2*B)\
            -0.002697*np.cos(3*B)+0.00148*np.sin(3*B)
    phi=np.radians(lat_local)
    #u=cos(θ)
    u=np.cos(phi)*np.cos(d)*np.cos(w)+np.sin(phi)*np.sin(d)
    #print(np.degrees(np.arccos(u)))
    return(u)

#calcula albedo usando Taylor
def taylor(u):
     A=0.037/(1.1*(u**1.4)+0.15)
     return A

#calcula albedo usando briegleb
def briegleb(u):
    A=0.026/((u**1.7)+0.065)
    A+=0.15*(u-0.1)*(u-0.5)*(u-1)
    return A
