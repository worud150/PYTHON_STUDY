import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')
        
        lbl_red.setStyleSheet(
            "color : red;"
            "border-style : solid;"
            "border-width : 2px;"
            "border-color : #fa8072;"
            "border-radius : 3px;"
        )
        lbl_green.setStyleSheet(
            "color : green;"
            "background-color : #87cefa;"   
        )
        lbl_blue.setStyleSheet(
            "color : blue;"
            "background-color : #7fffd4;"
            "border-style : dashed;"
            "border-width : 3px;"
            "border-color : #1e90ff;"
            "width : 10p"
        )
        
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_blue)
        vbox.addWidget(lbl_green)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 400, 200)
        self.show()
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
    
    