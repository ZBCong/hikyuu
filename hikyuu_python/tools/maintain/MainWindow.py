# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1071, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.start_import_pushButton = QtWidgets.QPushButton(self.tab)
        self.start_import_pushButton.setGeometry(QtCore.QRect(510, 30, 75, 23))
        self.start_import_pushButton.setObjectName("start_import_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 310, 481, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 451, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tdx_dir_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.tdx_dir_lineEdit.setObjectName("tdx_dir_lineEdit")
        self.gridLayout_2.addWidget(self.tdx_dir_lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.select_tdx_dir_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_tdx_dir_pushButton.sizePolicy().hasHeightForWidth())
        self.select_tdx_dir_pushButton.setSizePolicy(sizePolicy)
        self.select_tdx_dir_pushButton.setObjectName("select_tdx_dir_pushButton")
        self.gridLayout_2.addWidget(self.select_tdx_dir_pushButton, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 108, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.tdx_servers_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.tdx_servers_comboBox.setGeometry(QtCore.QRect(130, 120, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tdx_servers_comboBox.sizePolicy().hasHeightForWidth())
        self.tdx_servers_comboBox.setSizePolicy(sizePolicy)
        self.tdx_servers_comboBox.setObjectName("tdx_servers_comboBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(360, 120, 31, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.tdx_port_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.tdx_port_lineEdit.setGeometry(QtCore.QRect(400, 120, 71, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tdx_port_lineEdit.sizePolicy().hasHeightForWidth())
        self.tdx_port_lineEdit.setSizePolicy(sizePolicy)
        self.tdx_port_lineEdit.setMinimumSize(QtCore.QSize(10, 0))
        self.tdx_port_lineEdit.setMaxLength(6)
        self.tdx_port_lineEdit.setObjectName("tdx_port_lineEdit")
        self.pytdx_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.pytdx_radioButton.setEnabled(True)
        self.pytdx_radioButton.setGeometry(QtCore.QRect(20, 100, 125, 16))
        self.pytdx_radioButton.setObjectName("pytdx_radioButton")
        self.tdx_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.tdx_radioButton.setGeometry(QtCore.QRect(20, 30, 481, 16))
        self.tdx_radioButton.setObjectName("tdx_radioButton")
        self.ping_tdx_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.ping_tdx_pushButton.setEnabled(True)
        self.ping_tdx_pushButton.setGeometry(QtCore.QRect(20, 150, 75, 23))
        self.ping_tdx_pushButton.setObjectName("ping_tdx_pushButton")
        self.search_tdx_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.search_tdx_pushButton.setEnabled(True)
        self.search_tdx_pushButton.setGeometry(QtCore.QRect(110, 150, 151, 23))
        self.search_tdx_pushButton.setObjectName("search_tdx_pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 481, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 451, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hdf5_dir_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.hdf5_dir_lineEdit.setObjectName("hdf5_dir_lineEdit")
        self.gridLayout_3.addWidget(self.hdf5_dir_lineEdit, 0, 1, 1, 1)
        self.hdf5_dir_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.hdf5_dir_pushButton.setObjectName("hdf5_dir_pushButton")
        self.gridLayout_3.addWidget(self.hdf5_dir_pushButton, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(510, 70, 481, 431))
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 461, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.hdf5_trans_progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.hdf5_trans_progressBar.setProperty("value", 0)
        self.hdf5_trans_progressBar.setObjectName("hdf5_trans_progressBar")
        self.gridLayout.addWidget(self.hdf5_trans_progressBar, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.hdf5_5min_progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.hdf5_5min_progressBar.setProperty("value", 0)
        self.hdf5_5min_progressBar.setObjectName("hdf5_5min_progressBar")
        self.gridLayout.addWidget(self.hdf5_5min_progressBar, 1, 1, 1, 1)
        self.hdf5_min_progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.hdf5_min_progressBar.setProperty("value", 0)
        self.hdf5_min_progressBar.setObjectName("hdf5_min_progressBar")
        self.gridLayout.addWidget(self.hdf5_min_progressBar, 2, 1, 1, 1)
        self.hdf5_weight_label = QtWidgets.QLabel(self.layoutWidget2)
        self.hdf5_weight_label.setObjectName("hdf5_weight_label")
        self.gridLayout.addWidget(self.hdf5_weight_label, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.hdf5_day_progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.hdf5_day_progressBar.setProperty("value", 0)
        self.hdf5_day_progressBar.setObjectName("hdf5_day_progressBar")
        self.gridLayout.addWidget(self.hdf5_day_progressBar, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.hdf5_time_progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.hdf5_time_progressBar.setProperty("value", 0)
        self.hdf5_time_progressBar.setObjectName("hdf5_time_progressBar")
        self.gridLayout.addWidget(self.hdf5_time_progressBar, 4, 1, 1, 1)
        self.import_detail_textEdit = QtWidgets.QTextEdit(self.groupBox_5)
        self.import_detail_textEdit.setGeometry(QtCore.QRect(10, 180, 461, 241))
        self.import_detail_textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.import_detail_textEdit.setReadOnly(True)
        self.import_detail_textEdit.setObjectName("import_detail_textEdit")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 110, 481, 181))
        self.groupBox_7.setObjectName("groupBox_7")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 60, 155, 18))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.import_stock_checkBox = QtWidgets.QCheckBox(self.layoutWidget3)
        self.import_stock_checkBox.setObjectName("import_stock_checkBox")
        self.horizontalLayout_3.addWidget(self.import_stock_checkBox)
        self.import_fund_checkBox = QtWidgets.QCheckBox(self.layoutWidget3)
        self.import_fund_checkBox.setObjectName("import_fund_checkBox")
        self.horizontalLayout_3.addWidget(self.import_fund_checkBox)
        self.import_future_checkBox = QtWidgets.QCheckBox(self.layoutWidget3)
        self.import_future_checkBox.setEnabled(False)
        self.import_future_checkBox.setObjectName("import_future_checkBox")
        self.horizontalLayout_3.addWidget(self.import_future_checkBox)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 90, 297, 18))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.import_day_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.import_day_checkBox.setObjectName("import_day_checkBox")
        self.horizontalLayout_2.addWidget(self.import_day_checkBox)
        self.import_min_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.import_min_checkBox.setObjectName("import_min_checkBox")
        self.horizontalLayout_2.addWidget(self.import_min_checkBox)
        self.import_min5_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.import_min5_checkBox.setObjectName("import_min5_checkBox")
        self.horizontalLayout_2.addWidget(self.import_min5_checkBox)
        self.import_trans_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.import_trans_checkBox.setEnabled(True)
        self.import_trans_checkBox.setObjectName("import_trans_checkBox")
        self.horizontalLayout_2.addWidget(self.import_trans_checkBox)
        self.import_time_checkBox = QtWidgets.QCheckBox(self.layoutWidget4)
        self.import_time_checkBox.setEnabled(True)
        self.import_time_checkBox.setObjectName("import_time_checkBox")
        self.horizontalLayout_2.addWidget(self.import_time_checkBox)
        self.import_weight_checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.import_weight_checkBox.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.import_weight_checkBox.setObjectName("import_weight_checkBox")
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 120, 411, 48))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.trans_max_days_spinBox = QtWidgets.QSpinBox(self.layoutWidget5)
        self.trans_max_days_spinBox.setMinimum(1)
        self.trans_max_days_spinBox.setMaximum(300)
        self.trans_max_days_spinBox.setProperty("value", 70)
        self.trans_max_days_spinBox.setObjectName("trans_max_days_spinBox")
        self.gridLayout_4.addWidget(self.trans_max_days_spinBox, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.time_max_days_spinBox = QtWidgets.QSpinBox(self.layoutWidget5)
        self.time_max_days_spinBox.setMinimum(1)
        self.time_max_days_spinBox.setMaximum(2000)
        self.time_max_days_spinBox.setProperty("value", 70)
        self.time_max_days_spinBox.setObjectName("time_max_days_spinBox")
        self.gridLayout_4.addWidget(self.time_max_days_spinBox, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 2, 1, 1)
        self.import_status_label = QtWidgets.QLabel(self.tab)
        self.import_status_label.setGeometry(QtCore.QRect(620, 30, 361, 21))
        self.import_status_label.setObjectName("import_status_label")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据导入工具"))
        self.start_import_pushButton.setText(_translate("MainWindow", "执行导入"))
        self.groupBox_2.setTitle(_translate("MainWindow", "数据源设置"))
        self.label_2.setText(_translate("MainWindow", "通达信安装目录："))
        self.select_tdx_dir_pushButton.setText(_translate("MainWindow", "选择"))
        self.label_10.setText(_translate("MainWindow", "通达信行情服务器："))
        self.label_3.setText(_translate("MainWindow", "端口："))
        self.tdx_port_lineEdit.setText(_translate("MainWindow", "7709"))
        self.pytdx_radioButton.setText(_translate("MainWindow", "使用Pytdx（推荐）"))
        self.tdx_radioButton.setText(_translate("MainWindow", "使用通达信盘后数据（不支持分笔、分时数据）"))
        self.ping_tdx_pushButton.setText(_translate("MainWindow", "测试连接"))
        self.search_tdx_pushButton.setText(_translate("MainWindow", "查找速度最快的服务器"))
        self.groupBox_3.setTitle(_translate("MainWindow", "数据保存设置"))
        self.hdf5_dir_pushButton.setText(_translate("MainWindow", "选择"))
        self.label.setText(_translate("MainWindow", "目标数据（HDF5）存放目录："))
        self.groupBox_5.setTitle(_translate("MainWindow", "导入进展"))
        self.label_4.setText(_translate("MainWindow", "导入分笔数据："))
        self.label_14.setText(_translate("MainWindow", "导入1分钟线："))
        self.hdf5_weight_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "导入日线："))
        self.label_12.setText(_translate("MainWindow", "导入5分钟线："))
        self.label_9.setText(_translate("MainWindow", "导入权息数据："))
        self.label_5.setText(_translate("MainWindow", "导入分时数据："))
        self.import_detail_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入上证日线记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入深证日线记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入上证5分钟线记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入深证5分钟线记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入上证1分钟线记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入深证1分钟线记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入上证分笔记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入深证分笔记录：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入上证分时数据：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入深证分时数据：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入权息数据数：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">导入完毕！</p></body></html>"))
        self.groupBox_7.setTitle(_translate("MainWindow", "导入设置"))
        self.import_stock_checkBox.setText(_translate("MainWindow", "股票"))
        self.import_fund_checkBox.setText(_translate("MainWindow", "基金"))
        self.import_future_checkBox.setText(_translate("MainWindow", "期货"))
        self.import_day_checkBox.setText(_translate("MainWindow", "日线"))
        self.import_min_checkBox.setText(_translate("MainWindow", "1分钟线"))
        self.import_min5_checkBox.setText(_translate("MainWindow", "5分钟线"))
        self.import_trans_checkBox.setText(_translate("MainWindow", "分笔"))
        self.import_time_checkBox.setText(_translate("MainWindow", "分时"))
        self.import_weight_checkBox.setText(_translate("MainWindow", "下载并导入钱龙权息数据"))
        self.label_7.setText(_translate("MainWindow", "初次导入分时最大导入天数（自然日）："))
        self.label_6.setText(_translate("MainWindow", "初次导入分笔最大导入天数（自然日）："))
        self.label_11.setText(_translate("MainWindow", "（最大300天）"))
        self.label_13.setText(_translate("MainWindow", "（最大2000天，慢）"))
        self.import_status_label.setText(_translate("MainWindow", "import_status_label"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "数据导入"))

