
## PyQt5 Web Browser

### Overview
This Python application is a simple web browser built using PyQt5. It includes features such as URL navigation, ad blocking, and history viewing capabilities.

### Features
- **URL Navigation:** Enter URLs directly or search via the URL bar.
- **Ad Blocker:** Blocks predefined ad URLs for a cleaner browsing experience.
- **History Viewer:** Displays a list of visited URLs for easy navigation history access.

### Requirements
- Python 3.x
- PyQt5
- PyQtWebEngine (part of PyQt5)
  
### Installation
1. Ensure Python is installed. If not, download and install Python from [python.org](https://www.python.org).
2. Install PyQt5 and PyQtWebEngine using pip:
   ```bash
   pip install PyQt5 PyQtWebEngine
   ```
3. Download or clone the repository:
   ```bash
   git clone <repository_url>
   cd PyQt5-Web-Browser
   ```
4. Run the application:
   ```bash
   python main.py
   ```

### Usage
1. Launch the application.
2. Enter a URL in the address bar and press Enter or click the "Go" button to navigate.
3. Use the "History" button to view a list of visited URLs.
4. Enjoy browsing with ad-blocking capabilities for a more streamlined experience.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements
- This application utilizes PyQt5 for GUI development.
- Ad blocking functionality is achieved through `QWebEngineUrlRequestInterceptor`.



