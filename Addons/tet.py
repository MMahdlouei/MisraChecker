import sys
from PySide6.QtWidgets import QApplication, QTextBrowser, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Link to Code Line Example')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        text_browser = QTextBrowser()
        layout.addWidget(text_browser)

        # Simulated code with line numbers
        code_lines = [
            "1. def my_function():",
            "2.     print('Hello, world!')",
            "3. ",
            "4. my_function()"
        ]

        # Generate HTML with clickable line numbers
        formatted_lines = []
        for i, line in enumerate(code_lines, start=1):
            formatted_line = f'<a href="line:{i}">{i:3d}</a> {line}'
            formatted_lines.append(formatted_line)

        code_html = '<br>'.join(formatted_lines)
        text_browser.setHtml(code_html)

    def linkClicked(self, url):
        # Handle link clicks
        if url.scheme() == "line":
            line_number = int(url.host())
            print(f"Clicked on line {line_number}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    text_browser = mainWindow.findChild(QTextBrowser)
    text_browser.anchorClicked.connect(mainWindow.linkClicked)
    mainWindow.show()
    sys.exit(app.exec())
