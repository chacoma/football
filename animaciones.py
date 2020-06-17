import sys,os,json
sys.path.insert(1, 'libs/')
from plotter_lib import *


os.system("clear")
print ("# %s..........................................\n" % sys.argv[0])


arxs = [
'data/posiciones_2013-11-03_tromso_stromsgodset_first.json',
'data/posiciones_2013-11-03_tromso_stromsgodset_second.json',
'data/posiciones_2013-11-07_tromso_anji_first.json',
'data/posiciones_2013-11-07_tromso_anji_second.json',
'data/posiciones_2013-11-28_tromso_tottenham.json'
]


NoValidos = {
arxs[0]:['12','11','6', '3'],
arxs[1]:['12','11','1', '4'],
arxs[2]:['1','3'],
arxs[3]:['1','3','4','5','9','14','17'],
arxs[4]:['3','7','9','10','13'],
}


def data2animar(arx, noValido):
	
	
	pos = json.load(open(arx,'r'))
	
	pIds = [ x for x in pos.keys() if x not in noValido ]
	
	lmax=-1
	for pId in pIds:
		l = len(pos[pId]['t'])
		if l>lmax:
			T = pos[pId]['t']
			lmax = l
		
		pos[pId]['t'] = np.array(pos[pId]['t'])
		pos[pId]['x'] = np.array(pos[pId]['x'])
		pos[pId]['y'] = np.array(pos[pId]['y'])
	
	delta= 1
	
	X,J= [],[]
	
	for i in range(0, len(T)-delta):
		
		t0 = T[i]
		t1 = T[i+delta]
		
		x0,x1,jug = [],[],[]
		
		for pId in pIds:
			
			i0 = np.where( pos[pId]['t']==t0 )
			i1 = np.where( pos[pId]['t']==t1 )
			
			if len(i0[0])==1 and len(i1[0])==1:
				
				x00 = pos[pId]['x'][i0][0]
				x01 = pos[pId]['y'][i0][0]
								
				x10 = pos[pId]['x'][i1][0]
				x11 = pos[pId]['y'][i1][0]
				
				
				x0.append( [x00,x01] )
				x1.append( [x01,x11] )
				jug.append(pId)
			
		
		x0 = np.array(x0)
		x1 = np.array(x1)
		
		X.append(x0)
		J.append(jug)
			
	
	return X,J
			

def anim1():
	
	# ANIMACION COMUN
	
	arx = arxs[0]
	
	print (arx)
	
	xdata,jug = data2animar(arx, NoValidos[arx])
		
	plot = Plotter()
	
	plot.ax.set_xlim(-5,115)
	plot.ax.set_ylim(-2,70)
	
	p1, = plot.ax.plot([], [], marker='o', linewidth=0)
	p2, = plot.ax.plot([], [], marker='x', linewidth=0, c='C3')
	p3, = plot.ax.plot([], [], linewidth=1, c='C3')
	
	
	def init():
		p1.set_data([], [])
		p2.set_data([], [])
		p3.set_data([], [])
		
		return p1,p2,p3
	
	
	def animate(i):
		
		X = xdata[i]
		
		# pos jugadores
		x, y = X[:,0], X[:,1]
		
		# centro masa
		xcm, ycm = np.mean(x), np.mean(y)
		
		# elipse
		xr, yr = np.std(x), np.std(y)
		t = np.linspace(0, 2*np.pi, 100)
		xe = xr*np.cos(t)+xcm
		ye = yr*np.sin(t)+ycm
		
		#plots
		p1.set_data(x,y)
		p2.set_data(xcm,ycm)
		p3.set_data(xe,ye)
		
		return p1, p2, p3


	anim = FuncAnimation(plot.fig, animate, init_func=init,
								   frames=len(xdata), interval=100, blit=True)
	
	plot.show()
	

def anim2():
	
	# ANIMACION VISTO DESDE EL CENTRO DE MASA
	
	arx = arxs[0]
	
	xdata,jug = data2animar(arx, NoValidos[arx])
	
	
	plot = Plotter(W=5, H=5)
	
	plot.ax.set_xlim(-45,45)
	plot.ax.set_ylim(-45,45)
	
	p1, = plot.ax.plot([], [], marker='o', linewidth=0)
	p2, = plot.ax.plot([], [], marker='x', linewidth=0, c='C3')
	p3, = plot.ax.plot([], [], linewidth=1, c='C2')
	
	
	def init():
		p1.set_data([], [])
		p2.set_data([], [])
		p3.set_data([], [])
		
		return p1,p2,p3
	
	
	def animate(i):
		
		X = xdata[i]

		# centro masa
		xcm, ycm = np.mean(X[:,0]), np.mean(X[:,1])
		
		# pos jugadores
		x, y = X[:,0]-xcm, X[:,1]-ycm
		
		# elipse
		xr, yr = np.std(x), np.std(y)		
		t = np.linspace(0, 2*np.pi, 100)

		R = np.sqrt(xr**2 + yr**2)
		xe = R*np.cos(t)
		ye = R*np.sin(t)
		
		p1.set_data(x,y )
		p2.set_data(0,0)
		p3.set_data(xe,ye)
		
		return p1, p2, p3


	anim = FuncAnimation(plot.fig, animate, init_func=init,
								   frames=len(xdata), interval=100, blit=True)

	
	plot.show()
	
			
			



# main **********************	
#anim1()
anim2()

