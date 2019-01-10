import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel
from PyQt5.QtWidgets import QPushButton, QLineEdit, QFormLayout
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
        self.label = QLabel("123")
        self.btn = QRadioButton()
        
        self.b1 = QRadioButton("Button1")
        self.b2 = QRadioButton("Button2")
        
        self.b1.setChecked(False)
        self.b2.toggled.connect(self.b1.setChecked)
        self.b2.toggled.connect(lambda checked: not checked and self.b1.setChecked(False))
		
        self.b2 = QRadioButton("Button2")

        button = QPushButton('Go', self)
        button.setToolTip('Open stock chart of ticker')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        layout.addWidget(self.le)
        layout.addWidget(self.label)
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
                                
        self.setLayout(layout)
        self.show()
         
    def on_click(self):
        print('PyQt5 button click')
        shost = self.le.text()
        print (shost)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

