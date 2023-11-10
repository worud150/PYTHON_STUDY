import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(okButton)
        hBox.addWidget(cancelButton)
        hBox.addStretch(1)
        
        vBox = QVBoxLayout()
        vBox.addStretch(3)
        vBox.addLayout(hBox)
        vBox.addStretch(1)
        
        self.setLayout(vBox)
        
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wx = MyApp()
    sys.exit(app.exec_())
        