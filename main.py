

from PyQt5 import QtWidgets

from uisetup import MainWindowUI


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = MainWindowUI()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
