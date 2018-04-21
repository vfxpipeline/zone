# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Thu Oct 27 09:03:39 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(634, 860)
        MainWindow.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/qss_icons/rc/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 5px 30px 5px 30px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/qss_icons/rc/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/qss_icons/rc/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    border: 1px solid #444;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover\n"
"{\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px transparent #4A4949;\n"
"    border-radius: 2px;\n"
"    margin: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 1px transparent #4A4949;\n"
" border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 1px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    background-color: transparent;\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"        QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #444;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 9, 0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_7 = QtGui.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.frame_7)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(129, 129, 129);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.server_ip_2 = QtGui.QLabel(self.frame_7)
        self.server_ip_2.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.server_ip_2.setObjectName(_fromUtf8("server_ip_2"))
        self.horizontalLayout_3.addWidget(self.server_ip_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.db_server_status = QtGui.QLabel(self.frame_7)
        self.db_server_status.setMaximumSize(QtCore.QSize(15, 15))
        self.db_server_status.setText(_fromUtf8(""))
        self.db_server_status.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/green.gif")))
        self.db_server_status.setScaledContents(True)
        self.db_server_status.setObjectName(_fromUtf8("db_server_status"))
        self.horizontalLayout_5.addWidget(self.db_server_status)
        self.label_6 = QtGui.QLabel(self.frame_7)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 170, 127);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.frame_7)
        self.label.setStyleSheet(_fromUtf8("color: rgb(129, 129, 129);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.server_ip = QtGui.QLabel(self.frame_7)
        self.server_ip.setStyleSheet(_fromUtf8("color: rgb(0, 170, 255);"))
        self.server_ip.setObjectName(_fromUtf8("server_ip"))
        self.horizontalLayout_2.addWidget(self.server_ip)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.repo_server_status = QtGui.QLabel(self.frame_7)
        self.repo_server_status.setMaximumSize(QtCore.QSize(15, 15))
        self.repo_server_status.setText(_fromUtf8(""))
        self.repo_server_status.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/green.gif")))
        self.repo_server_status.setScaledContents(True)
        self.repo_server_status.setObjectName(_fromUtf8("repo_server_status"))
        self.horizontalLayout_4.addWidget(self.repo_server_status)
        self.label_3 = QtGui.QLabel(self.frame_7)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 170, 127);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_7, 0, 3, 1, 1)
        self.server_icon = QtGui.QLabel(self.frame_2)
        self.server_icon.setMaximumSize(QtCore.QSize(150, 100))
        self.server_icon.setText(_fromUtf8(""))
        self.server_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/server.gif")))
        self.server_icon.setScaledContents(True)
        self.server_icon.setObjectName(_fromUtf8("server_icon"))
        self.gridLayout_5.addWidget(self.server_icon, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans Unicode"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(132, 132, 132);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.job_info_tab = QtGui.QWidget()
        self.job_info_tab.setObjectName(_fromUtf8("job_info_tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.job_info_tab)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame_4 = QtGui.QFrame(self.job_info_tab)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.treeWidget_jobs = QtGui.QTreeWidget(self.frame_4)
        self.treeWidget_jobs.setStyleSheet(_fromUtf8("background-image: url(:/icons/images/bg/bg1.jpg);"))
        self.treeWidget_jobs.setFrameShape(QtGui.QFrame.NoFrame)
        self.treeWidget_jobs.setFrameShadow(QtGui.QFrame.Plain)
        self.treeWidget_jobs.setObjectName(_fromUtf8("treeWidget_jobs"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_jobs)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_jobs)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_jobs)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_jobs)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_jobs)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_jobs)
        self.gridLayout_6.addWidget(self.treeWidget_jobs, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.job_info_tab, _fromUtf8(""))
        self.client_info_tab = QtGui.QWidget()
        self.client_info_tab.setObjectName(_fromUtf8("client_info_tab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.client_info_tab)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.frame_5 = QtGui.QFrame(self.client_info_tab)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_14 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.groupBox = QtGui.QGroupBox(self.frame_5)
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.frame_6 = QtGui.QFrame(self.groupBox)
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_10.setMargin(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.frame_6)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.client_id_LE = QtGui.QLineEdit(self.frame_6)
        self.client_id_LE.setReadOnly(True)
        self.client_id_LE.setObjectName(_fromUtf8("client_id_LE"))
        self.horizontalLayout_11.addWidget(self.client_id_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtGui.QLabel(self.frame_6)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        self.database_LE = QtGui.QLineEdit(self.frame_6)
        self.database_LE.setReadOnly(True)
        self.database_LE.setObjectName(_fromUtf8("database_LE"))
        self.horizontalLayout_12.addWidget(self.database_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_7 = QtGui.QLabel(self.frame_6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_10.addWidget(self.label_7)
        self.client_status_LE = QtGui.QLineEdit(self.frame_6)
        self.client_status_LE.setReadOnly(True)
        self.client_status_LE.setObjectName(_fromUtf8("client_status_LE"))
        self.horizontalLayout_10.addWidget(self.client_status_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_17 = QtGui.QLabel(self.frame_6)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_16.addWidget(self.label_17)
        self.database_port_LE = QtGui.QLineEdit(self.frame_6)
        self.database_port_LE.setReadOnly(True)
        self.database_port_LE.setObjectName(_fromUtf8("database_port_LE"))
        self.horizontalLayout_16.addWidget(self.database_port_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.frame_6)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.running_time_LE = QtGui.QLineEdit(self.frame_6)
        self.running_time_LE.setReadOnly(True)
        self.running_time_LE.setObjectName(_fromUtf8("running_time_LE"))
        self.horizontalLayout_8.addWidget(self.running_time_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_18 = QtGui.QLabel(self.frame_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_17.addWidget(self.label_18)
        self.repo_path_LE = QtGui.QLineEdit(self.frame_6)
        self.repo_path_LE.setReadOnly(True)
        self.repo_path_LE.setObjectName(_fromUtf8("repo_path_LE"))
        self.horizontalLayout_17.addWidget(self.repo_path_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_17, 2, 1, 1, 1)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_19 = QtGui.QLabel(self.frame_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_18.addWidget(self.label_19)
        self.description_LE = QtGui.QLineEdit(self.frame_6)
        self.description_LE.setReadOnly(False)
        self.description_LE.setObjectName(_fromUtf8("description_LE"))
        self.horizontalLayout_18.addWidget(self.description_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_18, 3, 0, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(self.frame_6)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.comment_LE = QtGui.QLineEdit(self.frame_6)
        self.comment_LE.setReadOnly(False)
        self.comment_LE.setObjectName(_fromUtf8("comment_LE"))
        self.horizontalLayout_7.addWidget(self.comment_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_7, 4, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_11 = QtGui.QLabel(self.frame_6)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.associate_pools_LE = QtGui.QLineEdit(self.frame_6)
        self.associate_pools_LE.setReadOnly(True)
        self.associate_pools_LE.setObjectName(_fromUtf8("associate_pools_LE"))
        self.horizontalLayout_6.addWidget(self.associate_pools_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout_6, 5, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_12 = QtGui.QLabel(self.frame_6)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.associate_groups_LE = QtGui.QLineEdit(self.frame_6)
        self.associate_groups_LE.setReadOnly(True)
        self.associate_groups_LE.setObjectName(_fromUtf8("associate_groups_LE"))
        self.horizontalLayout.addWidget(self.associate_groups_LE)
        self.gridLayout_10.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.gridLayout_9.addWidget(self.frame_6, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.frame_5)
        self.groupBox_2.setStyleSheet(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.client_specification_frame = QtGui.QFrame(self.groupBox_2)
        self.client_specification_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.client_specification_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.client_specification_frame.setObjectName(_fromUtf8("client_specification_frame"))
        self.gridLayout_11 = QtGui.QGridLayout(self.client_specification_frame)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_14 = QtGui.QLabel(self.client_specification_frame)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        self.os_name_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.os_name_LE.setReadOnly(True)
        self.os_name_LE.setObjectName(_fromUtf8("os_name_LE"))
        self.horizontalLayout_13.addWidget(self.os_name_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_23 = QtGui.QLabel(self.client_specification_frame)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_22.addWidget(self.label_23)
        self.user_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.user_LE.setReadOnly(True)
        self.user_LE.setObjectName(_fromUtf8("user_LE"))
        self.horizontalLayout_22.addWidget(self.user_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_22, 0, 1, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_15 = QtGui.QLabel(self.client_specification_frame)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_14.addWidget(self.label_15)
        self.cpu_name_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.cpu_name_LE.setObjectName(_fromUtf8("cpu_name_LE"))
        self.horizontalLayout_14.addWidget(self.cpu_name_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_20 = QtGui.QLabel(self.client_specification_frame)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_19.addWidget(self.label_20)
        self.cpu_type_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.cpu_type_LE.setObjectName(_fromUtf8("cpu_type_LE"))
        self.horizontalLayout_19.addWidget(self.cpu_type_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_19, 1, 1, 1, 1)
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_27 = QtGui.QLabel(self.client_specification_frame)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_26.addWidget(self.label_27)
        self.l2_cache_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.l2_cache_LE.setReadOnly(True)
        self.l2_cache_LE.setObjectName(_fromUtf8("l2_cache_LE"))
        self.horizontalLayout_26.addWidget(self.l2_cache_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_26, 2, 0, 1, 1)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_28 = QtGui.QLabel(self.client_specification_frame)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_27.addWidget(self.label_28)
        self.l3_cache_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.l3_cache_LE.setReadOnly(True)
        self.l3_cache_LE.setObjectName(_fromUtf8("l3_cache_LE"))
        self.horizontalLayout_27.addWidget(self.l3_cache_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_27, 2, 1, 1, 1)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_16 = QtGui.QLabel(self.client_specification_frame)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_15.addWidget(self.label_16)
        self.ram_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.ram_LE.setReadOnly(True)
        self.ram_LE.setObjectName(_fromUtf8("ram_LE"))
        self.horizontalLayout_15.addWidget(self.ram_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.label_29 = QtGui.QLabel(self.client_specification_frame)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_28.addWidget(self.label_29)
        self.hostname_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.hostname_LE.setReadOnly(True)
        self.hostname_LE.setObjectName(_fromUtf8("hostname_LE"))
        self.horizontalLayout_28.addWidget(self.hostname_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_28, 3, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_8 = QtGui.QLabel(self.client_specification_frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_9.addWidget(self.label_8)
        self.disc_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.disc_LE.setReadOnly(True)
        self.disc_LE.setObjectName(_fromUtf8("disc_LE"))
        self.horizontalLayout_9.addWidget(self.disc_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_21 = QtGui.QLabel(self.client_specification_frame)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_20.addWidget(self.label_21)
        self.ip_address_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.ip_address_LE.setReadOnly(True)
        self.ip_address_LE.setObjectName(_fromUtf8("ip_address_LE"))
        self.horizontalLayout_20.addWidget(self.ip_address_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_20, 4, 1, 1, 1)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_24 = QtGui.QLabel(self.client_specification_frame)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_23.addWidget(self.label_24)
        self.gpu_card_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.gpu_card_LE.setReadOnly(True)
        self.gpu_card_LE.setObjectName(_fromUtf8("gpu_card_LE"))
        self.horizontalLayout_23.addWidget(self.gpu_card_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_23, 5, 0, 1, 1)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_22 = QtGui.QLabel(self.client_specification_frame)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_21.addWidget(self.label_22)
        self.mac_address_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.mac_address_LE.setReadOnly(True)
        self.mac_address_LE.setObjectName(_fromUtf8("mac_address_LE"))
        self.horizontalLayout_21.addWidget(self.mac_address_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_21, 5, 1, 1, 1)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_26 = QtGui.QLabel(self.client_specification_frame)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_25.addWidget(self.label_26)
        self.gpu_memory_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.gpu_memory_LE.setReadOnly(True)
        self.gpu_memory_LE.setObjectName(_fromUtf8("gpu_memory_LE"))
        self.horizontalLayout_25.addWidget(self.gpu_memory_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_25, 6, 0, 1, 1)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_25 = QtGui.QLabel(self.client_specification_frame)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_24.addWidget(self.label_25)
        self.network_speed_LE = QtGui.QLineEdit(self.client_specification_frame)
        self.network_speed_LE.setReadOnly(True)
        self.network_speed_LE.setObjectName(_fromUtf8("network_speed_LE"))
        self.horizontalLayout_24.addWidget(self.network_speed_LE)
        self.gridLayout_11.addLayout(self.horizontalLayout_24, 6, 1, 1, 1)
        self.gridLayout_12.addWidget(self.client_specification_frame, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_13.setMargin(0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.listWidget_services = QtGui.QListWidget(self.groupBox_3)
        self.listWidget_services.setStyleSheet(_fromUtf8(""))
        self.listWidget_services.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_services.setFrameShadow(QtGui.QFrame.Plain)
        self.listWidget_services.setViewMode(QtGui.QListView.ListMode)
        self.listWidget_services.setObjectName(_fromUtf8("listWidget_services"))
        item = QtGui.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/images/control_panel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_services.addItem(item)
        self.gridLayout_13.addWidget(self.listWidget_services, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.client_info_tab, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RenderBOX Client Console", None))
        self.label_4.setText(_translate("MainWindow", "Database Server   : ", None))
        self.server_ip_2.setText(_translate("MainWindow", "192.168.4.202", None))
        self.label_6.setText(_translate("MainWindow", "Connected", None))
        self.label.setText(_translate("MainWindow", "Repository Server : ", None))
        self.server_ip.setText(_translate("MainWindow", "192.168.4.202", None))
        self.label_3.setText(_translate("MainWindow", "Connected", None))
        self.label_2.setText(_translate("MainWindow", "ELITEBOOK-PC", None))
        self.treeWidget_jobs.headerItem().setText(0, _translate("MainWindow", "App", None))
        self.treeWidget_jobs.headerItem().setText(1, _translate("MainWindow", "Job Name", None))
        self.treeWidget_jobs.headerItem().setText(2, _translate("MainWindow", "Description", None))
        self.treeWidget_jobs.headerItem().setText(3, _translate("MainWindow", "Status", None))
        self.treeWidget_jobs.headerItem().setText(4, _translate("MainWindow", "user", None))
        __sortingEnabled = self.treeWidget_jobs.isSortingEnabled()
        self.treeWidget_jobs.setSortingEnabled(False)
        self.treeWidget_jobs.topLevelItem(0).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_jobs.topLevelItem(1).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_jobs.topLevelItem(2).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_jobs.topLevelItem(3).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_jobs.topLevelItem(4).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_jobs.topLevelItem(5).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_jobs.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.job_info_tab), _translate("MainWindow", "Jobs Information", None))
        self.groupBox.setTitle(_translate("MainWindow", "Renderbox Client Configurations", None))
        self.label_5.setText(_translate("MainWindow", "Client ID", None))
        self.label_13.setText(_translate("MainWindow", "Database IP Address", None))
        self.label_7.setText(_translate("MainWindow", "Client Status", None))
        self.label_17.setText(_translate("MainWindow", "Database Port", None))
        self.label_9.setText(_translate("MainWindow", "Running Time", None))
        self.label_18.setText(_translate("MainWindow", "Repository Path", None))
        self.label_19.setText(_translate("MainWindow", "Description", None))
        self.label_10.setText(_translate("MainWindow", "Comment", None))
        self.label_11.setText(_translate("MainWindow", "Associated Pools", None))
        self.label_12.setText(_translate("MainWindow", "Associated Groups", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Client Specifications", None))
        self.label_14.setText(_translate("MainWindow", "Operating System", None))
        self.label_23.setText(_translate("MainWindow", "User", None))
        self.label_15.setText(_translate("MainWindow", "CPU", None))
        self.label_20.setText(_translate("MainWindow", "CPU Type", None))
        self.cpu_type_LE.setText(_translate("MainWindow", "X64", None))
        self.label_27.setText(_translate("MainWindow", "L2 Cache", None))
        self.label_28.setText(_translate("MainWindow", "L3 Cache", None))
        self.label_16.setText(_translate("MainWindow", "RAM", None))
        self.label_29.setText(_translate("MainWindow", "Host Name", None))
        self.label_8.setText(_translate("MainWindow", "DISK", None))
        self.label_21.setText(_translate("MainWindow", "IP Address", None))
        self.label_24.setText(_translate("MainWindow", "GPU Card", None))
        self.label_22.setText(_translate("MainWindow", "Mac Address", None))
        self.label_26.setText(_translate("MainWindow", "GPU Memory", None))
        self.label_25.setText(_translate("MainWindow", "Network Speed", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Installed Services", None))
        __sortingEnabled = self.listWidget_services.isSortingEnabled()
        self.listWidget_services.setSortingEnabled(False)
        item = self.listWidget_services.item(0)
        item.setText(_translate("MainWindow", "Maya2015", None))
        item = self.listWidget_services.item(1)
        item.setText(_translate("MainWindow", "Windows CMD", None))
        item = self.listWidget_services.item(2)
        item.setText(_translate("MainWindow", "Linux Shell Script", None))
        item = self.listWidget_services.item(3)
        item.setText(_translate("MainWindow", "Python2", None))
        item = self.listWidget_services.item(4)
        item.setText(_translate("MainWindow", "Python3", None))
        item = self.listWidget_services.item(5)
        item.setText(_translate("MainWindow", "Blender2.78", None))
        item = self.listWidget_services.item(6)
        item.setText(_translate("MainWindow", "Houdini15", None))
        item = self.listWidget_services.item(7)
        item.setText(_translate("MainWindow", "Nuke9", None))
        item = self.listWidget_services.item(8)
        item.setText(_translate("MainWindow", "Natron2.2", None))
        item = self.listWidget_services.item(9)
        item.setText(_translate("MainWindow", "Realflow2016", None))
        item = self.listWidget_services.item(10)
        item.setText(_translate("MainWindow", "3ds Max2016", None))
        item = self.listWidget_services.item(11)
        item.setText(_translate("MainWindow", "Modo", None))
        item = self.listWidget_services.item(12)
        item.setText(_translate("MainWindow", "After Effects CS6", None))
        self.listWidget_services.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.client_info_tab), _translate("MainWindow", "Client Information", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))

import icons_rc
