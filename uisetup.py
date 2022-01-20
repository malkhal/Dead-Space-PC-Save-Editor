import os
from PyQt5 import QtCore, QtWidgets
from bench import Bench
from character import Character
from database import Database
from fileloadedwindow import Ui_fileloadedwindow
from inventory import Inventory, isWeapon
from keyitem import Keyitem

from mainwindow import Ui_mainwindow
from metadata import MetaData
from safe import Safe
from shop import Shop
from suit import Suit
from validatesavefile import validateSaveFile
from writesavefile import writeSaveFile
from dictionary import itemNameToIdDictionary, dataBaseIdToNameDictionary, dataBaseNameToIdDictionary, keyitemNameToIdDictionary



class MyQComboBox(QtWidgets.QComboBox):
    def __init__(self):
        QtWidgets.QComboBox.__init__(self)  
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        event.ignore()
class MainWindowUI(Ui_mainwindow):
    def retranslateUi(self, mainwindow):
        super(MainWindowUI, self).retranslateUi(mainwindow)
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Dead Space Save Editor"))
    def setupUi(self, mainwindow):
        super(MainWindowUI, self).setupUi(mainwindow)
        self.loadButton.clicked.connect(lambda: self.loadAndValidate(mainwindow))
        self.browseButton.clicked.connect(self.selectFile)
    def selectFile(self):
        self.saveFilePathLineEdit.setText(QtWidgets.QFileDialog.getOpenFileName(None, "Select Save File", os.path.expanduser('~/Documents/Electronic Arts/Dead Space'))[0])
    def loadAndValidate(self, mainwindow):
        
        try:
            with open(self.saveFilePathLineEdit.text(), 'rb') as f:
                hexdata = f.read().hex().upper()
                hexlist = list(map(''.join, zip(*[iter(hexdata)]*2)))
        except Exception as e:
            self.logTextBrowser.setText(str(e))
            
        else:
            valid, logMsg = validateSaveFile(hexlist)
            self.logTextBrowser.setText(logMsg)
            if (valid):
                self.Form = QtWidgets.QWidget()
                self.ui = FileLoadedWindowUI()
                self.ui.srcFileName = self.saveFilePathLineEdit.text()
                self.ui.setupUi(self.Form, hexlist)
                self.Form.setWindowModality(QtCore.Qt.ApplicationModal)
                self.Form.show()

class FileLoadedWindowUI(Ui_fileloadedwindow):
    def retranslateUi(self, fileloadedwindow):
        super(FileLoadedWindowUI, self).retranslateUi(fileloadedwindow)
        _translate = QtCore.QCoreApplication.translate
        fileloadedwindow.setWindowTitle(_translate("fileloadedwindow", self.srcFileName))
    def setupUi(self, fileloadedwindow, hexlist):
        super(FileLoadedWindowUI, self).setupUi(fileloadedwindow)
        self.fileloadedwindow = fileloadedwindow
        metaData = MetaData(hexlist)
        self.slotLabel.setText("Slot: {}".format(metaData.slot))
        self.chapterLabel.setText("Chapter: {}".format(metaData.chapter))
        self.checkPointLabel.setText("Check Point: {}".format(metaData.checkpoint))
        self.roundLabel.setText("Round: {}".format(metaData.round))
        self.difficultyLabel.setText("Difficulty: {}".format(metaData.difficulty))
        self.playedLabel.setText("Played: {}:{}:{}".format(metaData.hoursPlayed,metaData.minutesPlayed,metaData.secondsPlayed))
        self.hexlist = hexlist
        self.inventory = Inventory(hexlist)
        self.character = Character(hexlist)
        self.suit = Suit(hexlist)
        self.safe = Safe(hexlist)
        self.shop = Shop(hexlist)
        self.database = Database(hexlist)
        self.bench = Bench(hexlist)
        self.bench.updateBenchCheckBoxes(self)
        self.keyitem = Keyitem(hexlist)
        
        #################################################
        #                Inventory Table                #
        #################################################
        self.inventoryTable.setRowCount(self.inventory.trueSize + 1)
        x = 0
        for item in self.inventory.items:
            combobox = self.itemComboBox(x, item["name"])
            self.inventoryTable.setCellWidget(x, 0, combobox)
            self.inventoryTable.setItem(x, 1, QtWidgets.QTableWidgetItem(str(item['quantity'])))
            if isWeapon(item["id"]) :
                combobox2 = MyQComboBox()
                for i in range(4):
                    combobox2.addItem(str(i))
                    
                combobox2.setCurrentText(str(item["slot"]))
                self.inventoryTable.setCellWidget(x, 2, combobox2)
            x += 1
        combobox = self.itemComboBox(x, "", True)
        self.inventoryTable.setCellWidget(x, 0, combobox)
        self.inventoryTable.setItem(x, 1, QtWidgets.QTableWidgetItem("1"))
        self.inventoryTable.resizeColumnToContents(0)
        #################################################



        #################################################
        #                  Shop Table                   #
        #################################################
        self.shopTable.setRowCount(self.shop.trueSize + 1)
        x = 0
        for item in self.shop.items:
            combobox = self.itemComboBox(x, item["name"])
            self.shopTable.setCellWidget(x, 0, combobox)
            x += 1
        combobox = self.itemComboBox(self.shopTable.rowCount() - 1, "", True)
        self.shopTable.setCellWidget(self.shopTable.rowCount() - 1, 0, combobox)
        self.shopTable.resizeColumnToContents(0)
        #################################################

        #################################################
        #                  Safe Table                   #
        #################################################
        self.safeTable.setRowCount(self.safe.trueSize + 1)
        x = 0
        for item in self.safe.items:
            combobox = self.itemComboBox(x, item["name"])
            self.safeTable.setCellWidget(x, 0, combobox)
            self.safeTable.setItem(x, 1, QtWidgets.QTableWidgetItem(str(item['quantity'])))
            x += 1
        combobox = self.itemComboBox(x, "", True)
        self.safeTable.setCellWidget(x, 0, combobox)
        self.safeTable.setItem(x, 1, QtWidgets.QTableWidgetItem("1"))
        self.safeTable.resizeColumnToContents(0)
        #################################################


        #################################################
        #               Databas logs Table              #
        #################################################
        self.databaseLogsTable.setRowCount(len(dataBaseIdToNameDictionary))
        x = 0
        currentChapter = ""
        for i in dataBaseIdToNameDictionary:
            if x < 17: currentChapter = "Training"
            elif x < 35: currentChapter = "Chapter 1"
            elif x < 54: currentChapter = "Chapter 2"
            elif x < 67: currentChapter = "Chapter 3"
            elif x < 87: currentChapter = "Chapter 4"
            elif x < 102: currentChapter = "Chapter 5"
            elif x < 115: currentChapter = "Chapter 6"
            elif x < 128: currentChapter = "Chapter 7"
            elif x < 137: currentChapter = "Chapter 8"
            elif x < 147: currentChapter = "Chapter 9"
            elif x < 165: currentChapter = "Chapter 10"
            elif x < 175: currentChapter = "Chapter 11"
            elif x < 185: currentChapter = "Chapter 12"
            self.databaseLogsTable.setItem(x, 0, QtWidgets.QTableWidgetItem(currentChapter))
            self.databaseLogsTable.setItem(x, 1, QtWidgets.QTableWidgetItem(dataBaseIdToNameDictionary[i]))
            checkbox = QtWidgets.QCheckBox()
            if currentChapter == "Training":
                for log in self.database.chapterTrainingLogs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 1":
                for log in self.database.chapter1Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 2":
                for log in self.database.chapter2Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 3":
                for log in self.database.chapter3Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 4":
                for log in self.database.chapter4Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 5":
                for log in self.database.chapter5Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 6":
                for log in self.database.chapter6Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 7":
                for log in self.database.chapter7Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 8":
                for log in self.database.chapter8Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 9":
                for log in self.database.chapter9Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 10":
                for log in self.database.chapter10Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 11":
                for log in self.database.chapter11Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            elif currentChapter == "Chapter 12":
                for log in self.database.chapter12Logs:
                    if log["id"] == i:
                        checkbox.setChecked(True)
                        break
            
            checkboxWidget = QtWidgets.QWidget()
            checkboxLayout = QtWidgets.QHBoxLayout(checkboxWidget)
            checkboxLayout.addWidget(checkbox)
            checkboxLayout.setAlignment(QtCore.Qt.AlignCenter)
            checkboxLayout.setContentsMargins(0, 0, 0, 0)
            self.databaseLogsTable.setCellWidget(x, 2, checkboxWidget)
            x += 1
        for x in range(3): self.databaseLogsTable.resizeColumnToContents(x)
        #################################################

        #################################################
        #                 Keyitem Table                 #
        #################################################
        self.keyitemTable.setRowCount(self.keyitem.trueSize + 1)
        x = 0
        for item in self.keyitem.items:
            combobox = self.itemComboBox(x, item["name"], isKeyitem = True)
            self.keyitemTable.setCellWidget(x, 0, combobox)
            x += 1
        combobox = self.itemComboBox(self.keyitemTable.rowCount() - 1, "", True, isKeyitem = True)
        self.keyitemTable.setCellWidget(self.keyitemTable.rowCount() - 1, 0, combobox)
        self.keyitemTable.resizeColumnToContents(0)
        self.keyitemTable.objectName()
        #################################################

        self.healthSpinBox.setValue(int(self.character.health))
        self.airSpinBox.setValue(int(self.character.air))
        self.stasisSpinBox.setValue(int(self.character.stasis))
        self.creditSpinBox.setValue(self.inventory.credit)
        self.nodesSpinBox.setValue(self.character.nodes)
        for i in range(1,7):
            self.suitLevelComboBox.addItem(str(i))
            self.suitLevelComboBox.setCurrentIndex(self.suit.suitLevel)
        self.writeSaveFileButton.clicked.connect(self.saveFile)
        
    def itemComboBox(self, x, itemName = "", lastRow = False, isKeyitem = False):
            combobox = MyQComboBox()
            if isKeyitem:
                for item in keyitemNameToIdDictionary:
                    combobox.addItem(item)
            else:
                for item in itemNameToIdDictionary:
                    combobox.addItem(item)
            if not lastRow: 
                combobox.addItem("Remove")
                index = combobox.findText(itemName)
                combobox.setCurrentIndex(index)
            combobox.setProperty('row', x)
            if lastRow: 
                combobox.addItem("")
                combobox.setCurrentIndex(combobox.count() - 1)
            combobox.currentIndexChanged.connect(self.indexChanged)
            return combobox  
    def indexChanged(self):
        combobox = self.fileloadedwindow.sender()
        table = combobox.parent().parent()
        row = combobox.property('row')
        iskeyitemc = False
        if row == table.rowCount() - 1:
            newTableSize = table.rowCount() + 1
            if table.objectName() == "keyitemTable": iskeyitemc = True
            nCombobox = self.itemComboBox(row, combobox.currentText(), isKeyitem=iskeyitemc)
            table.removeRow(combobox.property('row'))
            table.setRowCount(newTableSize)
            table.setCellWidget(row, 0, nCombobox)
            if table.columnCount() > 1: table.setItem(row, 1, QtWidgets.QTableWidgetItem("1"))
            n2Combobox = self.itemComboBox(row + 1, "",True, isKeyitem=iskeyitemc)
            table.setCellWidget(row + 1, 0, n2Combobox)
            if table.columnCount() > 1: table.setItem(row + 1, 1, QtWidgets.QTableWidgetItem("1"))
            if table.columnCount() > 2:
                if isWeapon(itemNameToIdDictionary[combobox.currentText()]) :
                    slotCombobox = MyQComboBox()
                    for i in range(4):
                        slotCombobox.addItem(str(i))

                    slotCombobox.setCurrentIndex(0)
                    self.inventoryTable.setCellWidget(row, 2, slotCombobox)

        if combobox.currentText() == "Remove":
            table.removeRow(combobox.property('row'))
            for x in range(table.rowCount()):
                table.cellWidget(x, 0).setProperty('row', x)
        

    def saveFile(self):
        
        self.character.health = self.healthSpinBox.value()
        self.character.air = self.airSpinBox.value()
        self.character.stasis = self.stasisSpinBox.value()
        self.character.nodes = self.nodesSpinBox.value()
        self.inventory.credit = self.creditSpinBox.value()
        self.suit.suitLevel = self.suitLevelComboBox.currentIndex()
        items = []
        for i in range(self.shopTable.rowCount() - 1):
            name = self.shopTable.cellWidget(i,0).currentText()
            itemId = itemNameToIdDictionary[name]
            items.append({"name":name, "id":itemId, "unknown":0})
        self.shop.items = items.copy()
        items = []
        for i in range(self.inventoryTable.rowCount() - 1):
            name = self.inventoryTable.cellWidget(i,0).currentText()
            quantity = int(self.inventoryTable.item(i, 1).text())
            itemId = itemNameToIdDictionary[name]
            slot = 0
            if isWeapon(itemId): slot = int(self.inventoryTable.cellWidget(i,2).currentText())
            items.append({"name":name, "id":itemId, "slot":slot, "quantity":quantity, "unknown0":0})
        self.inventory.items = items.copy()
        slot0 = 0
        slot1 = 0
        slot2 = 0
        slot3 = 0
        for item in self.inventory.items:
            if isWeapon(item["id"]):
                if item["slot"] == 0 : slot0 += 1
                if item["slot"] == 1 : slot1 += 1
                if item["slot"] == 2 : slot2 += 1
                if item["slot"] == 3 : slot3 += 1
        if slot0 > 1 or slot1 > 1 or slot2 > 1 or slot3 > 1:
            errorMsg = QtWidgets.QMessageBox()
            errorMsg.setWindowTitle("Error")
            errorMsg.setText("File was not saved\nCheck Weapon Slots in Inventory Tab")
            errorMsg.exec()
            return
        items = []
        for i in range(self.safeTable.rowCount() - 1):
            name = self.safeTable.cellWidget(i,0).currentText()
            quantity = int(self.safeTable.item(i, 1).text())
            itemId = itemNameToIdDictionary[name]
            items.append({"unknown0":0, "name":name, "id":itemId, "unknown1":0, "quantity":quantity})
        self.safe.items = items.copy()
        items = []
        for i in range(self.keyitemTable.rowCount() - 1):
            name = self.keyitemTable.cellWidget(i,0).currentText()
            itemId = keyitemNameToIdDictionary[name]
            items.append({"unknown0":0, "name":name, "id":itemId, "unknown1":0, "quantity":1})
        self.keyitem.items = items.copy()

        chapterTrainingLogs = []
        chapter1Logs = []
        chapter2Logs = []
        chapter3Logs = []
        chapter4Logs = []
        chapter5Logs = []
        chapter6Logs = []
        chapter7Logs = []
        chapter8Logs = []
        chapter9Logs = []
        chapter10Logs = []
        chapter11Logs = []
        chapter12Logs = []
        for i in range(self.databaseLogsTable.rowCount()):
            chapter = self.databaseLogsTable.item(i, 0).text()
            name = self.databaseLogsTable.item(i, 1).text()
            logId = dataBaseNameToIdDictionary[name]
            checked = self.databaseLogsTable.cellWidget(i, 2).children()[1].isChecked()
            if checked:
                if chapter == "Training" : chapterTrainingLogs.append({"name":name, "id":logId})
                elif chapter == "Chapter 1" : chapter1Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 2" : chapter2Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 3" : chapter3Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 4" : chapter4Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 5" : chapter5Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 6" : chapter6Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 7" : chapter7Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 8" : chapter8Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 9" : chapter9Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 10" : chapter10Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 11" : chapter11Logs.append({"name":name, "id":logId})
                elif chapter == "Chapter 12" : chapter12Logs.append({"name":name, "id":logId})
        self.database.chapterTrainingLogs = chapterTrainingLogs.copy()
        self.database.chapter1Logs = chapter1Logs.copy()
        self.database.chapter2Logs = chapter2Logs.copy()
        self.database.chapter3Logs = chapter3Logs.copy()
        self.database.chapter4Logs = chapter4Logs.copy()
        self.database.chapter5Logs = chapter5Logs.copy()
        self.database.chapter6Logs = chapter6Logs.copy()
        self.database.chapter7Logs = chapter7Logs.copy()
        self.database.chapter8Logs = chapter8Logs.copy()
        self.database.chapter9Logs = chapter9Logs.copy()
        self.database.chapter10Logs = chapter10Logs.copy()
        self.database.chapter11Logs = chapter11Logs.copy()
        self.database.chapter12Logs = chapter12Logs.copy()
        self.bench.updateUpgradesList(self)
        backup = writeSaveFile(self.srcFileName, self.hexlist, self.safe, self.inventory, self.shop, self.bench, self.keyitem, self.character, self.suit, self.database)
        writeMsg = QtWidgets.QMessageBox()
        writeMsg.setWindowTitle("File Saved")
        writeMsg.setText("File saved\nOld Save Backup:\n{}".format(backup))
        writeMsg.exec()
    