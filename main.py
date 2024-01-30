# This is a sample Python script.
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt import Ui_MainWindow
from process import run_process


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.destTextEdit.setReadOnly(True)
        self.changeButton.pressed.connect(self.change)
        self.copyButton.pressed.connect(self.copy)
        self.show()

    def change(self):
        # Perform pre-translation to English via Google Translate.
        fileName = 'dataset/TEXT.txt'
        if fileName:
            text = self.srcTextEdit.toPlainText()
            with open(fileName, "w") as file:   # 清除文档重写
                file.write(text)

        changedText = run_process()
        self.destTextEdit.setPlainText(changedText)

    def copy(self):
        # 获取源文本编辑框的纯文本内容
        plainText = self.destTextEdit.document().toPlainText()

        # 将纯文本复制到剪贴板
        clipboard = QApplication.clipboard()
        clipboard.setText(plainText, QClipboard.Clipboard)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
