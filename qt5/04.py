import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      QToolTip.setFont(QFont('SansSerif', 10))
      self.setToolTip('This is a <b>QWidget</b> widget')
      
      btn = QPushButton('Button', self)
      btn.setToolTip('This is a <b>QWidget</b> widget')
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      ㅊ

      self.setWindowTitle('Tooltips')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())