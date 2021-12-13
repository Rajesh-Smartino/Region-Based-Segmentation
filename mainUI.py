import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import backend


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class userinterface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.layout = QVBoxLayout(self)

        self.buttonLayout = QHBoxLayout(self)

        lbl1 = QLabel('Switch the tabs for gray scale image or color image and the Select the appropriate image', self)
        lbl1.setAlignment(Qt.AlignCenter)

        btn1 = QPushButton('Select an Image', self)
        self.clrbtn = QPushButton("Clear tabs", self)
        self.save = QPushButton('Save Image', self)

        #btn2 = QPushButton('Select a good Image', self)

        self.layout.addWidget(lbl1)
        self.buttonLayout.addWidget(btn1)
        self.buttonLayout.addWidget(self.save)
        self.buttonLayout.addWidget(self.clrbtn)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Gray Scale Images")
        self.tabs.addTab(self.tab2, "Color Images")
        self.tabs.addTab(self.tab3, "Quality & Efficiency")

        # first tab
        self.tab1.layout = QVBoxLayout(self)

        self.openimageG = QPushButton('Select an Image', self)

        self.tab1.btnlayout1 = QHBoxLayout(self)
        self.tab1.btnlayout1.addWidget(self.openimageG)

        self.tab1.imglayout1 = QHBoxLayout(self)

        self.tab1.layout.addLayout(self.tab1.btnlayout1)
        self.tab1.layout.addLayout(self.tab1.imglayout1)
        self.tab1.setLayout(self.tab1.layout)

        # second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.layout)

        # Third tab
        self.tab3.layout = QVBoxLayout(self)
        self.tab3.setLayout(self.tab3.layout)



        self.layout.addLayout(self.buttonLayout)
        self.layout.addWidget(self.tabs)

        self.setLayout(self.layout)

        self.setGeometry(600, 600, 1024, 720)
        self.setWindowTitle('Image Segmentation by Region Growing')

        self.openimageG.clicked.connect(self.ginputfn)
        self.show()

    def ginputfn(self):
        self.path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                                'All Files (*.*)')
        if self.path != ('', ''):
            print("File path : " + self.path[0])

        try:
            image = backend.loadgrayimage(self.path[0])
            sc = MplCanvas(self, width=5, height=4, dpi=100)
            sc.axes.imshow(image, cmap='gray')
            self.tab1.imglayout1.addWidget(sc)
            seed_point = sc.ginput(1)
            print(seed_point)

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error Loading an Image!!!")
            msg.setText("OOPS! \nAN ERROR OCCURED WHILE LOADING AN IMAGE\nPlease select an Image to proceed! (.jpg/.jpeg/.png)")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()




def main():
    app = QApplication(sys.argv)
    ex = userinterface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
