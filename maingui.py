import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel
from PyQt5.QtWidgets import QPushButton, QLineEdit, QFormLayout
from datapull import candlestick, chart
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Stock Charting Daily'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()
     
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        layout = QFormLayout()
        self.le = QLineEdit()
        label = QLabel("Kevin Lam", self)
        label.move(330,170)
        self.space = QLabel("Ticker")
        self.btn = QRadioButton()
        
        self.b1 = QRadioButton("Line")
        self.b2 = QRadioButton("Candlestick")
        
        self.b1.setChecked(False)
        self.b2.toggled.connect(self.b1.setChecked)
        self.b2.toggled.connect(lambda checked: not checked and self.b1.setChecked(False))
		
        self.b2 = QRadioButton("Candlestick")

        button = QPushButton('Go', self)
        button.setToolTip('Open stock chart of ticker')
        button.move(260,140)
        button.clicked.connect(self.on_click)

        
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        layout.addWidget(self.space)
        layout.addWidget(self.le)

        
                                
        self.setLayout(layout)
        self.show()
         
    def on_click(self):
        print('PyQt5 button click')
        
        shost = self.le.text()
        print (shost)
        candlestick(shost)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

