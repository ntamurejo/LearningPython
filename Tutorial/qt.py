import sys
import cv2

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,150)
    w.move(300,0)
    w.setWindowTitle('Simple')
    w.show()


    sys.exit(app.exec_())