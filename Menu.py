from PyQt5.QtWidgets import *

import base
def menu():
    window = QDialog()
    main_line = QVBoxLayout()

    add_btn = QPushButton("Добавити")
    quest_lbl = QLabel("запитання")
    quest_ledt = QLineEdit()

    h1 = QVBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_ledt)
    main_line.addLayout(h1)

    right_lbl = QLabel("Правилна відповидь")
    right_ledt = QLineEdit()

    h2 = QVBoxLayout()
    h2.addWidget(right_lbl)
    h2.addWidget(right_ledt)
    main_line.addLayout(h2)

    right2_lbl = QLabel("Не правилна відповидь")
    right2_ledt = QLineEdit()

    h3 = QVBoxLayout()
    h3.addWidget(right2_lbl)
    h3.addWidget(right2_ledt)
    main_line.addLayout(h3)

    right3_lbl = QLabel("Не правилна відповидь")
    right3_ledt = QLineEdit()

    h4 = QVBoxLayout()
    h4.addWidget(right3_lbl)
    h4.addWidget(right3_ledt)
    main_line.addLayout(h4)

    right4_lbl = QLabel("Не правилна відповидь")
    right4_ledt = QLineEdit()

    h5 = QVBoxLayout()
    h5.addWidget(right4_lbl)
    h5.addWidget(right4_ledt)
    main_line.addLayout(h5)

    def add_func():
        new_quest =  {
        "запитання": quest_ledt.text(),
        "Правильна відповідь": right_ledt.text(),
        "Не правильна відповідь1": right2_ledt.text(),
        "Не правильна відповідь2": right3_ledt.text(),
        "Не правильна відповідь3": right4_ledt.text(),

        }
        base.questions.append(new_quest)

    add_btn.clicked.connect(add_func)
    main_line.addWidget(add_btn)

    window.setLayout(main_line)
    window.exec()