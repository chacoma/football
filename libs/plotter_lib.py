import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.animation import FuncAnimation

matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = 'CMU Serif, Times New Roman'
matplotlib.rc('text', usetex=True)



class Plotter:
	
	def __init__(self , W=4, H=3):
		
		self.font_axis = 13
		self.font_ticks= 12
		self.font_ticks_inset= 20
		self.font_axis_inset= 25
		
		self.leg_size= 12
		self.W=W
		self.H=H 
		
		self.fig, self.ax = plt.subplots(figsize=(self.W,self.H) )
		self.ax.tick_params(axis="x", labelsize=self.font_ticks)
		self.ax.tick_params(axis="y", labelsize=self.font_ticks)

		self.labx = ''
		self.laby = ''

	def label(self, where='', lab='' ):
		
		if where=='x':
			self.ax.set_xlabel(lab, fontsize=self.font_axis, fontname='CMU Serif')
			
			self.labx = lab
		
		if where=='y':
			self.ax.set_ylabel(lab, fontsize=self.font_axis, fontname='CMU Serif')
			
			self.laby = lab
	
	
	def show(self, save='', loc=1, dpi=300, inset=0, box=False):
		
		if inset:
			
			self.ax.tick_params(axis="x", labelsize=self.font_ticks_inset, direction="in", pad=1,width=2)
			self.ax.tick_params(axis="y", labelsize=self.font_ticks_inset, direction="in", pad=0.1,width=2)
			
			
			self.ax.set_xlabel(self.labx, fontsize=self.font_axis_inset, fontname='CMU Serif')
			self.ax.set_ylabel(self.laby, fontsize=self.font_axis_inset, fontname='CMU Serif')
			
			
		plt.legend(prop={'size': self.leg_size}, loc=loc, fancybox=box, 
			frameon=box, handlelength=self.leg_size*0.1)
		
		plt.tight_layout()
		
		if save!='':
			plt.savefig(save, dpi=dpi, transparent=True)
		
		plt.show()
	
	
	
	
	
	
	
	
	
	def save(self, save='x.svg', loc=1, dpi=300, inset=0, box=False):
		
		plt.legend(prop={'size': self.leg_size}, loc=loc, fancybox=box, 
			frameon=box, handlelength=self.leg_size*0.1)
		
		plt.tight_layout()
		plt.savefig(save, dpi=dpi, transparent=True)



	def logscale(self, eje='',p1=[1e-4, 1e4], p2= [1e4, 1e-4]):
		
		
		if eje=='':
			self.ax.set_xscale('log')
			self.ax.set_yscale('log')	
		
		if eje=='x':
			self.ax.set_xscale('log')
		
		if eje=='y':
			self.ax.set_yscale('log')
		
		
		x0 = p1[0]
		x1 = p2[0]
		
		y0 = p2[1]
		y1 = p1[1]
	
		self.ax.set_xlim(x0, x1)	
		self.ax.set_ylim(y0, y1)



