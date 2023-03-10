# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
os.system("rm face_rec.stop")
os.system("rm face_rec.run")
os.system("echo '' > user/detected_users.txt")
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1250, 751)

        #exit system
        self.exit_system = QtWidgets.QPushButton(Dialog)
        self.exit_system.setGeometry(QtCore.QRect(950, 670, 271, 34))
        self.exit_system.setMaximumSize(QtCore.QSize(271, 34))
        self.exit_system.setObjectName("exit_system")
        self.exit_system.clicked.connect(self.exitSystem)
        #exit system

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 801, 711))
        self.gridLayoutWidget.setMaximumSize(QtCore.QSize(801, 711))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        #add user
        self.add_user = QtWidgets.QPushButton(Dialog)
        self.add_user.setGeometry(QtCore.QRect(950, 620, 271, 34))
        self.add_user.setMaximumSize(QtCore.QSize(271, 34))
        self.add_user.setObjectName("add_user")
        self.add_user.clicked.connect(self.addUser)
        #add user

        #list user
        self.list_users = QtWidgets.QPushButton(Dialog)
        self.list_users.setGeometry(QtCore.QRect(950, 570, 271, 34))
        self.list_users.setMaximumSize(QtCore.QSize(271, 34))
        self.list_users.setObjectName("list_users")
        self.list_users.clicked.connect(self.listUser)
        #list user

        #start recognition
        self.start_recognition = QtWidgets.QPushButton(Dialog)
        self.start_recognition.setGeometry(QtCore.QRect(950, 520, 271, 34))
        self.start_recognition.setMaximumSize(QtCore.QSize(271, 34))
        self.start_recognition.setObjectName("start_recognition")
        self.start_recognition.clicked.connect(self.startRecognition)
        #start recognition

        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(950, 20, 271, 218))
        self.gridLayoutWidget_2.setMaximumSize(QtCore.QSize(271, 218))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.recognited_users_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.recognited_users_grid.setContentsMargins(0, 0, 0, 0)
        self.recognited_users_grid.setObjectName("recognited_users_grid")

        self.UserslistView = QtWidgets.QListView(self.gridLayoutWidget_2)
        self.UserslistView.setMaximumSize(QtCore.QSize(269, 192))
        self.UserslistView.setObjectName("UserslistView")

        self.recognited_users_grid.addWidget(self.UserslistView, 1, 0, 1, 1)
        self.title_of_recognited_users = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.title_of_recognited_users.setMaximumSize(QtCore.QSize(269, 18))
        self.title_of_recognited_users.setObjectName("title_of_recognited_users")
        self.recognited_users_grid.addWidget(self.title_of_recognited_users, 0, 0, 1, 1)
        self.title_of_recognited_users.raise_()
        self.UserslistView.raise_()
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(950, 250, 271, 191))
        self.gridLayoutWidget_3.setMaximumSize(QtCore.QSize(271, 191))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.camera_frame_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.camera_frame_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.camera_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.camera_frame_layout.setHorizontalSpacing(2)
        self.camera_frame_layout.setVerticalSpacing(0)
        self.camera_frame_layout.setObjectName("camera_frame_layout")
        self.camera_freame = QtWidgets.QLCDNumber(self.gridLayoutWidget_3)
        self.camera_freame.setMaximumSize(QtCore.QSize(269, 189))
        self.camera_freame.setMode(QtWidgets.QLCDNumber.Dec)
        self.camera_freame.setProperty("value", 0.0)
        self.camera_freame.setProperty("intValue", 2)
        self.camera_freame.setObjectName("camera_freame")
        self.camera_frame_layout.addWidget(self.camera_freame, 1, 1, 1, 1)
        self.actionimage = QtWidgets.QAction(Dialog)
        self.actionimage.setObjectName("actionimage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Face Detection GUI"))
        self.exit_system.setText(_translate("Dialog", "Exit system"))
        self.add_user.setText(_translate("Dialog", "Add User"))
        self.list_users.setText(_translate("Dialog", "List users"))
        self.start_recognition.setText(_translate("Dialog", "Start recognation"))
        self.title_of_recognited_users.setText(_translate("Dialog", "Recognited Users"))
        self.actionimage.setText(_translate("Dialog", "image"))

    def startRecognition(self):
        os.system("echo '' > user/detected_users.txt")
        if os.path.exists("face_rec.run"):
            print("stopping...")
            os.system("touch face_rec.stop")
            self.start_recognition.setText("Start recognation")
         
        else:     
            print("Pressed start recognition_button")
            print("starting face_recognition script")
            os.system("python run.face_recognition.py &> /dev/null &")
            os.system("touch face_rec.run")
            self.start_recognition.setText("Stop recognation")

    def addUser(self):
        print("Pressed add_user button")
        os.system("bash files/add.user.sh")

    def listUser(self):
        print("Pressed list_user button")
        with open("user/detected_users.txt", "r") as file:
            data = file.readlines()
            users = set(data)
        users = [user.strip() for user in users]
        model = QtGui.QStandardItemModel(self.UserslistView)
        for user in users:
          item = QtGui.QStandardItem(user)
          model.appendRow(item)
        self.UserslistView.setModel(model)
        os.system("sleep 3;zenity --question --text='Do you want send mail detected users list?' --ellipsize")



    def exitSystem(self):
        print("Pressed exit_system button, exiting...")
        if os.path.exists("face_rec.run"):
            os.system("touch face_rec.stop")
            sys.exit()
        else:
            sys.exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
