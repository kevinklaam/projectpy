from PyQt5 import QtWidgets as Qt

import sys

app = Qt.QApplication(sys.argv)

window = Qt.QWidget()
layout = Qt.QVBoxLayout()

layout.addWidget(Qt.QCheckBox("Middle"))
window.setLayout(layout)

window.show()
