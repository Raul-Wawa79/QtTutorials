import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStatusBar, QTextEdit, QToolBar, QDockWidget)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction

class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Basic Menu Example 2')
        self.setCentralWidget(QTextEdit())
        self.createMenu()
        self.createToolBar()
        self.createDockWidget()
        self.show()

    def createMenu(self):
        self.exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)
        full_screen_act = QAction('Full Screen', self, checkable=True)
        full_screen_act.setStatusTip('Switch to full screen mode')
        full_screen_act.triggered.connect(self.switchToFullScreen)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_act)
        view_menu = menu_bar.addMenu('View')
        appearance_submenu = view_menu.addMenu('Appearance')
        appearance_submenu.addAction(full_screen_act)
        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)
        tool_bar.addAction(self.exit_act)

    def createDockWidget(self):
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        dock_widget.setWidget(QTextEdit())
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

    def switchToFullScreen(self, state):
        if state:
            self.showFullScreen()
        else:
            self.showNormal()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec())