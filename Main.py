from PyQt5.QtWidgets import *

app = QApplication([])


window = QWidget()
window.resize(600,500)

menu_btn = QPushButton("Меню")
idk_btn = QPushButton("Відпочити")
spin_btn = QSpinBox()
text_btn = QLabel("хвилин")
text2_btn = QLabel("Яблуко")
text3_btn = QLabel("Варіанти відповідей")
v_1 = QRadioButton("caterpillar")
v_2 = QRadioButton("apple")
v_3 = QRadioButton("application")
v_4 = QRadioButton("building")
answer_bth = QPushButton("Відповісти")

group = QGroupBox("Варіанти відповідей")
main_line = QVBoxLayout()

horizotal_line = QHBoxLayout()
horizotal_line.addWidget(menu_btn)
horizotal_line.addWidget(idk_btn)
horizotal_line.addWidget(spin_btn)
horizotal_line.addWidget(text_btn)
main_line.addLayout(horizotal_line)
main_line.addWidget(text2_btn)

horizotal1_line = QHBoxLayout()
horizotal2_line = QHBoxLayout()
group_main_line = QVBoxLayout()

group.setLayout(horizotal1_line)
horizotal1_line.addWidget(v_1)
horizotal1_line.addWidget(v_2)
group.setLayout(horizotal2_line)
horizotal2_line.addWidget(v_3)
horizotal2_line.addWidget(v_4)
group.setLayout(group_main_line)
main_line.addWidget(group)

main_line.addWidget(answer_bth)

main_line.addLayout(horizotal_line)


window.setLayout(main_line)
window.show()
app.exec()