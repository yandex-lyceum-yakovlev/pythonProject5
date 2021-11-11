import sys
import re
import pymorphy2

import docx

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout,  QTextEdit



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Text manager Instruction')
        """прикрепление аудио файла"""
        self.load_mp3('media.mp3')
        """создание кнопки для воспроизведения аудио файла"""
        self.playBtn = QPushButton('Воспроизвести', self)
        self.playBtn.resize(self.playBtn.sizeHint())
        self.playBtn.move(40, 150)
        self.playBtn.clicked.connect(self.player.play)
        """создание кнопки для приостановки аудио файла"""
        self.pauseBtn = QPushButton('Пауза', self)
        self.pauseBtn.resize(self.pauseBtn.sizeHint())
        self.pauseBtn.move(180, 150)
        self.pauseBtn.clicked.connect(self.player.pause)
        """создание кнопки для выключения аудио файла"""
        self.stopBtn = QPushButton('Стоп', self)
        self.stopBtn.resize(self.stopBtn.sizeHint())
        self.stopBtn.move(40, 190)
        self.stopBtn.clicked.connect(self.player.stop)
        """создание кнопки для перехода на следующую страницу"""
        self.btn = QPushButton('Дальше', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(180, 190)
        self.btn.clicked.connect(self.open_types_of_files_form)

        self.label = QLabel(self)
        self.label.move(40, 30)
        self.text_label = QLabel(self)
        self.text_label.setText("Вас приветствует Text manager.")
        self.text_label.move(70, 20)
        self.text_label = QLabel(self)
        self.text_label.setText("Text manager - это программа для анализа содержания")
        self.text_label.move(10, 40)
        self.text_label = QLabel(self)
        self.text_label.setText("текста и поиска ответа на заданный вами вопрос.")
        self.text_label.move(10, 60)
        self.text_label = QLabel(self)
        self.text_label.setText("Чтобы получше познакомится с функциями Text manager,")
        self.text_label.move(10, 80)
        self.text_label = QLabel(self)
        self.text_label.setText(" вы можите прослушать аудиоинструкцию,")
        self.text_label.move(40, 100)
        self.text_label = QLabel(self)
        self.text_label.setText(" нажав на кнопку 'Воспроизвести'.")
        self.text_label.move(60, 120)

    def open_types_of_files_form(self):
        self.types_of_files_form = TypesOfFilesForm(self, "Данные для второй формы")
        self.types_of_files_form.show()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


class TypesOfFilesForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Text manager')
        """создание кнопки для прикрепления word файла"""
        self.btn_word_file = QPushButton(self)
        self.btn_word_file.clicked.connect(self.showDialog)
        self.btn_word_file.setIcon(QIcon('word_file.jpg'))
        self.btn_word_file.move(170, 140)
        self.btn_word_file.setIconSize(QSize(100, 100))
        """создание кнопки для прикрепления text файла"""
        self.btn_text_file = QPushButton(self)
        self.btn_text_file.clicked.connect(self.open_text_form)
        self.btn_text_file.setIcon(QIcon('text_file.jpg'))
        self.btn_text_file.move(30, 140)
        self.btn_text_file.setIconSize(QSize(100, 100))
        self.name_label = QLabel(self)
        self.name_label.setText("Выберите формат файла,")
        self.name_label.move(60, 90)
        self.name_label = QLabel(self)
        self.name_label.setText("который хотите прикрепить.")
        self.name_label.move(60, 105)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Load file', '', "Word File (*)")
        if fname:
            doc = docx.Document
            all_paras = doc.paragraphs
            text1 = []
            """разбиение текста на параграфы и добавление каждого параграфа в список text1"""
            for para in all_paras:
                text1.append(((para.text).replace("\xa0", " ")))
            text1 = ''.join(text1)
            self.text = text1.text()
        else:
            QMessageBox.warning(self, 'Error', "Файл не выбран.")
        self.open_question_form()

    def open_question_form(self):
        self.question_form = QuestionForm(self, "")
        self.question_form.show()

    def open_text_form(self):
        self.text_form = TextForm(self, "")
        self.text_form.show()


class TextForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        self.length = ''


    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Text manager Text file')
        """создание кнопки для загрузки введенного текста"""
        self.btn_download1 = QPushButton('Отправить', self)
        self.btn_download1.resize(self.btn_download1.sizeHint())
        self.btn_download1.move(100, 150)
        self.btn_download1.clicked.connect(self.open_question_form)
        self.label = QLabel(self)
        self.label.move(40, 30)
        self.text_label = QLabel(self)
        self.text_label.setText("Пожалуйста введите текст.")
        self.text_label.move(100, 90)
        self.text_input = QLineEdit(self)
        self.text_input.move(100, 110)
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        self.text = self.text_input.text()

    def open_question_form(self):
        self.question_form = QuestionForm(self, "test", self.length)
        self.question_form.show()


class QuestionForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        self.length = ''
        self.text = ''

    def initUI(self, args):
        length = args[2]
        length1 = str(length)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Text manager Text file')
        """создание кнопки для загрузки введенного текста"""
        self.btn_download2 = QPushButton('Отправить', self)
        self.btn_download2.resize(self.btn_download2.sizeHint())
        self.btn_download2.move(100, 150)
        """если есть ответ навопрос то есть длина списа с ответами не равно 0"""
        """тогда можно открывать класс вывода ответов иначе открыть класс"""
        """в котором программа говорит о том что  совпадений нет"""
        if length1 != '0':
            self.btn_download2.clicked.connect(self.open_result_form)
        else:
            self.btn_download2.clicked.connect(self.open_bad_result_form)
        self.label = QLabel(self)
        self.label.move(40, 30)
        self.text_label = QLabel(self)
        self.text_label.setText("Пожалуйста введите текст вопроса.")
        self.text_label.move(100, 90)
        self.question_input = QLineEdit(self)
        self.question_input.move(100, 110)
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        self.question = self.question_input.text()

    def open_result_form(self):
        try:
            self.result_form = ResultForm(self, "", self.text, self.question)
            self.result_form.show()
        except Exception as e:
            print(e)


    def open_bad_result_form(self):
        self.bad_result_form = BadResultForm(self, "")
        self.bad_result_form.show()


class ResultForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
        self.text = ''
        self.question = ''


    def initUI(self, args):
        self.text = args[2]
        self.question = args[3]
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Text manager Answer')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        self.text_label = QLabel(self)
        self.text_label.setText("Все результаты по вашему запросу: ")
        self.text_label.move(40, 30)
        self.label = QLabel(self)
        n = 0
        for i in self.text_output:
            n += 1
            """вывод новых результатов"""
            self.label.setText(i)
            """координаты новой строки каждый раз смещаются на 15"""
            self.label1.move(40, 30 + 15 * n)
        """создание полосы прокрутки"""
        app = QApplication([])
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.label1)
        self.scroll_area.show()
        app.exec()
        self.text_analysis()

    def text_analysis(self):

        morph = pymorphy2.MorphAnalyzer()
        a = []
        b = []
        analysis_text = []
        """разбиение введенного текста предложения и слова путем создания вложенных списков"""
        split_regex = re.compile(r'[.|!|?|…]')
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(self.text)])
        for s in sentences:
            g = s.split()
            for t in g:
                res = morph.parse(t)[0]
                """во вложенные списки попадают только те части речи,
                 которые не являются частицами, местоимениями, местоимениями, союзами, предлогами """
                if ("CONJ" not in res.tag) and ("NPRO" not in res.tag) and ("PREP" not in res.tag) and (
                        "PRCL" not in res.tag):
                    """причем слова изменются и попадают в список в начальной форме"""
                    b.append(morph.parse(t)[0].normal_form)
                    a.append(b)
                    b = []
            analysis_text.append(a)
            a = []
        numbers = []
        """сравниваются слова из введенного текста и слова из текста вопроса """
        for i in analysis_text:
            for j in i:
                e = ''.join(j)
                for k in self.question.split():
                    if k == e:
                        """и добаляются индексы предложений в новый список"""
                        numbers.append(analysis_text.index(i))
        numbers1 = []
        for i in numbers:
            """если в предложении и вопросе 2 и больше одинаковых слов, 
            то индексы этих предложений попадают в новый список """
            if numbers.count(i) >= 2:
                numbers1.append(i)
        numbers2 = []
        for i in numbers1:
            if i not in numbers2:
                numbers2.append(i)
        self.length = str(len(numbers2))
        self.text_output = []
        for i in numbers2:
            text_output1 = (
                (((str((analysis_text[int(i)]))).replace("['", "")).replace("'],", "")).replace("']]", "")).replace(
                "[", "")
            self.text_output.append(text_output1)



class BadResultForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Text manager Answer')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.text_label1 = QLabel(self)
        self.text_label2 = QLabel(self)
        self.text_label3 = QLabel(self)
        self.text_label4 = QLabel(self)
        self.text_label1.setText("К сожалению результатов по вашему запросу ")
        self.text_label2.setText("не найдено. Попробуйте еще раз сформулировав")
        self.text_label3.setText("более точный вопрос или приложите больше")
        self.text_label4.setText("информации для поиска.")
        self.text_label1.move(40, 90)
        self.text_label2.move(40, 105)
        self.text_label3.move(40, 120)
        self.text_label4.move(40, 135)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

