from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QRadioButton,
                            QLabel, QButtonGroup, QGroupBox, QPushButton, QSpinBox)
app= QApplication([])
main_win=QWidget()
main_win.setWindowTitle("Казино")
main_win.resize(400,400)
qtext=QLabel()
v_line=QVBoxLayout()

rbtn_1=QRadioButton('1991')
rbtn_2=QRadioButton('1989')
rbtn_3=QRadioButton('1998')
rbtn_4=QRadioButton('1992')

RadioGroupBox = QGroupBox('Baрiaнти відповідей')
RadioGroup=QButtonGroup()
RadioGroup.addButton (rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton (rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1=QHBoxLayout()
Layout_ans2=QVBoxLayout()
Layout_ans3=QVBoxLayout()

Layout_ans2.addWidget(rbtn_1)
Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3)
Layout_ans3.addWidget(rbtn_4)


btn_Menu=QPushButton("Меню")
btn_Sleep=QPushButton("Відпочити")
box_Minutes=QSpinBox()
box_Minutes.setValue(30)
btn_Ok=QPushButton("Відповісти")

Layout_line1=QHBoxLayout()
Layout_line2=QHBoxLayout()
Layout_line3=QHBoxLayout()
Layout_line4=QHBoxLayout()

Layout_line1.addWidget(btn_Menu)
Layout_line1.addWidget(btn_Sleep)
Layout_line1.addWidget(box_Minutes)

Layout_line2.addWidget(qtext,alignment=Qt.AlignVCenter)
Layout_line3.addWidget(RadioGroupBox)
Layout_line4.addWidget(btn_Ok,alignment=Qt.AlignVCenter)

Layout_card=QVBoxLayout()
Layout_card.addLayout(Layout_line1)
Layout_card.addLayout(Layout_line2)
Layout_card.addLayout(Layout_line3)
Layout_card.addLayout(Layout_line4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)
RadioGroupBox.setLayout(Layout_ans1)



main_win.setLayout(Layout_card)
main_win.show()
app.exec_()
