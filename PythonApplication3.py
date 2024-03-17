from loguru import logger
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from qwe import Ui_MainWindow

logger.add('LZW.log', format="{message}", level='DEBUG')


class LZW(QtWidgets.QMainWindow):
    @classmethod
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.lang = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.LZW)

    def LZW(self):
        string = str(self.ui.lineEdit.text())
        dictionary = {chr(i): i for i in range(1, 123)}
        last = 256
        p = ""
        result1 = []
        for c in string:
            pc = p + c
            if pc in dictionary:
                p = pc
            else:
                result1.append(dictionary[p])
                dictionary[pc] = last
                last += 1
                p = c
            if p != '':
                result1.append(dictionary[p])
                x2 = len(result1)
        logger.debug(result1)
        # Decoding
        dictionary2 = {i: chr(i) for i in range(1, 123)}
        last2 = 256
        result2 = []
        p = result1.pop(0)
        result2.append(dictionary2[p])
        for c in result1:
            if c in dictionary2:
                entry = dictionary2[c]
            result2.append(entry)
            dictionary2[last2] = dictionary2[p] + entry[0]
            last2 += 1
            p = c
            x1 = len(string)
            x3 = (x2 * 9) / (x1 * 8)
        logger.debug(''.join(result2))
        logger.debug(x1)
        logger.debug(x2)
        logger.debug(x3)
        n = 'check log'
        self.ui.textEdit.setText((n))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LZW()
    myapp.show()
    sys.exit(app.exec_())
