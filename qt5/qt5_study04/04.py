import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow) : 
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile = QAction(QIcon('./qt5/img/edit.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openFile)
        
        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
				# 파일 선택하기
        
        if fname[0] :
            f = open(fname[0], 'r')
            
            with f :
                data = f.read()
                self.textEdit.setText(data) #편집 위젯
            
            
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())