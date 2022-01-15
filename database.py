from common import readBytesList, readByteslr, readInt32, searchForBytePattern, writeBytes, writeInt32
from dictionary import dataBaseIdToNameDictionary

class Database:
    def __init__(self, hexlist):
        self.chapterTrainingMagic = ["95", "C6", "C8", "4B", "FD", "9C", 
                                     "0B", "80", "43", "45", "4E", "54", 
                                     "4B", "4F", "57", "53", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter1Magic        = ["4A", "D9", "C7", "38", "35", "DB", 
                                     "81", "57", "4E", "4F", "4F", "4E",
                                     "41", "4E", "31", "30", "52", "B4",
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter2Magic        = ["C3", "FB", "C7", "38", "DB", "90", 
                                     "4A", "78", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter3Magic        = ["51", "D9", "C7", "38", "07", "26",
                                     "24", "FD", "4E", "4F", "4F", "4E",
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter4Magic        = ["C3", "FB", "C7", "38", "D1", "E9", 
                                     "1A", "88", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter5Magic        = ["C3", "FB", "C7", "38", "20", "74", 
                                     "BC", "8E", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter6Magic        = ["C3", "FB", "C7", "38", "E1", "6D", 
                                     "EF", "95", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter7Magic        = ["C3", "FB", "C7", "38", "FD", "19", 
                                     "60", "A0", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter8Magic        = ["C3", "FB", "C7", "38", "65", "BB", 
                                     "B7", "A6", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter9Magic        = ["C3", "FB", "C7", "38", "99", "C0", 
                                     "F2", "AC", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter10Magic       = ["C3", "FB", "C7", "38", "A5", "BE", 
                                     "C8", "B3", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter11Magic       = ["C3", "FB", "C7", "38", "AF", "58", 
                                     "15", "B9", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        self.chapter12Magic       = ["C3", "FB", "C7", "38", "9B", "6D", 
                                     "FB", "BD", "4E", "4F", "4F", "4E", 
                                     "41", "4E", "31", "30", "52", "B4", 
                                     "E5", "26", "FF", "FF", "FF", "FF"]
        
        self.chapterTrainingOffset = searchForBytePattern(hexlist, self.chapterTrainingMagic)
        self.chapter1Offset       = searchForBytePattern(hexlist, self.chapter1Magic)
        self.chapter2Offset       = searchForBytePattern(hexlist, self.chapter2Magic)
        self.chapter3Offset       = searchForBytePattern(hexlist, self.chapter3Magic)
        self.chapter4Offset       = searchForBytePattern(hexlist, self.chapter4Magic)
        self.chapter5Offset       = searchForBytePattern(hexlist, self.chapter5Magic)
        self.chapter6Offset       = searchForBytePattern(hexlist, self.chapter6Magic)
        self.chapter7Offset       = searchForBytePattern(hexlist, self.chapter7Magic)
        self.chapter8Offset       = searchForBytePattern(hexlist, self.chapter8Magic)
        self.chapter9Offset       = searchForBytePattern(hexlist, self.chapter9Magic)
        self.chapter10Offset      = searchForBytePattern(hexlist, self.chapter10Magic)
        self.chapter11Offset      = searchForBytePattern(hexlist, self.chapter11Magic)
        self.chapter12Offset      = searchForBytePattern(hexlist, self.chapter12Magic)
        
        self.chapterTrainingSizeAddress = self.chapterTrainingOffset + 0x18
        self.chapter1SizeAddress        = self.chapter1Offset  + 0x18
        self.chapter2SizeAddress        = self.chapter2Offset  + 0x18
        self.chapter3SizeAddress        = self.chapter3Offset  + 0x18
        self.chapter4SizeAddress        = self.chapter4Offset  + 0x18
        self.chapter5SizeAddress        = self.chapter5Offset  + 0x18
        self.chapter6SizeAddress        = self.chapter6Offset  + 0x18
        self.chapter7SizeAddress        = self.chapter7Offset  + 0x18
        self.chapter8SizeAddress        = self.chapter8Offset  + 0x18
        self.chapter9SizeAddress        = self.chapter9Offset  + 0x18
        self.chapter10SizeAddress       = self.chapter10Offset + 0x18
        self.chapter11SizeAddress       = self.chapter11Offset + 0x18
        self.chapter12SizeAddress       = self.chapter12Offset + 0x18

        self.chapterTrainingSize = readInt32(hexlist, self.chapterTrainingSizeAddress)
        self.chapter1Size        = readInt32(hexlist, self.chapter1SizeAddress)
        self.chapter2Size        = readInt32(hexlist, self.chapter2SizeAddress)
        self.chapter3Size        = readInt32(hexlist, self.chapter3SizeAddress)
        self.chapter4Size        = readInt32(hexlist, self.chapter4SizeAddress)
        self.chapter5Size        = readInt32(hexlist, self.chapter5SizeAddress)
        self.chapter6Size        = readInt32(hexlist, self.chapter6SizeAddress)
        self.chapter7Size        = readInt32(hexlist, self.chapter7SizeAddress)
        self.chapter8Size        = readInt32(hexlist, self.chapter8SizeAddress)
        self.chapter9Size        = readInt32(hexlist, self.chapter9SizeAddress)
        self.chapter10Size       = readInt32(hexlist, self.chapter10SizeAddress)
        self.chapter11Size       = readInt32(hexlist, self.chapter11SizeAddress)
        self.chapter12Size       = readInt32(hexlist, self.chapter12SizeAddress)

        self.chapterTrainingTrueSize = int(self.chapterTrainingSize / 0x14)
        self.chapter1TrueSize        = int(self.chapter1Size / 0x14)
        self.chapter2TrueSize        = int(self.chapter2Size / 0x14)
        self.chapter3TrueSize        = int(self.chapter3Size / 0x14)
        self.chapter4TrueSize        = int(self.chapter4Size / 0x14)
        self.chapter5TrueSize        = int(self.chapter5Size / 0x14)
        self.chapter6TrueSize        = int(self.chapter6Size / 0x14)
        self.chapter7TrueSize        = int(self.chapter7Size / 0x14)
        self.chapter8TrueSize        = int(self.chapter8Size / 0x14)
        self.chapter9TrueSize        = int(self.chapter9Size / 0x14)
        self.chapter10TrueSize       = int(self.chapter10Size / 0x14)
        self.chapter11TrueSize       = int(self.chapter11Size / 0x14)
        self.chapter12TrueSize       = int(self.chapter12Size / 0x14)

        self.chapterTrainingUnknownAddress = self.chapterTrainingOffset + 0x1C
        self.chapter1UnknownAddress        = self.chapter1Offset + 0x1C
        self.chapter2UnknownAddress        = self.chapter2Offset + 0x1C
        self.chapter3UnknownAddress        = self.chapter3Offset + 0x1C
        self.chapter4UnknownAddress        = self.chapter4Offset + 0x1C
        self.chapter5UnknownAddress        = self.chapter5Offset + 0x1C
        self.chapter6UnknownAddress        = self.chapter6Offset + 0x1C
        self.chapter7UnknownAddress        = self.chapter7Offset + 0x1C
        self.chapter8UnknownAddress        = self.chapter8Offset + 0x1C
        self.chapter9UnknownAddress        = self.chapter9Offset + 0x1C
        self.chapter10UnknownAddress       = self.chapter10Offset + 0x1C
        self.chapter11UnknownAddress       = self.chapter11Offset + 0x1C
        self.chapter12UnknownAddress       = self.chapter12Offset + 0x1C

        self.chapterTrainingUnknown = readBytesList(hexlist, self.chapterTrainingUnknownAddress, 0x08)
        self.chapter1Unknown        = readBytesList(hexlist, self.chapter1UnknownAddress, 0x08)
        self.chapter2Unknown        = readBytesList(hexlist, self.chapter2UnknownAddress, 0x08)
        self.chapter3Unknown        = readBytesList(hexlist, self.chapter3UnknownAddress, 0x08)
        self.chapter4Unknown        = readBytesList(hexlist, self.chapter4UnknownAddress, 0x08)
        self.chapter5Unknown        = readBytesList(hexlist, self.chapter5UnknownAddress, 0x08)
        self.chapter6Unknown        = readBytesList(hexlist, self.chapter6UnknownAddress, 0x08)
        self.chapter7Unknown        = readBytesList(hexlist, self.chapter7UnknownAddress, 0x08)
        self.chapter8Unknown        = readBytesList(hexlist, self.chapter8UnknownAddress, 0x08)
        self.chapter9Unknown        = readBytesList(hexlist, self.chapter9UnknownAddress, 0x08)
        self.chapter10Unknown       = readBytesList(hexlist, self.chapter10UnknownAddress, 0x08)
        self.chapter11Unknown       = readBytesList(hexlist, self.chapter11UnknownAddress, 0x08)
        self.chapter12Unknown       = readBytesList(hexlist, self.chapter12UnknownAddress, 0x08)

        self.chapterTrainingLogs = []
        self.chapter1Logs = []
        self.chapter2Logs = []
        self.chapter3Logs = []
        self.chapter4Logs = []
        self.chapter5Logs = []
        self.chapter6Logs = []
        self.chapter7Logs = []
        self.chapter8Logs = []
        self.chapter9Logs = []
        self.chapter10Logs = []
        self.chapter11Logs = []
        self.chapter12Logs = []

        for x in range(0, self.chapterTrainingTrueSize):
            logOffet= self.chapterTrainingOffset + 0x24 + (x * 0x14)
            self.chapterTrainingLogs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                             "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter1TrueSize):
            logOffet= self.chapter1Offset + 0x24 + (x * 0x14)
            self.chapter1Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter2TrueSize):
            logOffet= self.chapter2Offset + 0x24 + (x * 0x14)
            self.chapter2Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter3TrueSize):
            logOffet= self.chapter3Offset + 0x24 + (x * 0x14)
            self.chapter3Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter4TrueSize):
            logOffet= self.chapter4Offset + 0x24 + (x * 0x14)
            self.chapter4Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter5TrueSize):
            logOffet= self.chapter5Offset + 0x24 + (x * 0x14)
            self.chapter5Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter6TrueSize):
            logOffet= self.chapter6Offset + 0x24 + (x * 0x14)
            self.chapter6Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter7TrueSize):
            logOffet= self.chapter7Offset + 0x24 + (x * 0x14)
            self.chapter7Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter8TrueSize):
            logOffet= self.chapter8Offset + 0x24 + (x * 0x14)
            self.chapter8Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter9TrueSize):
            logOffet= self.chapter9Offset + 0x24 + (x * 0x14)
            self.chapter9Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                      "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter10TrueSize):
            logOffet= self.chapter10Offset + 0x24 + (x * 0x14)
            self.chapter10Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                       "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter11TrueSize):
            logOffet= self.chapter11Offset + 0x24 + (x * 0x14)
            self.chapter11Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                       "id":readByteslr(hexlist, logOffet, 0x14)})
        for x in range(0, self.chapter12TrueSize):
            logOffet= self.chapter12Offset + 0x24 + (x * 0x14)
            self.chapter12Logs.append({"name":dataBaseIdToNameDictionary[readByteslr(hexlist, logOffet, 0x14)],
                                       "id":readByteslr(hexlist, logOffet, 0x14)})
    

    def writeData(self, hexlist, offset):
        self.chapter1Offset = offset
        writeBytes(self.chapter1Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter1SizeAddress = offset
        self.chapter1Size = len(self.chapter1Logs) * 0x14
        self.chapter1TrueSize = len(self.chapter1Logs)
        writeInt32(self.chapter1Size , hexlist, offset)
        offset += 4
        self.chapter1UnknownAddress = offset
        writeBytes(self.chapter1Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter1Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter3Offset = offset
        writeBytes(self.chapter3Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter3SizeAddress = offset
        self.chapter3Size = len(self.chapter3Logs) * 0x14
        self.chapter3TrueSize = len(self.chapter3Logs)
        writeInt32(self.chapter3Size , hexlist, offset)
        offset += 4
        self.chapter3UnknownAddress = offset
        writeBytes(self.chapter3Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter3Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter2Offset = offset
        writeBytes(self.chapter2Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter2SizeAddress = offset
        self.chapter2Size = len(self.chapter2Logs) * 0x14
        self.chapter2TrueSize = len(self.chapter2Logs)
        writeInt32(self.chapter2Size , hexlist, offset)
        offset += 4
        self.chapter2UnknownAddress = offset
        writeBytes(self.chapter2Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter2Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter4Offset = offset
        writeBytes(self.chapter4Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter4SizeAddress = offset
        self.chapter4Size = len(self.chapter4Logs) * 0x14
        self.chapter4TrueSize = len(self.chapter4Logs)
        writeInt32(self.chapter4Size , hexlist, offset)
        offset += 4
        self.chapter4UnknownAddress = offset
        writeBytes(self.chapter4Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter4Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter5Offset = offset
        writeBytes(self.chapter5Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter5SizeAddress = offset
        self.chapter5Size = len(self.chapter5Logs) * 0x14
        self.chapter5TrueSize = len(self.chapter5Logs)
        writeInt32(self.chapter5Size , hexlist, offset)
        offset += 4
        self.chapter5UnknownAddress = offset
        writeBytes(self.chapter5Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter5Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter6Offset = offset
        writeBytes(self.chapter6Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter6SizeAddress = offset
        self.chapter6Size = len(self.chapter6Logs) * 0x14
        self.chapter6TrueSize = len(self.chapter6Logs)
        writeInt32(self.chapter6Size , hexlist, offset)
        offset += 4
        self.chapter6UnknownAddress = offset
        writeBytes(self.chapter6Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter6Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter7Offset = offset
        writeBytes(self.chapter7Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter7SizeAddress = offset
        self.chapter7Size = len(self.chapter7Logs) * 0x14
        self.chapter7TrueSize = len(self.chapter7Logs)
        writeInt32(self.chapter7Size , hexlist, offset)
        offset += 4
        self.chapter7UnknownAddress = offset
        writeBytes(self.chapter7Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter7Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter8Offset = offset
        writeBytes(self.chapter8Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter8SizeAddress = offset
        self.chapter8Size = len(self.chapter8Logs) * 0x14
        self.chapter8TrueSize = len(self.chapter8Logs)
        writeInt32(self.chapter8Size , hexlist, offset)
        offset += 4
        self.chapter8UnknownAddress = offset
        writeBytes(self.chapter8Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter8Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter9Offset = offset
        writeBytes(self.chapter9Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter9SizeAddress = offset
        self.chapter9Size = len(self.chapter9Logs) * 0x14
        self.chapter9TrueSize = len(self.chapter9Logs)
        writeInt32(self.chapter9Size , hexlist, offset)
        offset += 4
        self.chapter9UnknownAddress = offset
        writeBytes(self.chapter9Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter9Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter10Offset = offset
        writeBytes(self.chapter10Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter10SizeAddress = offset
        self.chapter10Size = len(self.chapter10Logs) * 0x14
        self.chapter10TrueSize = len(self.chapter10Logs)
        writeInt32(self.chapter10Size , hexlist, offset)
        offset += 4
        self.chapter10UnknownAddress = offset
        writeBytes(self.chapter10Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter10Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter11Offset = offset
        writeBytes(self.chapter11Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter11SizeAddress = offset
        self.chapter11Size = len(self.chapter11Logs) * 0x14
        self.chapter11TrueSize = len(self.chapter11Logs)
        writeInt32(self.chapter11Size , hexlist, offset)
        offset += 4
        self.chapter11UnknownAddress = offset
        writeBytes(self.chapter11Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter11Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapter12Offset = offset
        writeBytes(self.chapter12Magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapter12SizeAddress = offset
        self.chapter12Size = len(self.chapter12Logs) * 0x14
        self.chapter12TrueSize = len(self.chapter12Logs)
        writeInt32(self.chapter12Size , hexlist, offset)
        offset += 4
        self.chapter12UnknownAddress = offset
        writeBytes(self.chapter12Unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapter12Logs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        self.chapterTrainingOffset = offset
        writeBytes(self.chapterTrainingMagic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.chapterTrainingSizeAddress = offset
        self.chapterTrainingSize = len(self.chapterTrainingLogs) * 0x14
        self.chapterTrainingTrueSize = len(self.chapterTrainingLogs)
        writeInt32(self.chapterTrainingSize , hexlist, offset)
        offset += 4
        self.chapterTrainingUnknownAddress = offset
        writeBytes(self.chapterTrainingUnknown, hexlist, offset, 0x08, True)
        offset += 0x08
        for i in self.chapterTrainingLogs:
            logID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(logID ,hexlist, offset, 0x14, True)
            offset += 0x14
        return offset