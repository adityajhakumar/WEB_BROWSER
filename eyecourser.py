import sys
import logging
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class AdBlocker(QWebEngineUrlRequestInterceptor):
    blocked_urls = [
        'ad.doubleclick.net',
        'adservice.google.com',
        # Add more URLs as needed
    ]

    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        for blocked_url in self.blocked_urls:
            if blocked_url in url:
                info.block(True)
                return

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Python Web Browser')
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView()
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.navigate_to_url)
        self.history_view_button = QPushButton('History')
        self.history_view_button.clicked.connect(self.show_history)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.url_bar)
        self.layout.addWidget(self.go_button)
        self.layout.addWidget(self.history_view_button)
        self.layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Configure ad blocker
        self.ad_blocker = AdBlocker()
        profile = self.web_view.page().profile()
        profile.setRequestInterceptor(self.ad_blocker)

        # Initialize history list
        self.history = []

    def navigate_to_url(self, url=None):
        if not url:
            url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        try:
            logger.debug(f"Loading URL: {url}")
            self.web_view.setUrl(QUrl(url))
            self.history.append(url)  # Add to history list
        except Exception as e:
            logger.error(f"Error loading URL: {str(e)}")
            QMessageBox.critical(self, 'Error', f'Failed to load URL: {url}\nError: {str(e)}')

    def show_history(self):
        if not self.history:
            QMessageBox.information(self, 'History', 'No history yet.')
            return
        
        history_dialog = QMessageBox(self)
        history_dialog.setWindowTitle('History')
        history_dialog.setText('Visited URLs:')
        history_dialog.setDetailedText('\n'.join(self.history))
        history_dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.navigate_to_url("http://google.com")  # Initial URL
    browser.show()
    logger.debug("Application running...")
    sys.exit(app.exec_())
