import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        hbox = QHBoxLayout()
        
				# ------------------------------------------------------------- #
        top = QFrame()
        top.setFrameShape(QFrame.Box)
        
        midleft = QFrame()
        midleft.setFrameShape(QFrame.Box)
        
        midright = QFrame()
        midright.setFrameShape(QFrame.Box)
        
        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)
				# 각 영역에 들어갈 프레임 만들기
        # ------------------------------------------------------------- #

        spllitter1 = QSplitter(Qt.Horizontal)
        spllitter1.addWidget(midleft)
        spllitter1.addWidget(midright)
        
        spllitter2 = QSplitter(Qt.Vertical)
        spllitter2.addWidget(top)
        spllitter2.addWidget(spllitter1)
        spllitter2.addWidget(bottom)
        
        hbox.addWidget(spllitter2)
        self.setLayout(hbox)      
        
        self.setWindowTitle('QSplitter')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
        
    
    def button_clicked(self):
        self.slider.setValue(0)        
        self.dial.setValue(0)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wx = MyApp()
    sys.exit(app.exec_())