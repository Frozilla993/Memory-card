from PyQt5.QtCore import Qt
from PyQt5.QWidgets import QApplication, QWidget, QTable, QListView, QListWidgetItem, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QLabel, QPushButton, QSpinBox
app = QApplication([])

menu_btn = QPushButton('Меню')
sleep_btn = QpushButton('Відпочити')
time_sleep = QSpinBox()
time_sleep.setValue(20)
okyn_btn = QPushButton('Відвповісти')
okyn_lb = QLabel('#####')


RadioGroupBox = QGroupBox('Варіант відповідей')
RadioGroup = QButtonGroup()
rdb_1 = QRadioButton('#####')
rdb_2 = QRadioButton('#####')
rdb_3 = QRadioButton('#####')
rdb_4 = QRadioButton('#####')
RadioGroup.addButton(rdbt_1)
RadioGroup.addButton(rdbt_2)
RadioGroup.addButton(rdbt_3)
RadioGroup.addButton(rdbt_4)


resultGroupBox = QGroupBox('Результат тесту')
result_lb = QLabel('#####')
result_true_lb = QLabel('#####')


layout_an1 = QHBoxLayout()
layout_an2 = QVBoxLayout()
layout_an3 = QVBoxLayout()

layout_an2.addWidget(rdbt_1)
layout_an2.addWidget(rdbt_2)

layout_an3.addWidget(rdbt_3)
layout_an3.addWidget(rdbt_4)

layout_an1.addLayout(layout_an2)
layout_an1.addLayout(layout_an3)
RadioGroupBox.setLayout(layout_an3)

layout_res = QVBoxLayout()
layout_res.addWidget(result_lb, alligment=Qt.AlignLeft|Qt.AlignTop)
layout_res.addWidget(result_true_lb, alligment=Qt.AlignHCenter, stretch = 2)
resultGroupBox.setLayout()
resultGroupBox.hide()


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(menu_btn)
layout_line1.addStretch(1)
layout_line1.addWidget(sleep_btn)
layout_line1.addWidget(time_sleep)

layout_line2.addWidget(okyn_lb)
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(result_lb)

layout_line4.addStretch(1)
layout_line4.addWidget(okyn_btn, stretch = 2)
layout_line4.addStretch(1)

card_layout = QVBoxLayout()
card_layout.addLayout(layout_line1, stretch = 1)
card_layout.addLayout(layout_line2, stretch = 2)
card_layout.addLayout(layout_line3, stretch = 8)
card_layout.addStretch(1)
card_layout.addLayout(layout_line4, stretch = 1)
card_layout.setSpacing(S)


def show_result():
    RadioGroupBox.hide()
    resultGroupBox.show()
    okyn_btn.setText('Наступне питання')

def show_question():
    RadioGroupBox.hide()
    resultGroupBox.show()
    okyn_btn.setText('Відповісти')

RadioGroup.setExclusive(False)
rdb_1.setChecked(False)
rdb_2.setChecked(False)
rdb_3.setChecked(False)
rdb_4.setChecked(False)
RadioGroup.setExclusive(True)

















