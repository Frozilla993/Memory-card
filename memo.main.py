from memo_card_layout import (app, layout_card, lbQuestion, lbCorrect, lbResult, rbtn_1, rbtn_2, rbtn_3, rbtn_4, btn_Ok, show_result, show_question)
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle

card_width, card_height = 600, 900
text_wrong = 'Неправильно'
text_correct = 'Правильно'

frm_question = 'З якого року Україна стала незалежна'
frm_right = '1991'
frm_wrong1 = 'Завтра'
frm_wrong2 = 'Вчора'
frm_wrong3 = '250млн років до нашої ери'

radiolist = [rbtn_1,rbtn_2, rbtn_3, rbtn_4]
shuffle(radiolist)
answer = radiolist[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radiolist[1],radiolist[2],radiolist[3]

def show_data():
    lbQuestion.setText(frm_question)
    lb_correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    correct = answer.isChecked()
    if correct:
        lb_Result.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            lb_Result.setText(text_wrong)
            show_result()

    def click_ok():
        if btn_Ok != 'Наступне питання':
            check_result()
    
win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300,300)
win_card.setWindowTitle('Memory card')

win_card.setLayout(layout_card)
show_data()
show.question()
btn_Ok.Clicked.connect(click_ok)


win_card.show()
app.exec_()