import numpy as np
import sys,os,glob,json
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


def explore_jugador():

	arx = arxs[4]
	
	pos = json.load(open(arx,'r'))
	
	pId_ref = '3'
	t0 = pos[pId_ref]['t'][0]
	
	
	for pId in pos.keys():
		
		t, x, y = pos[pId]['t'], pos[pId]['x'], pos[pId]['y']
		
		print ("\npId :", pId, len(x))
		print ("Tiempo en cancha :", (t[0] - t0)/60., (t[-1] - t0)/60)
		print ("cerrar ventana para ver siguiente jugador ...")
		
		#print (x)
		
		plot = Plotter()
		
		plot.ax.scatter(x,y, s=0.2, c='C2' )
		
		
		plot.ax.set_xlim(-2,107)
		plot.ax.set_ylim(-2,70)
		plot.show()








#*****************************************************
explore_jugador()

