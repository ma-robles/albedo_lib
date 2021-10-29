import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import sys
#import albedo_lib
import albedo_lib as alb
sys.path.append('./')

#Dia juliano
n=47
#hora local
hl=-6
#longitud CDMX
lon_local=99.145556
lat_local=19.419444

#generación de malla
lat_local=np.arange(0, 60, 0.5)
lon_local=np.arange(-180,180,)
lat_local, lon_local=np.meshgrid(lat_local,lon_local)

#formato de gráficas
#cmap = mpl.cm.tab20
cmap = mpl.cm.viridis
ticks = [0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09, 0.1, 0.2,0.3]
bounds= list(np.arange(0.02,0.11,0.01))
bounds.append(0.2)
bounds.append(0.3)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='both')
px = 1/plt.rcParams['figure.dpi']
fig, (ax1,ax2) = plt.subplots(2, sharex=False,
        constrained_layout=True,
        figsize=(1280*px, 720*px)
        )
cbar=fig.colorbar(mpl.cm.ScalarMappable(norm, cmap=cmap),
        ticks=ticks,
        ax=[ax1,ax2],
        orientation='vertical',
        aspect=50,
        )
cbar.ax.tick_params(labelsize=8)
for h in np.arange(8,19,1):
    st=alb.get_st_local(n, lon_local, h, hl)
    u=alb.get_cosT(n, lat_local, st)
    #Taylor
    A1=alb.taylor(u)
    #briegleb
    A2=alb.briegleb(u)
    #graficación
    ax1.cla()
    ax2.cla()
    ax1.set_title('Taylor')
    CS1=ax1.contourf(lon_local, lat_local, A1,
            cmap=cmap,
            levels=bounds,
            norm=norm,
            )
    ax1.clabel(CS1, colors='k', fontsize=6)
    ax1.contour(lon_local, lat_local, A1,
            cmap=cmap,
            levels=bounds,
            norm=norm,
            )
    ax2.set_title('Briegleb')
    CS2=ax2.contour(lon_local, lat_local, A2,
            cmap=cmap,
            levels=bounds,
            norm=norm,
            )
    ax2.clabel(CS2, colors='k', fontsize=6)
    ax2.contourf(lon_local, lat_local, A2, 
            cmap=cmap,
            levels=bounds,
            norm=norm,
            )
    fig.suptitle('Albedo día:{:d}, {:02d}:00 hrs GTM{}'.format(n, int(h), hl))
    #plt.savefig('albedo_{:02}_{:02}.png'.format(n,h))
    plt.pause(0.5)
plt.show()
