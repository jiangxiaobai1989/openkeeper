# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/ok/gui/ui/mainwindow.ui'
#
# Created: Sat Oct 16 03:44:38 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(250, 604)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("None")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setStyleSheet("None")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outter_login = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outter_login.sizePolicy().hasHeightForWidth())
        self.outter_login.setSizePolicy(sizePolicy)
        self.outter_login.setStyleSheet("None")
        self.outter_login.setObjectName("outter_login")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.outter_login)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.outter_login)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.outter_net_username = QtGui.QComboBox(self.outter_login)
        self.outter_net_username.setEditable(True)
        self.outter_net_username.setObjectName("outter_net_username")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.outter_net_username)
        self.outter_net_username_extra = QtGui.QLineEdit(self.outter_login)
        self.outter_net_username_extra.setEnabled(False)
        self.outter_net_username_extra.setObjectName("outter_net_username_extra")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.outter_net_username_extra)
        self.label_2 = QtGui.QLabel(self.outter_login)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.outter_net_password = QtGui.QLineEdit(self.outter_login)
        self.outter_net_password.setText("")
        self.outter_net_password.setEchoMode(QtGui.QLineEdit.Password)
        self.outter_net_password.setObjectName("outter_net_password")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.outter_net_password)
        self.outter_remember_passwd = QtGui.QCheckBox(self.outter_login)
        self.outter_remember_passwd.setCursor(QtCore.Qt.PointingHandCursor)
        self.outter_remember_passwd.setChecked(True)
        self.outter_remember_passwd.setObjectName("outter_remember_passwd")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.outter_remember_passwd)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_7 = QtGui.QLabel(self.outter_login)
        self.label_7.setObjectName("label_7")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.outter_eth_select = QtGui.QComboBox(self.outter_login)
        self.outter_eth_select.setEditable(True)
        self.outter_eth_select.setObjectName("outter_eth_select")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.outter_eth_select)
        self.verticalLayout_5.addLayout(self.formLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outter_net_on = QtGui.QPushButton(self.outter_login)
        self.outter_net_on.setCursor(QtCore.Qt.PointingHandCursor)
        self.outter_net_on.setObjectName("outter_net_on")
        self.horizontalLayout.addWidget(self.outter_net_on)
        self.outter_net_off = QtGui.QPushButton(self.outter_login)
        self.outter_net_off.setCursor(QtCore.Qt.PointingHandCursor)
        self.outter_net_off.setObjectName("outter_net_off")
        self.horizontalLayout.addWidget(self.outter_net_off)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.outter_textBrowser = QtGui.QTextBrowser(self.outter_login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outter_textBrowser.sizePolicy().hasHeightForWidth())
        self.outter_textBrowser.setSizePolicy(sizePolicy)
        self.outter_textBrowser.setMaximumSize(QtCore.QSize(180, 195))
        self.outter_textBrowser.setObjectName("outter_textBrowser")
        self.verticalLayout_5.addWidget(self.outter_textBrowser)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_onboot = QtGui.QCheckBox(self.outter_login)
        self.start_onboot.setEnabled(False)
        self.start_onboot.setObjectName("start_onboot")
        self.verticalLayout_2.addWidget(self.start_onboot)
        self.login_inner_before_outter = QtGui.QCheckBox(self.outter_login)
        self.login_inner_before_outter.setEnabled(False)
        self.login_inner_before_outter.setChecked(True)
        self.login_inner_before_outter.setObjectName("login_inner_before_outter")
        self.verticalLayout_2.addWidget(self.login_inner_before_outter)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.outter_login)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.inner_login = QtGui.QGroupBox(self.tab_2)
        self.inner_login.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inner_login.sizePolicy().hasHeightForWidth())
        self.inner_login.setSizePolicy(sizePolicy)
        self.inner_login.setCheckable(False)
        self.inner_login.setObjectName("inner_login")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.inner_login)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtGui.QLabel(self.inner_login)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.inner_username = QtGui.QComboBox(self.inner_login)
        self.inner_username.setEditable(True)
        self.inner_username.setObjectName("inner_username")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.inner_username)
        self.label_4 = QtGui.QLabel(self.inner_login)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.inner_password = QtGui.QLineEdit(self.inner_login)
        self.inner_password.setEchoMode(QtGui.QLineEdit.Password)
        self.inner_password.setObjectName("inner_password")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.inner_password)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtGui.QLabel(self.inner_login)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.inner_eth_select = QtGui.QComboBox(self.inner_login)
        self.inner_eth_select.setEditable(True)
        self.inner_eth_select.setObjectName("inner_eth_select")
        self.inner_eth_select.addItem("")
        self.inner_eth_select.addItem("")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.inner_eth_select)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtGui.QPushButton(self.inner_login)
        self.pushButton_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.inner_login)
        self.pushButton_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.inner_textBrowser = QtGui.QTextBrowser(self.inner_login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inner_textBrowser.sizePolicy().hasHeightForWidth())
        self.inner_textBrowser.setSizePolicy(sizePolicy)
        self.inner_textBrowser.setMaximumSize(QtCore.QSize(180, 192))
        self.inner_textBrowser.setObjectName("inner_textBrowser")
        self.verticalLayout_4.addWidget(self.inner_textBrowser)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.inner_remember_passwd = QtGui.QCheckBox(self.inner_login)
        self.inner_remember_passwd.setObjectName("inner_remember_passwd")
        self.verticalLayout_3.addWidget(self.inner_remember_passwd)
        self.checkBox_3 = QtGui.QCheckBox(self.inner_login)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.inner_login)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 250, 25))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtGui.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_account = QtGui.QAction(MainWindow)
        self.action_account.setObjectName("action_account")
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu.addAction(self.action_account)
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_about)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_exit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenKeeper", None, QtGui.QApplication.UnicodeUTF8))
        self.outter_login.setTitle(QtGui.QApplication.translate("MainWindow", "拨号后即可关闭", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.outter_net_username_extra.setText(QtGui.QApplication.translate("MainWindow", "@cqupt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.outter_remember_passwd.setText(QtGui.QApplication.translate("MainWindow", "记住密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "网卡", None, QtGui.QApplication.UnicodeUTF8))
        self.outter_net_on.setText(QtGui.QApplication.translate("MainWindow", "拨号", None, QtGui.QApplication.UnicodeUTF8))
        self.outter_net_off.setText(QtGui.QApplication.translate("MainWindow", "挂断", None, QtGui.QApplication.UnicodeUTF8))
        self.start_onboot.setText(QtGui.QApplication.translate("MainWindow", "开机自动启动", None, QtGui.QApplication.UnicodeUTF8))
        self.login_inner_before_outter.setText(QtGui.QApplication.translate("MainWindow", "登录外网前先登录内网", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "外网登录", None, QtGui.QApplication.UnicodeUTF8))
        self.inner_login.setTitle(QtGui.QApplication.translate("MainWindow", "本模块研发中。。。", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "网卡", None, QtGui.QApplication.UnicodeUTF8))
        self.inner_eth_select.setItemText(0, QtGui.QApplication.translate("MainWindow", "eth0", None, QtGui.QApplication.UnicodeUTF8))
        self.inner_eth_select.setItemText(1, QtGui.QApplication.translate("MainWindow", "wlan0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "拨号", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "挂断", None, QtGui.QApplication.UnicodeUTF8))
        self.inner_remember_passwd.setText(QtGui.QApplication.translate("MainWindow", "记住密码", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "挂断外网前先挂断内网", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "内网登录", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("MainWindow", "帮助", None, QtGui.QApplication.UnicodeUTF8))
        self.action_account.setText(QtGui.QApplication.translate("MainWindow", "账户管理(&M)...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_account.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "退出(&Q)", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("MainWindow", "关于...(&A)", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
import background_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

