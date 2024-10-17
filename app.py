from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel


app = QApplication([])
window = QWidget()
window.setWindowTitle('Programming Languages')
window.resize(400, 300)

#Step 1. Create 6 labels with the names of programming languages
sentence1 = QLabel('PHP')
sentence2 = QLabel('JavaScript')
sentence3 = QLabel('Python')
sentence4 = QLabel('Pascal')
sentence5 = QLabel('SQL')
sentence6 = QLabel('C++')

lv1 = QVBoxLayout()
lv2 = QVBoxLayout()
hbck = QHBoxLayout()

lv1.addWidget(sentence1,alignment=Qt.AlignCenter)
lv1.addWidget(sentence3,alignment=Qt.AlignCenter)
lv1.addWidget(sentence5,alignment=Qt.AlignCenter)
lv2.addWidget(sentence2,alignment=Qt.AlignCenter)
lv2.addWidget(sentence4,alignment=Qt.AlignCenter)
lv2.addWidget(sentence6,alignment=Qt.AlignCenter)

hbck.addLayout(lv1)
hbck.addLayout(lv2)
window.setLayout(hbck)
window.show()
app.exec_()
