#Refer to http://blog.rcnelson.com/building-a-matplotlib-gui-with-qt-designer-part-2/l
from PyQt4.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

	
Ui_MainWindow, QMainWindow = loadUiType('window_v0.ui')

class Main(QMainWindow, Ui_MainWindow):
	def __init__(self, ):
		super(Main, self).__init__()
		self.setupUi(self)
		
	def addmpl(self, fig):
		self.canvas = FigureCanvas(fig)
		self.mplvl.addWidget(self.canvas)
		self.canvas.draw()

		# add navigation toolbar
		self.toolbar = NavigationToolbar(self.canvas, 
				self.mplwindow, coordinates=True)
		self.mplvl.addWidget(self.toolbar)
 
if __name__ == '__main__':
	import sys
	from PyQt4 import QtGui
	import numpy as np
 
	fig1 = Figure()
	ax1f1 = fig1.add_subplot(111)
	ax1f1.plot(np.random.rand(5))
 
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.addmpl(fig1)
	main.show()
	sys.exit(app.exec_())