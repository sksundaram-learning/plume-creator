# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/workspace_eric/plume-creator/src/plume/gui/preferences_themes.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThemesPage(object):
    def setupUi(self, ThemesPage):
        ThemesPage.setObjectName("ThemesPage")
        ThemesPage.resize(500, 347)
        self.gridLayout_2 = QtWidgets.QGridLayout(ThemesPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.customColorsBox = QtWidgets.QGroupBox(ThemesPage)
        self.customColorsBox.setFlat(False)
        self.customColorsBox.setCheckable(True)
        self.customColorsBox.setObjectName("customColorsBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.customColorsBox)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget = QtWidgets.QWidget(self.customColorsBox)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_9.setObjectName("formLayout_9")
        self.sheetColorButton = QtWidgets.QToolButton(self.widget)
        self.sheetColorButton.setText("")
        self.sheetColorButton.setObjectName("sheetColorButton")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sheetColorButton)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_20)
        self.sheetTextColorButton = QtWidgets.QToolButton(self.widget)
        self.sheetTextColorButton.setText("")
        self.sheetTextColorButton.setObjectName("sheetTextColorButton")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sheetTextColorButton)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_22)
        self.backColorButton = QtWidgets.QToolButton(self.widget)
        self.backColorButton.setText("")
        self.backColorButton.setObjectName("backColorButton")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.backColorButton)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_21)
        self.treeBackColorButton = QtWidgets.QToolButton(self.widget)
        self.treeBackColorButton.setText("")
        self.treeBackColorButton.setObjectName("treeBackColorButton")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.treeBackColorButton)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.treeTextColorButton = QtWidgets.QToolButton(self.widget)
        self.treeTextColorButton.setText("")
        self.treeTextColorButton.setObjectName("treeTextColorButton")
        self.formLayout_9.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.treeTextColorButton)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout_9.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.notesColorButton = QtWidgets.QToolButton(self.widget)
        self.notesColorButton.setText("")
        self.notesColorButton.setObjectName("notesColorButton")
        self.formLayout_9.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.notesColorButton)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.formLayout_9.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_23)
        self.notesTextColorButton = QtWidgets.QToolButton(self.widget)
        self.notesTextColorButton.setText("")
        self.notesTextColorButton.setObjectName("notesTextColorButton")
        self.formLayout_9.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.notesTextColorButton)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setObjectName("label_24")
        self.formLayout_9.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_24)
        self.resetColorsButton = QtWidgets.QToolButton(self.widget)
        self.resetColorsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/edit-undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetColorsButton.setIcon(icon)
        self.resetColorsButton.setObjectName("resetColorsButton")
        self.formLayout_9.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.resetColorsButton)
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setObjectName("label_25")
        self.formLayout_9.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_25)
        self.verticalLayout_5.addLayout(self.formLayout_9)
        self.horizontalLayout_6.addWidget(self.widget)
        self.gridLayout_2.addWidget(self.customColorsBox, 1, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(ThemesPage)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout.setObjectName("gridLayout")
        self.themeListWidget = QtWidgets.QListWidget(self.groupBox_8)
        self.themeListWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.themeListWidget.setObjectName("themeListWidget")
        self.gridLayout.addWidget(self.themeListWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)

        self.retranslateUi(ThemesPage)
        QtCore.QMetaObject.connectSlotsByName(ThemesPage)

    def retranslateUi(self, ThemesPage):

        ThemesPage.setWindowTitle(_("Form"))
        ThemesPage.setProperty("title", _("Themes"))
        self.customColorsBox.setTitle(_("Custom Colors"))
        self.label_20.setText(_("Sheet Color"))
        self.label_22.setText(_("Sheet Text Color"))
        self.label_21.setText(_("Background Color"))
        self.label_19.setText(_("Tree Background Color"))
        self.label_5.setText(_("Tree Text Color"))
        self.label_23.setText(_("Notes Color"))
        self.label_24.setText(_("Notes Text Color"))
        self.label_25.setText(_("Reset to default"))
        self.groupBox_8.setTitle(_("Theme"))
        self.themeListWidget.setSortingEnabled(True)


