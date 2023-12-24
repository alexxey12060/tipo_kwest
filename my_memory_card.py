from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

class question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(question('самая дорогая мка', 'm5cs', 'x7', 'm5 f90 2022', 'm5 first edition'))
question_list.append(question('что быстрее всех', 'BMW M5 CS 1200HP AWD', 'AUDI Q7 600HP АWD','MERSEDES CLS63 AWD','ROLSE-ROYSE CULLINAN 800HP AWD',))
question_list.append(question('у кого комфортабельнее салон?', 'MERSEDES S CLASS', 'AUDI Q7','BMW M5 F90','ROLSE-ROYSE CULLINAN',))
question_list.append(question('чей ремонт дороже(внешка)', 'ROLSE-ROYSE CULLINAN ', 'AUDI Q7','BMW M5 F90','MERSEDES S CLASS',))
question_list.append(question('чей ремонт дороже(мотор и тд)', 'BMW M5 F90', 'AUDI Q7','ROLSE-ROYSE CULLINAN','MERSEDES S CLASS',))
question_list.append(question('чья стоимость составляет 14 150 000 - 16 190 000 рублей', 'BMW X6 M', 'Audi RS Q8','Bentley Continental GT','Mercedes-Maybach S class',))
question_list.append(question('чья стоимость составляет 11 900 000 - 15 948 700', 'Bentley Bentayga 2020', 'Audi RS 6','BMW X7 M','Mercedes-Benz E-Class E53',))

app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1
main_win.resize(400, 200)
main_win.total = 1
main_win.score = 0

main_win.setWindowTitle('alexey12060')
wopros = QPushButton('ответить')
wopros_werx = QLabel('самый последний x7')

RadioGroup = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('x7 m60i')
rbtn_2 = QRadioButton('x7 2020')
rbtn_3 = QRadioButton('x7 2019')
rbtn_4 = QRadioButton('x7 2021')

Radio = QButtonGroup()
Radio.addButton(rbtn_1)
Radio.addButton(rbtn_2)
Radio.addButton(rbtn_3)
Radio.addButton(rbtn_4)

layout_anc1 = QHBoxLayout()
layout_anc2 = QVBoxLayout()
layout_anc3 = QVBoxLayout()

layout_anc2.addWidget(rbtn_1)
layout_anc2.addWidget(rbtn_2)

layout_anc3.addWidget(rbtn_3)
layout_anc3.addWidget(rbtn_4)

layout_anc1.addLayout(layout_anc2)
layout_anc1.addLayout(layout_anc3)
RadioGroup.setLayout(layout_anc1)

ancGroup = QGroupBox('Результат теста')
result = QLabel('Правда или Не правда')
otvet = QLabel('x7 m60i')

Layout_res = QVBoxLayout()
Layout_res.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(otvet, alignment = Qt.AlignHCenter)
ancGroup.setLayout(Layout_res)




Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()

Layout_line1.addWidget(wopros_werx, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
Layout_line2.addWidget(RadioGroup)
Layout_line2.addWidget(ancGroup)
ancGroup.hide()
Layout_line3.addStretch(1)
Layout_line3.addWidget(wopros, stretch=2)
Layout_line3.addStretch(1)

Layout_card = QVBoxLayout()
Layout_card.setSpacing(5)

Layout_card.addLayout(Layout_line1, stretch=2)
Layout_card.addLayout(Layout_line2, stretch=8)
Layout_card.addLayout(Layout_line3, stretch=2)








main_win.setLayout(Layout_card)

def show_result():
    RadioGroup.hide()
    ancGroup.show()
    wopros.setText('Следующий вопрос')
def show_wopros_werx():
    RadioGroup.show()
    ancGroup.hide()
    wopros.setText('ответить')
    Radio.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    Radio.setExclusive(True)

def test():
    if 'ответить' == wopros.text():
        show_result()
    else:
        show_wopros_werx()

#wopros.clicked.connect(test)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    wopros_werx.setText(q.question)

    otvet.setText(q.right_answer)
    show_wopros_werx()

def show_correct(res):
    result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('правильно')
        main_win.score+=1
        print('Статистика \n Всего вопросов:', main_win.total, '\n Правильных ответов', main_win.score)
        print('рейтинг:', main_win.score/main_win.total * 100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('не верно')
        print('рейтинг:', main_win.score/main_win.total * 100, '%')

def next_question():
    main_win.total +=1
    print('Статистика \n Всего вопросов:', main_win.total, '\n Правильных ответов', main_win.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def clicked_OK():
    if wopros.text() == 'ответить':
        check_answer()
    else:
        next_question()


wopros.clicked.connect(clicked_OK)






#RadioGroup = QGroupBox('ОТВЕТИТЬ')



#ancGroup = QGroupBox('РЕЗУЛЬТАТ')




main_win.show()
app.exec()













































































































































































