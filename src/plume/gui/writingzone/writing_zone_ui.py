# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyril/Devel/plume/plume-creator/src/plume/gui/writingzone/writing_zone.ui'
#
# Created: Sat Nov 21 12:43:26 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WritingZone(object):
    def setupUi(self, WritingZone):
        WritingZone.setObjectName("WritingZone")
        WritingZone.setEnabled(True)
        WritingZone.resize(816, 523)
        self.verticalLayout = QtWidgets.QVBoxLayout(WritingZone)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sizeHorizontalSpacer_left = QtWidgets.QWidget(WritingZone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeHorizontalSpacer_left.sizePolicy().hasHeightForWidth())
        self.sizeHorizontalSpacer_left.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.sizeHorizontalSpacer_left.setPalette(palette)
        self.sizeHorizontalSpacer_left.setObjectName("sizeHorizontalSpacer_left")
        self.horizontalLayout.addWidget(self.sizeHorizontalSpacer_left)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.toolBar = ToolBar(WritingZone)
        self.toolBar.setMinimumSize(QtCore.QSize(20, 0))
        self.toolBar.setObjectName("toolBar")
        self.verticalLayout_2.addWidget(self.toolBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.richTextEdit = RichTextEdit(WritingZone)
        self.richTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.richTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.richTextEdit.setObjectName("richTextEdit")
        self.horizontalLayout.addWidget(self.richTextEdit)
        self.sizeHandle = QtWidgets.QWidget(WritingZone)
        self.sizeHandle.setMinimumSize(QtCore.QSize(4, 0))
        self.sizeHandle.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.sizeHandle.setMouseTracking(True)
        self.sizeHandle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sizeHandle.setObjectName("sizeHandle")
        self.horizontalLayout.addWidget(self.sizeHandle)
        self.sizeHorizontalSpacer_right = QtWidgets.QWidget(WritingZone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeHorizontalSpacer_right.sizePolicy().hasHeightForWidth())
        self.sizeHorizontalSpacer_right.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.sizeHorizontalSpacer_right.setPalette(palette)
        self.sizeHorizontalSpacer_right.setObjectName("sizeHorizontalSpacer_right")
        self.horizontalLayout.addWidget(self.sizeHorizontalSpacer_right)
        self.minimap = Minimap2(WritingZone)
        self.minimap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minimap.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minimap.setObjectName("minimap")
        self.horizontalLayout.addWidget(self.minimap)
        self.minimap_old = Minimap(WritingZone)
        self.minimap_old.setObjectName("minimap_old")
        self.horizontalLayout.addWidget(self.minimap_old)
        self.verticalScrollBar = QtWidgets.QScrollBar(WritingZone)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.actionCopy = QtWidgets.QAction(WritingZone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pics/32x32/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon)
        self.actionCopy.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(WritingZone)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pics/32x32/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon1)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(WritingZone)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/32x32/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon2)
        self.actionCut.setObjectName("actionCut")
        self.actionBold = QtWidgets.QAction(WritingZone)
        self.actionBold.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pics/32x32/format-text-bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon3)
        self.actionBold.setObjectName("actionBold")
        self.actionStrikethrough = QtWidgets.QAction(WritingZone)
        self.actionStrikethrough.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pics/32x32/format-text-strikethrough.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStrikethrough.setIcon(icon4)
        self.actionStrikethrough.setObjectName("actionStrikethrough")
        self.actionItalic = QtWidgets.QAction(WritingZone)
        self.actionItalic.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pics/32x32/format-text-italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon5)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(WritingZone)
        self.actionUnderline.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pics/32x32/format-text-underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon6)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionPrint_directly = QtWidgets.QAction(WritingZone)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/pics/32x32/document-print-direct.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint_directly.setIcon(icon7)
        self.actionPrint_directly.setObjectName("actionPrint_directly")

        self.retranslateUi(WritingZone)
        QtCore.QMetaObject.connectSlotsByName(WritingZone)

    def retranslateUi(self, WritingZone):

        WritingZone.setWindowTitle(_("Form"))
        self.actionCopy.setText(_("Copy"))
        self.actionCopy.setShortcut(_("Ctrl+C"))
        self.actionPaste.setText(_("Paste"))
        self.actionPaste.setShortcut(_("Ctrl+V"))
        self.actionCut.setText(_("Cut"))
        self.actionCut.setShortcut(_("Ctrl+X"))
        self.actionBold.setText(_("Bold"))
        self.actionBold.setShortcut(_("Ctrl+B"))
        self.actionStrikethrough.setText(_("Strikethrough"))
        self.actionItalic.setText(_("Italic"))
        self.actionItalic.setShortcut(_("Ctrl+I"))
        self.actionUnderline.setText(_("Underline"))
        self.actionUnderline.setShortcut(_("Ctrl+U"))
        self.actionPrint_directly.setText(_("Print directly"))
        self.actionPrint_directly.setShortcut(_("Ctrl+Shift+P"))

from .tool_bar import ToolBar
from .minimap_text_browser import Minimap2
from .rich_text_edit import RichTextEdit
from .minimap import Minimap
