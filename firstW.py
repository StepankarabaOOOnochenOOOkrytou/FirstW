# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from final_win import *
from second_win import *

app = QApplication([])

class FirstW(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Здоровье")
        self.resize(900,700)

        self.winner = QLabel("Добро пожаловать в программу по определению состояния здоровья!")
        self.dgt = QLabel('''
        Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.
        Проба Руфье представляет собой нагрузочный комплекс, предназначенный 
        для оценки работоспособности сердца при физической нагрузке. 
        У испытуемого, находяшегося в положении лежа на спине в течени 5 минут, 
        определяют чистоту пульса за 15 секунд;
        затем в течении 45 секунд испытуемый выполняет 30 приседаний.
        После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,
        а потом - за последние 15 секунд первой минуты периода восстановления.
        Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в
        ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.
        ''')
        self.button = QPushButton("Начать")
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.winner)
        self.v_line.addWidget(self.dgt)
        self.v_line.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)

        self.button.clicked.connect(self.next)
        self.show()

    def next(self):
        self.hide()
        self.NW = SecondW()
        self.NW.show()

mainWin = FirstW()

app.exec_()
