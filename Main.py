import random

from PyQt5.QtWidgets import *
import base

import Menu


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

res_lbl = QLabel("Результат")
next_quest_btn = QPushButton("Наступне запитання")

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

horizotal1_line.addWidget(v_1)
horizotal1_line.addWidget(v_2)
group_main_line.addLayout(horizotal1_line)

horizotal2_line.addWidget(v_3)
horizotal2_line.addWidget(v_4)
group_main_line.addLayout(horizotal2_line)
group.setLayout(group_main_line)
group_main_line.addWidget(res_lbl)
main_line.addWidget(group)

main_line.addWidget(answer_bth)

main_line.addLayout(horizotal_line)
main_line.addWidget(next_quest_btn)

answers = [v_1, v_2, v_3, v_4]
def set_quest():
    random.shuffle(answers)
    current_question = base.questions[base.nomer]
    text2_btn.setText(current_question["запитання"])
    answers[0].setText(current_question["Правильна відповідь"])
    answers[1].setText(current_question["Не правильна відповідь1"])
    answers[2].setText(current_question["Не правильна відповідь2"])
    answers[3].setText(current_question["Не правильна відповідь3"])

set_quest()
def ans_func():
    if answers[0].isChecked():
        res_lbl.setText("Правильно")
    else:
        res_lbl.setText("Не правильно")

    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    res_lbl.show()
    next_quest_btn.show()
    answer_bth.hide()

def test_func():
    random.shuffle(answers)
    current_question = base.questions[base.nomer]
    text2_btn.setText(current_question["запитання"])
    answers[0].show()
    answers[1].show()
    answers[2].show()
    answers[3].show()
    res_lbl.hide()
    next_quest_btn.hide()
    answer_bth.show()
    base.nomer += 1
    set_quest()

next_quest_btn.clicked.connect(test_func)
answer_bth.clicked.connect(ans_func)
menu_btn.clicked.connect(Menu.menu)
res_lbl.hide()
next_quest_btn.hide()


window.setLayout(main_line)
window.show()
app.exec()