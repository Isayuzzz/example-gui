import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
import numpy as np

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class UserInterface(QtWidgets.QMainWindow):
    """User Interface to plot a sin function 

        ARg: Q main window

        Return: User interface of a sin function with spinboxes to vary min, max, number of steps

    """    

    def __init__(self):
        super().__init__()
        # ------------------     widget spinboxes for min, max and numpoints
        self.widget_spin_box_min = QtWidgets.QSpinBox()
        self.widget_spin_box_min.setRange(0,90)
        self.widget_spin_box_min.setSingleStep(2)
        self.widget_spin_box_min.valueChanged.connect(self.plotter)

        self.widget_spin_box_max = QtWidgets.QSpinBox()
        self.widget_spin_box_max.setRange(0,90)
        self.widget_spin_box_max.setSingleStep(2)
        self.widget_spin_box_max.valueChanged.connect(self.plotter)

        self.numpoints = QtWidgets.QSpinBox()
        self.numpoints.setRange(10,200)
        self.numpoints.setSingleStep(2)
        self.numpoints.valueChanged.connect(self.plotter)        

        # ------------------

        # initiate the plot
        self.plot_widget = pg.PlotWidget()

        # title
        self.setWindowTitle("My sine function")
        # start central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # create vbox
        vbox = QtWidgets.QVBoxLayout(central_widget)
        vbox.addWidget(self.plot_widget)

        # create H box for the windget spinners and add it to layout
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.widget_spin_box_min)
        hbox.addWidget(self.widget_spin_box_max)
        hbox.addWidget(self.numpoints)

        vbox.addLayout(hbox)



    @Slot()
    def plotter(self):
        """plot sin function

            arg: self 
        Returns:
            plot 
        """        
        self.plot_widget.clear() 
        x = np.linspace(self.widget_spin_box_min.value(), self.widget_spin_box_max.value(), self.numpoints.value())
        self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "k", "width": 5})
        self.plot_widget.setLabel("left", "sin(x)")
        self.plot_widget.setLabel("bottom", "x ")
        return self.plot_widget




def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()

print("gelukt")