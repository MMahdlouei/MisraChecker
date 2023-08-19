# This Python file uses the following encoding: utf-8
import sys
import os

SettingPath = sys.path[0].replace("\\MisraGUI","")
sys.path.append(SettingPath+'\\addons')
sys.path.append(SettingPath+'\\Cppcheck')
SettingPath = sys.path[0].replace("\\MisraGui","")
CppCheckPath = SettingPath+'\\Cppcheck\\'
sys.path.append(SettingPath+'\\addons')
sys.path.append(SettingPath+'\\Cppcheck')
SettingPath = SettingPath  +"\\Config\\setting.txt"
import re

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from PySide6.QtGui import QTextCursor  # Import QTextCursor
import misra
from io import StringIO


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(True)
        self.custom_stream = CustomStream(self.ui.textEdit)
        sys.stdout = self.custom_stream
        self.BrowseText()
        self.BrowseFile()
#        self.redirector = StdoutRedirector(self.ui.textEdit)
        self.ui.btnanalyze.clicked.connect(self.Analyze)
        self.ui.btnBrowseFile.clicked.connect(self.BrowseNewFile)
        self.ui.btnBrowseText.clicked.connect(self.BrowseNewText)

    def Analyze(self):
        self.ui.textEdit.clear()
        os.system(CppCheckPath+"cppcheck --dump " + self.file_path)
        misra.main(self.file_path + ".dump", self.txt_path)
#
#        os.system("python misra.py --rule-text=" + self.txt_path + " " + self.file_path + ".dump")


    def ReadSetting(self):
        try:
            file = open(SettingPath , "r")
        except:
            file = open(SettingPath , "w")
            file = open(SettingPath , "r")
        self.content = file.read()
        file.close()

    def BrowseText(self):
        self.ReadSetting()
        txtpattern = "Text Rule Path:\"(.*)\""
        try:
            self.txt_path = re.findall(txtpattern, self.content)[0]
        except:
            self.txt_path, _ = QFileDialog.getOpenFileName(self, "Select Misra Rules Text File", "", "Text File (*.txt)", options=QFileDialog.Options())
            file = open(SettingPath , "a")
            file.write("Text Rule Path:\""+self.txt_path+"\"")
            file.close()
        self.ui.txtpath.setText(self.txt_path)

    def BrowseFile(self):
        self.ReadSetting()
        txtpattern = "File To Analyze Path:\"(.*)\""
        try:
            self.file_path = re.findall(txtpattern, self.content)[0]

        except:
            self.file_path, _ = QFileDialog.getOpenFileName(self, "Select C/C++ File To Analyze", "", "C Files (*.c *.cpp)", options=QFileDialog.Options())

            file = open(SettingPath , "a")
            file.write("\nFile To Analyze Path:\""+self.file_path+"\"")
            file.close()
        self.ui.filepath.setText(self.file_path)

    def BrowseNewFile(self):
        file = open(SettingPath , "r")
        content = file.read()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select C/C++ File To Analyze", "", "C Files (*.c *.cpp)", options=QFileDialog.Options())
        txtpattern = "File To Analyze Path:\"(.*)\""
        print(re.findall(txtpattern, self.content)[0])
        print(self.file_path)
        content = content.replace(re.findall(txtpattern, self.content)[0], self.file_path)
        print(content)
        file = open(SettingPath , "w")
        file.write(content)
        file.close()
        self.ui.filepath.setText(self.file_path)

    def BrowseNewText(self):
        file = open(SettingPath, "r")
        content = file.read()
        self.txt_path, _ = QFileDialog.getOpenFileName(self, "Select Misra Rules Text File", "", "Text Files (*.txt)", options=QFileDialog.Options())
        txtpattern = "Text Rule Path:\"(.*)\""
        content = content.replace(re.findall(txtpattern, self.content)[0], self.txt_path)
        file = open(SettingPath, "w")
        file.write(content)
        file.close()
        self.ui.txtpath.setText(self.txt_path)

class CustomStream:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.original_stdout = sys.stdout
        self.buffer = StringIO()

    def write(self, message):
        self.buffer.write(message)
        self.text_widget.moveCursor(QTextCursor.End)
        self.text_widget.insertPlainText(message)
        self.original_stdout.write(message)

    def flush(self):
        self.original_stdout.flush()

    def get_value(self):
        return self.buffer.getvalue()

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.original_stdout = sys.stdout
        sys.stdout = self

    def write(self, text):
        cursor = self.text_widget.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.text_widget.setTextCursor(cursor)
        self.text_widget.ensureCursorVisible()
        self.original_stdout.write(text)

    def flush(self):
        self.original_stdout.flush()

    def __del__(self):
        sys.stdout = self.original_stdout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

