# PyQt5 introduction
# for install : "pip install PyQt5"

# sys (system specific parameter and function) : used to maintained by the interpreter and to functions that interact strongly with the interperter. it is always available 
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(). __init__()
        
        self.setWindowTitle("Fist GUI")
        self.setGeometry(700, 300, 500, 500) # (x, y, width, height)
        self.setWindowIcon(QIcon("icon.svg"))
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()